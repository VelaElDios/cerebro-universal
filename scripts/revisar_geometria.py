"""
Revisión GEOMÉTRICA de los diagramas del PDF (sin IA, exacta): lee del PDF las líneas, las cajas y las letras
de cada diagrama y comprueba las reglas 16-18 con coordenadas reales:

  - una línea o flecha que pasa por encima de letras (atraviesa una caja con texto o una etiqueta);
  - cajas que se pisan entre sí;
  - palabras partidas con guion dentro del diagrama («render-», «chi-»);
  - letras demasiado pequeñas (el diagrama se ha encogido para caber: adjustbox, resizebox, scale).

Se usa desde revisar_figuras.py. Necesita pdfplumber (si no está, avisa y no bloquea).
"""

import re

TAM_MIN = 7.5          # pt reales en el PDF: por debajo no se lee bien en papel
MARCOS = {"alt", "else", "lop", "loop", "opt", "par", "break", "critical"}
MARGEN_LETRA = 0.3     # se recorta cada letra un 30% por cada lado (que rozar el borde no cuente)


def _seg_corta_rect(p, q, r) -> bool:
    """¿El segmento p-q atraviesa el rectángulo r=(x0,y0,x1,y1)? (Liang-Barsky)"""
    x0, y0, x1, y1 = r
    dx, dy = q[0] - p[0], q[1] - p[1]
    t0, t1 = 0.0, 1.0
    for pp, qq in ((-dx, p[0] - x0), (dx, x1 - p[0]), (-dy, p[1] - y0), (dy, y1 - p[1])):
        if pp == 0:
            if qq < 0:
                return False
            continue
        t = qq / pp
        if pp < 0:
            t0 = max(t0, t)
        else:
            t1 = min(t1, t)
        if t0 > t1:
            return False
    return True


def _encoger(b, f):
    w, h = b[2] - b[0], b[3] - b[1]
    return (b[0] + w * f, b[1] + h * f, b[2] - w * f, b[3] - h * f)


def _se_pisan(a, b, holgura=1.0) -> bool:
    return (min(a[2], b[2]) - max(a[0], b[0]) > holgura) and (min(a[3], b[3]) - max(a[1], b[1]) > holgura)


def _dentro(a, b) -> bool:
    return a[0] >= b[0] - 1 and a[1] >= b[1] - 1 and a[2] <= b[2] + 1 and a[3] <= b[3] + 1


def _es_parrafo(linea, ancho_pagina) -> bool:
    """Línea del texto normal (no del dibujo): letra de tamaño normal y casi todo el ancho."""
    chars = [c for c in linea.get("chars", []) if c["text"].strip()]
    if not chars:
        return False
    tam = sorted(c["size"] for c in chars)[len(chars) // 2]
    return tam >= 9.5 and (linea["x1"] - linea["x0"]) > ancho_pagina * 0.55 and len(linea["text"]) > 50


def _caption_top(pagina, numero: str):
    """Coordenada superior del pie «Figura N:» en la página, y la del pie anterior (si lo hay)."""
    lineas = pagina.extract_text_lines() if hasattr(pagina, "extract_text_lines") else []
    este, anteriores = None, []
    for l in lineas:
        if re.match(r"^Figura\s*" + re.escape(numero) + r"\s*:", l["text"]):
            este = l
        elif re.match(r"^(Figura\s*[\dA-Z.]+\s*:|Tabla\s*[\dA-Z.]+\s*:|\([a-z]\))", l["text"]):
            anteriores.append(l)
        elif _es_parrafo(l, pagina.width):
            anteriores.append(l)
    if not este:
        return None, None
    previos = [l["bottom"] for l in anteriores if l["bottom"] <= este["top"]]
    return este["top"], (max(previos) if previos else 0)


def revisar(ruta_pdf, numero: str, n_pagina: int) -> list[str]:
    """Problemas geométricos del diagrama «Figura numero» en la página n_pagina (1 = primera)."""
    import pdfplumber
    with pdfplumber.open(str(ruta_pdf)) as pdf:
        pag = pdf.pages[n_pagina - 1]
        abajo, arriba = _caption_top(pag, numero)
        if abajo is None:
            return []
        ancho_util = pag.width * 0.7
        # Trazos del dibujo: caminos dentro de la franja (sin las rayas de cabecera/pie de página)
        caminos = []
        for o in list(pag.lines) + list(pag.curves) + list(pag.rects):
            if o["top"] < arriba - 1 or o["bottom"] > abajo + 1:
                continue
            if o["x1"] - o["x0"] > ancho_util and o["bottom"] - o["top"] < 1:
                continue
            pts = o.get("pts") or [(o["x0"], o["top"]), (o["x1"], o["top"]), (o["x1"], o["bottom"]),
                                   (o["x0"], o["bottom"]), (o["x0"], o["top"])]
            caminos.append((o, [(float(x), float(y)) for x, y in pts]))
        if not caminos:
            return []
        zona = (min(o["x0"] for o, _ in caminos), min(o["top"] for o, _ in caminos),
                max(o["x1"] for o, _ in caminos), max(o["bottom"] for o, _ in caminos))
        letras = [c for c in pag.chars if c["text"].strip() and _dentro(
            (c["x0"], c["top"], c["x1"], c["bottom"]), (zona[0] - 2, zona[1] - 2, zona[2] + 2, zona[3] + 2))]
        # Letras dibujadas dos veces casi en el mismo sitio (negrita falsa de las etiquetas alt/else/loop de
        # los diagramas de secuencia): se queda una sola
        unicas = []
        for c in letras:
            if not any(u["text"] == c["text"] and abs(u["x0"] - c["x0"]) < 1.5 and abs(u["top"] - c["top"]) < 1.0
                       for u in unicas[-6:]):
                unicas.append(c)
        letras = unicas
        if not letras:
            return []
        problemas = []

        # 1. Letras pequeñas
        tams = sorted(c["size"] for c in letras)
        mediana = tams[len(tams) // 2]
        if mediana < TAM_MIN:
            problemas.append(f"letras de {mediana:.1f} pt (mínimo {TAM_MIN}): el diagrama se ha encogido para "
                             "caber; hay que rehacerlo más estrecho (menos columnas, cajas más pequeñas o en vertical) "
                             "en vez de escalarlo")

        # Palabras del diagrama (para decir qué texto queda tapado)
        recorte = (max(0, zona[0] - 2), max(0, zona[1] - 2), min(pag.width, zona[2] + 2), min(pag.height, zona[3] + 2))
        if zona[2] > pag.width + 1 or zona[0] < -1:
            problemas.append(f"el diagrama se sale de la página ({max(zona[2] - pag.width, -zona[0]):.0f} pt): hay que "
                             "estrecharlo sin escalarlo (menos separación, etiquetas o nombres más cortos)")
        palabras = pag.crop(recorte).extract_words(
            keep_blank_chars=False, use_text_flow=False, x_tolerance=1.2)

        def palabra_de(c):
            for w in palabras:
                if w["x0"] - 0.5 <= c["x0"] and c["x1"] <= w["x1"] + 0.5 and w["top"] - 0.5 <= c["top"] <= w["bottom"]:
                    return w["text"]
            return c["text"]

        # 2. Trazos que pasan por encima de letras
        tapadas = []
        for o, pts in caminos:
            if len(pts) < 2:
                continue
            for c in letras:
                caja = _encoger((c["x0"], c["top"], c["x1"], c["bottom"]), MARGEN_LETRA)
                if any(_seg_corta_rect(pts[i], pts[i + 1], caja) for i in range(len(pts) - 1)):
                    p = palabra_de(c)
                    if re.sub(r"(.)\1+", r"\1", p.lower()) in MARCOS:
                        continue   # pestaña «alt», «else», «loop»… de un diagrama de secuencia: el marco la rodea
                    tapadas.append(p)
        if tapadas:
            vistas = list(dict.fromkeys(tapadas))
            problemas.append(f"líneas o flechas que pasan por encima del texto de {len(vistas)} caja(s)/etiqueta(s): "
                             + ", ".join(f"«{v}»" for v in vistas[:8]) + (" …" if len(vistas) > 8 else "")
                             + ". Cada flecha debe ir de una caja a la siguiente (o con codos) sin cruzar otras; en un diagrama de "
                               "secuencia, que ninguna línea de vida cruce un texto (etiquetas más cortas o en dos líneas, "
                               "o participantes reordenados)")

        # 3. Cajas que se pisan (caminos cerrados de tamaño de caja)
        cajas = []
        for o, pts in caminos:
            w, h = o["x1"] - o["x0"], o["bottom"] - o["top"]
            cerrado = len(pts) > 3 and abs(pts[0][0] - pts[-1][0]) < 1 and abs(pts[0][1] - pts[-1][1]) < 1
            if cerrado and w > 12 and h > 8:
                cajas.append((o["x0"], o["top"], o["x1"], o["bottom"]))
        pisadas = set()
        for i, a in enumerate(cajas):
            for b in cajas[i + 1:]:
                if _se_pisan(a, b, 2.0) and not _dentro(a, b) and not _dentro(b, a):
                    pisadas.add((a, b))
        # Texto encima de texto (dos palabras distintas en el mismo sitio)
        for i, a in enumerate(palabras):
            for b in palabras[i + 1:]:
                if _se_pisan((a["x0"], a["top"], a["x1"], a["bottom"]), (b["x0"], b["top"], b["x1"], b["bottom"]), 0.8):
                    pisadas.add((a["text"], b["text"]))
        if pisadas:
            textos = []
            for a, b in list(pisadas)[:4]:
                if isinstance(a, str):
                    textos.append(f"«{a}» con «{b}»")
            problemas.append(f"{len(pisadas)} solape(s) de cajas o textos"
                             + (": " + ", ".join(textos) if textos else "")
                             + ". Hay que separar las cajas (más distancia o otra colocación)")

        # 4. Palabras partidas con guion
        partidas = [w["text"] for w in palabras if re.search(r"\w-$", w["text"])]
        if partidas:
            problemas.append("palabras partidas con guion dentro de las cajas: "
                             + ", ".join(f"«{p}»" for p in partidas[:6])
                             + ". Usa cajas más anchas, \\mbox{} o salto de línea manual (\\\\) en vez de dejar que "
                               "LaTeX parta los nombres")
        return problemas
