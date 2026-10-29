#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verificar.py — Test automático de la memoria (proyecto memoria-procesos).

Está FUERA de borrador/ a propósito: las IAs no pueden modificarlo para aprobarse solas.
Se ejecuta desde borrador/ DESPUÉS de compilar (ver "comando_prueba" en proyecto.json).

Comprueba que:
  1. Memoria.tex incluye todos los capítulos y anexos, con \\appendix antes de los anexos.
  2. No queda texto de relleno de la plantilla (\\lipsum, MiApp, "...", dedicatoria de ejemplo, DNI).
  3. La compilación no deja referencias ni citas sin resolver, la bibliografía no está vacía y
     no hay líneas que se salgan mucho del margen.
  4. Cada \\cite existe en bib/ref.bib y cada referencia tiene una URL que aparece en las fuentes.
  5. Cada imagen existe; cada figura y tabla tiene \\caption y \\label, y se cita con \\ref en el texto.
  6. Hay un mínimo de figuras, tablas y palabras por capítulo.
  7. NINGÚN NÚMERO del texto está inventado: todos (salvo los pequeños, ≤ 20) aparecen en fuentes/.
  8. El PDF no contiene "??" (referencias rotas) ni texto de relleno.

Sale con 0 si todo va bien y con 1 si algo falla. Cada fallo indica archivo y línea cuando puede.
"""

import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

BORRADOR = Path.cwd()
CARPETA = Path(__file__).resolve().parent            # carpeta del proyecto
RAIZ = CARPETA.parents[1]                            # raíz del cerebro
FUENTES = CARPETA / "fuentes"
PRINCIPAL = BORRADOR / "Memoria.tex"

CAPITULOS = ["01-introduccion", "03-propuesta", "04-descripcion", "04b-juego", "05-evaluacion",
             "06-conclusiones"]
ANEXOS = ["a1-desarrollo", "a4-trazabilidad", "a2-material", "a3-uso-ia"]
PALABRAS_MIN = {"01-introduccion": 600, "03-propuesta": 900, "04-descripcion": 3000, "04b-juego": 1800,
                "05-evaluacion": 1200, "06-conclusiones": 500, "a1-desarrollo": 2500,
                "a4-trazabilidad": 150, "a2-material": 60, "a3-uso-ia": 250}
RESUMEN_MIN = 150
ABSTRACT_MIN = 120
FIGURAS_MIN = 30
TABLAS_MIN = 15
OVERFULL_MAX_PT = 30
# Figuras que tienen que estar (patrón en el código de los capítulos, mínimo, qué es)
FIGURAS_OBLIGATORIAS = [
    (r"figs/capturas/app/", 4, "capturas de la aplicación (figs/capturas/app/)"),
    (r"figs/capturas/hito4/", 4, "capturas del Hito 4 (figs/capturas/hito4/: correo, Google, errores)"),
    (r"figs/capturas/juego/", 8, "capturas del juego (figs/capturas/juego/)"),
    (r"figs/capturas/donetonic/", 5, "capturas de DoneTonic (figs/capturas/donetonic/: backlog, tableros y "
                                     "gráficas de los dos sprints)"),
    (r"figs/capturas/produccion/", 2, "capturas de producción (figs/capturas/produccion/)"),
    (r"figs/capturas/prueba-tecnica/", 1, "capturas de la prueba técnica (figs/capturas/prueba-tecnica/)"),
]
# Figuras con una etiqueta fija: (label, qué tiene que llevar dentro, qué es)
DIBUJO = r"\\begin\{(tikzpicture|sequencediagram)\}"
FIGURAS_CON_ETIQUETA = [
    ("fig:capas", DIBUJO, "diagrama de capas (TikZ)"),
    ("fig:modelo-datos", DIBUJO, "modelo de datos entidad-relación (TikZ), con las tablas del juego"),
    ("fig:sec-registro", DIBUJO, "diagrama de secuencia del registro (§7.1)"),
    ("fig:sec-confirmacion", DIBUJO, "diagrama de secuencia de la confirmación por correo (§7.2)"),
    ("fig:sec-login", DIBUJO, "diagrama de secuencia del inicio de sesión local (§7.3)"),
    ("fig:sec-google", DIBUJO, "diagrama de secuencia del inicio de sesión con Google (§7.4)"),
    ("fig:sec-baja", DIBUJO, "diagrama de secuencia de la baja (§7.8)"),
    ("fig:sec-partida", DIBUJO, "diagrama de secuencia de una partida del juego (§7.10)"),
    ("fig:sec-contratar", DIBUJO, "diagrama de secuencia de contratar con concurrencia optimista (§7.11)"),
    ("fig:pipeline", DIBUJO, "pipeline de integración y despliegue continuos (§7.12 y §11)"),
    ("fig:burndown-s1", r"\\begin\{axis\}", "burndown del Sprint 1 con pgfplots"),
    ("fig:burndown-s2", r"\\begin\{axis\}", "burndown REAL del Sprint 2 por fechas de los PR, con pgfplots"),
]
# Identificadores que tienen que aparecer: (patrón con {n}, desde, hasta, dónde, qué)
IDENTIFICADORES = [
    ("RF-{n:02d}", 1, 13, None, "requisito funcional"),
    ("RJ-{n:02d}", 1, 20, None, "requisito del juego"),
    ("RNF-{n:02d}", 1, 12, None, "requisito no funcional"),
    ("P{n}", 1, 48, "chapters/a4-trazabilidad.tex", "PBI"),
    ("T{n}", 1, 82, "chapters/a4-trazabilidad.tex", "tarea"),
]
PROHIBIDO = [
    (r"figs/capturas/(app|donetonic)-", "captura ANTIGUA (figs/capturas/app-… o donetonic-…): usa las nuevas de "
                                        "figs/capturas/app/, hito4/, juego/, donetonic/…"),
]
NUMERO_LIBRE = 20          # los números hasta este valor no hace falta que estén en las fuentes

RELLENO = [
    (r"\\lipsum", "texto de relleno \\lipsum"),
    (r"MiApp", "nombre de ejemplo «MiApp»"),
    (r"Aquí va la dedicatoria", "dedicatoria de ejemplo"),
    (r"\\quad\s*\\ldots|\\ldots\s*\\quad", "hueco «… » de la plantilla"),
    (r"\bDNI\b", "DNI (dato personal: no va en un repo público)"),
    (r"Nombre del (co)?director", "director de ejemplo"),
    (r"\\pcite|\\ps\b|\\fs\b|\\todo\b|\\missingfigure", "marca de pendiente de la plantilla"),
    (r"\bTODO\b|\bPENDIENTE\b", "TODO o PENDIENTE"),
    (r"Lorem ipsum", "texto de relleno"),
]

fallos: list[str] = []


def fallo(msg: str):
    fallos.append(msg)


def leer(ruta: Path) -> str:
    return ruta.read_text(encoding="utf-8", errors="replace") if ruta.exists() else ""


def sin_comentarios(texto: str) -> str:
    """Quita lo que va tras un % no escapado, conservando las líneas (para dar números de línea)."""
    return "\n".join(re.split(r"(?<!\\)%", l, maxsplit=1)[0] for l in texto.splitlines())


def linea_de(texto: str, pos: int) -> int:
    return texto.count("\n", 0, pos) + 1


def quitar_entornos(texto: str, nombres: tuple[str, ...]) -> str:
    """Vacía el contenido de ciertos entornos (TikZ, código...) conservando los saltos de línea."""
    for n in nombres:
        texto = re.sub(r"\\begin\{%s\}.*?\\end\{%s\}" % (n, n),
                       lambda m: "\n" * m.group(0).count("\n"), texto, flags=re.S)
    return texto


def archivos_tex() -> dict[str, str]:
    """{nombre: texto sin comentarios} de los capítulos, anexos y el preámbulo."""
    res = {}
    for n in CAPITULOS + ANEXOS:
        res[f"chapters/{n}.tex"] = sin_comentarios(leer(BORRADOR / "chapters" / f"{n}.tex"))
    for extra in ("elements/preambulo.tex", "elements/portada.tex", "include/opciones.tex"):
        res[extra] = sin_comentarios(leer(BORRADOR / extra))
    return res


# ---------- 1. Estructura ----------

def comprobar_estructura():
    principal = sin_comentarios(leer(PRINCIPAL))
    if not principal:
        fallo("Falta Memoria.tex")
        return
    for n in CAPITULOS + ANEXOS:
        if not (BORRADOR / "chapters" / f"{n}.tex").exists():
            fallo(f"Falta chapters/{n}.tex")
        if not re.search(r"\\(input|include)\{chapters/%s(\.tex)?\}" % re.escape(n), principal):
            fallo(f"Memoria.tex no incluye chapters/{n} (\\input{{chapters/{n}}})")
    pos_ap = principal.find("\\appendix")
    pos_a1 = min((p for p in (principal.find(f"chapters/{n}") for n in ANEXOS) if p >= 0), default=-1)
    if pos_ap < 0 or (pos_a1 >= 0 and pos_ap > pos_a1):
        fallo("Memoria.tex: \\appendix tiene que ir justo antes de los anexos (chapters/a1-…)")


# ---------- 2. Relleno ----------

def comprobar_relleno(textos: dict[str, str]):
    for nombre, texto in textos.items():
        for patron, que in RELLENO:
            for m in re.finditer(patron, texto):
                fallo(f"{nombre}:{linea_de(texto, m.start())}: queda {que}")
                break


# ---------- 3. Log de la compilación ----------

def comprobar_log():
    log = leer(BORRADOR / "Memoria.log")
    if not log:
        fallo("No hay Memoria.log: compila antes de verificar")
        return
    for m in re.finditer(r"(Citation|Reference) [`'](.+?)' on page \d+ undefined", log):
        fallo(f"Memoria.log: {'cita' if m.group(1) == 'Citation' else 'referencia'} sin resolver: {m.group(2)}")
    for m in re.finditer(r"Float too large for page by ([\d.]+)pt", log):
        fallo(f"Memoria.log: una tabla o figura no cabe en la página (sobran {float(m.group(1)):.0f} pt): "
              "si es una tabla larga, usa longtable en vez de table")
    if "Empty `thebibliography'" in log:
        fallo("La bibliografía sale vacía: hay que citar las referencias con \\cite en el texto")
    for m in re.finditer(r"Overfull \\hbox \(([\d.]+)pt too wide\) (.*)", log):
        if float(m.group(1)) > OVERFULL_MAX_PT:
            # El archivo es el último «(./ruta.tex» abierto antes del aviso; las 2 líneas siguientes dicen qué se sale
            archivo = (re.findall(r"\(\./([^\s()]+\.tex)", log[:m.start()]) or ["?"])[-1]
            texto = " ".join(log[m.end():].strip().splitlines()[:2])[:120]
            fallo(f"{archivo}: algo se sale {float(m.group(1)):.0f} pt del margen ({m.group(2).strip()[:40]}): «{texto}». "
                  "Si es una tabla o imagen, estréchala; si es texto con una cita o una ruta larga que no se parte, "
                  "revisa las lecciones de la memoria")


# ---------- 4. Bibliografía ----------

def entradas_bib() -> dict[str, str]:
    bib = leer(BORRADOR / "bib" / "ref.bib")
    entradas = {}
    for m in re.finditer(r"@\w+\s*\{\s*([^,\s]+)\s*,(.*?)(?=\n@|\Z)", bib, flags=re.S):
        entradas[m.group(1)] = m.group(2)
    return entradas


def comprobar_bibliografia(textos: dict[str, str], fuentes: str):
    entradas = entradas_bib()
    if not entradas:
        fallo("bib/ref.bib no tiene ninguna referencia")
    citadas = set()
    for nombre, texto in textos.items():
        for m in re.finditer(r"\\(?:no)?cite[pt]?\*?(?:\[[^\]]*\])?\{([^}]*)\}", texto):
            for clave in (c.strip() for c in m.group(1).split(",")):
                citadas.add(clave)
                if clave not in entradas:
                    fallo(f"{nombre}:{linea_de(texto, m.start())}: \\cite{{{clave}}} no existe en bib/ref.bib")
    for clave, cuerpo in entradas.items():
        urls = re.findall(r"https?://[^\s}\"]+", cuerpo)
        if not urls and clave != "enunciado":   # el PDF del enunciado de la asignatura no tiene URL
            fallo(f"bib/ref.bib: {clave} no tiene URL (en howpublished o url); "
                  "solo valen referencias que estén en las fuentes")
        for url in urls:
            if url.rstrip("/.") not in fuentes:
                fallo(f"bib/ref.bib: {clave}: la URL {url} no aparece en las fuentes (¿inventada?)")
        if not re.search(r"\byear\s*=", cuerpo):
            fallo(f"bib/ref.bib: {clave} no tiene year (si la fuente no da fecha, year = {{s.f.}})")
        if clave not in citadas:
            fallo(f"bib/ref.bib: {clave} no se cita en ningún sitio (cítala con \\cite o quítala)")


# ---------- 5 y 6. Figuras, tablas y palabras ----------

def comprobar_flotantes(textos: dict[str, str]):
    todo = "\n".join(textos.values())
    referidas = set()
    for m in re.finditer(r"\\(?:auto|page|c|C|name)?ref\{([^}]*)\}", todo):
        referidas.update(x.strip() for x in m.group(1).split(","))
    figuras = tablas = 0
    for nombre, texto in textos.items():
        for m in re.finditer(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]*)\}", texto):
            ruta = m.group(1).strip()
            if not any((BORRADOR / (ruta + ext)).exists() for ext in ("", ".png", ".pdf", ".jpg")):
                fallo(f"{nombre}:{linea_de(texto, m.start())}: no existe la imagen {ruta}")
        for tipo in ("figure", "table"):
            for m in re.finditer(r"\\begin\{%s\*?\}(.*?)\\end\{%s\*?\}" % (tipo, tipo), texto, flags=re.S):
                n = linea_de(texto, m.start())
                cuerpo = m.group(1)
                if tipo == "figure":
                    figuras += 1
                else:
                    tablas += 1
                if "\\caption" not in cuerpo:
                    fallo(f"{nombre}:{n}: {tipo} sin \\caption")
                etiquetas = re.findall(r"\\label\{([^}]*)\}", cuerpo)
                if not etiquetas:
                    fallo(f"{nombre}:{n}: {tipo} sin \\label")
                for e in etiquetas:
                    if e not in referidas:
                        fallo(f"{nombre}:{n}: la {('figura' if tipo == 'figure' else 'tabla')} {e} "
                              "no se cita en el texto (usa \\ref{" + e + "})")
    codigo = "\n".join(v for k, v in textos.items() if k.startswith("chapters/"))
    for patron, minimo, que in FIGURAS_OBLIGATORIAS:
        hay = len(set(re.findall(patron + r"[^}]*", codigo)))
        if hay < minimo:
            fallo(f"Faltan {que}: hay {hay} distintas y se piden al menos {minimo}")
    cuerpos = re.findall(r"\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}", codigo, flags=re.S)
    for etiqueta, patron, que in FIGURAS_CON_ETIQUETA:
        con = [c for c in cuerpos if "\\label{%s}" % etiqueta in c]
        if not con:
            fallo(f"Falta la figura {etiqueta}: {que}")
        elif not re.search(patron, con[0]):
            fallo(f"La figura {etiqueta} tiene que ser un dibujo ({que}), no una imagen")
    for patron, que in PROHIBIDO:
        for nombre, texto in textos.items():
            for m in re.finditer(patron, texto):
                fallo(f"{nombre}:{linea_de(texto, m.start())}: {que}")
                break
    if figuras < FIGURAS_MIN:
        fallo(f"Hay {figuras} figuras y se piden al menos {FIGURAS_MIN}")
    if tablas < TABLAS_MIN:
        fallo(f"Hay {tablas} tablas y se piden al menos {TABLAS_MIN}")
    return figuras, tablas


def palabras(texto: str) -> int:
    texto = quitar_entornos(texto, ("tikzpicture", "lstlisting", "verbatim"))
    texto = re.sub(r"\\(begin|end|label|ref|cite[pt]?|includegraphics|input|url|href)\*?(\[[^\]]*\])?\{[^}]*\}", " ", texto)
    texto = re.sub(r"\\[a-zA-Z]+\*?", " ", texto)
    return len(re.findall(r"[A-Za-zÁÉÍÓÚÜÑáéíóúüñ]{2,}", texto))


def comprobar_palabras(textos: dict[str, str]) -> int:
    total = 0
    for n, minimo in PALABRAS_MIN.items():
        cuantas = palabras(textos.get(f"chapters/{n}.tex", ""))
        total += cuantas
        if cuantas < minimo:
            fallo(f"chapters/{n}.tex: {cuantas} palabras, mínimo {minimo}")
    pre = textos.get("elements/preambulo.tex", "")
    for titulo, minimo, clave in (("Resumen", RESUMEN_MIN, "Palabras clave"), ("Abstract", ABSTRACT_MIN, "Keywords")):
        m = re.search(r"\{%s\}\}(.*?)(\\cleardoublepage|\Z)" % titulo, pre, flags=re.S)
        if not m:
            fallo(f"elements/preambulo.tex: no encuentro el {titulo} (página con \\bft{{{titulo}}}, como el Resumen)")
            continue
        if palabras(m.group(1)) < minimo:
            fallo(f"elements/preambulo.tex: el {titulo} tiene {palabras(m.group(1))} palabras, mínimo {minimo}")
        if clave not in m.group(1):
            fallo(f"elements/preambulo.tex: al {titulo} le faltan las «{clave}»")
    return total


def comprobar_identificadores(textos: dict[str, str]):
    todo = "\n".join(textos.values())
    for patron, desde, hasta, donde, que in IDENTIFICADORES:
        texto = textos.get(donde, "") if donde else todo
        faltan = [patron.format(n=n) for n in range(desde, hasta + 1)
                  if not re.search(r"(?<![A-Za-z0-9])%s(?![0-9])" % re.escape(patron.format(n=n)), texto)]
        if faltan:
            lugar = f" en {donde}" if donde else ""
            fallo(f"Falta{'n' if len(faltan) > 1 else ''} {len(faltan)} {que}(s){lugar}: {', '.join(faltan[:12])}"
                  + (" …" if len(faltan) > 12 else ""))


# ---------- 7. Números ----------

NUMERO = re.compile(r"\d+(?:[.,]\d+)*")


def normalizar(numero: str) -> str:
    if re.fullmatch(r"\d{1,3}(\.\d{3})+", numero):   # 1.128 → 1128 (separador de miles)
        return numero.replace(".", "")
    return numero


def es_libre(numero: str) -> bool:
    try:
        return float(numero.replace(",", ".")) <= NUMERO_LIBRE
    except ValueError:
        return False


def limpiar_para_numeros(texto: str) -> str:
    texto = quitar_entornos(texto, ("tikzpicture", "axis", "lstlisting", "verbatim"))
    # argumentos que no son texto: etiquetas, citas, archivos, URLs, colores, medidas de columnas
    texto = re.sub(r"\\(label|ref|autoref|pageref|cite[pt]?|includegraphics|input|include|url|"
                   r"definecolor|setlength|vspace|hspace|fontsize|rule|cline|columncolor|rowcolor|"
                   r"cellcolor|arraystretch|bibliography|raisebox|resizebox|scalebox)\*?(\[[^\]]*\])?"
                   r"(\{[^}]*\})+", " ", texto)
    texto = re.sub(r"\\href\{[^}]*\}", " ", texto)
    texto = re.sub(r"\\begin\{(tabular|tabularx|longtable)\*?\}(\{[^}]*\})?(\{(?:[^{}]|\{[^{}]*\})*\})",
                   " ", texto)
    texto = re.sub(r"\[[^\]\n]*\]", " ", texto)                                # opciones [..]
    texto = re.sub(r"-?\d*\.?\d+\s*\\(text|line|column|paper)(width|height)", " ", texto)
    texto = re.sub(r"-?\d*\.?\d+\s*(pt|cm|mm|em|ex|bp|pc)\b", " ", texto)
    texto = texto.replace("\\,", "").replace("~", " ").replace("{}", "")
    return texto


def comprobar_numeros(textos: dict[str, str], fuentes: str):
    validos = {normalizar(x) for x in NUMERO.findall(fuentes.replace("\u202f", "").replace("\u00a0", " "))}
    vistos = 0
    for nombre, texto in textos.items():
        if nombre in ("elements/portada.tex", "include/opciones.tex"):
            continue
        limpio = limpiar_para_numeros(texto)
        for m in NUMERO.finditer(limpio):
            num = normalizar(m.group(0))
            if es_libre(num) or num in validos:
                continue
            if vistos < 15:
                fallo(f"{nombre}:{linea_de(limpio, m.start())}: el número «{m.group(0)}» no aparece en las "
                      "fuentes (¿inventado o mal copiado?)")
            vistos += 1
    if vistos > 15:
        fallo(f"… y {vistos - 15} números más que no están en las fuentes")


# ---------- 8. PDF ----------

def comprobar_pdf():
    pdf = BORRADOR / "Memoria.pdf"
    if not pdf.exists():
        fallo("No hay Memoria.pdf")
        return
    if not shutil.which("pdftotext"):
        print("(aviso: sin pdftotext no se revisa el texto del PDF)")
        return
    texto = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True,
                           text=True, errors="replace").stdout
    if "??" in texto:
        fallo("El PDF contiene «??»: hay referencias o citas rotas")
    for m in re.finditer(r"\[[^\[\]\n]{0,60}, \]|\[de [A-Z][^\]\n]{0,40}\]", texto):
        fallo(f"El PDF tiene una cita mal formada «{m.group(0)}»: falta el año o el autor corporativo va sin "
              "doble llave (author = {{Universidad de Castilla-La Mancha}})")
        break
    if "Lorem ipsum" in texto or "Nam dui ligula" in texto:
        fallo("El PDF contiene texto de relleno (lipsum)")


def leer_fuentes() -> str:
    """Las mismas fuentes que leen las IAs: las de proyecto.json, incluidas las de repos públicos."""
    cfg = json.loads((CARPETA / "proyecto.json").read_text(encoding="utf-8-sig"))
    if not cfg.get("fuentes"):
        return "\n".join(leer(p) for p in sorted(FUENTES.glob("*.md")))
    sys.path.insert(0, str(RAIZ / "scripts"))
    from cerebro import repos
    if not repos.repos_listos(CARPETA, cfg):   # p. ej. si se ejecuta a mano, fuera del cerebro
        repos.preparar(CARPETA, cfg)
    return repos.texto_fuentes(CARPETA, cfg)


def main():
    fuentes = leer_fuentes()
    if not fuentes:
        print(f"ERROR: no hay fuentes en {FUENTES}")
        return 1
    textos = archivos_tex()
    comprobar_estructura()
    comprobar_relleno(textos)
    comprobar_log()
    comprobar_bibliografia(textos, fuentes)
    figuras, tablas = comprobar_flotantes(textos)
    total = comprobar_palabras(textos)
    comprobar_identificadores(textos)
    comprobar_numeros(textos, fuentes)
    comprobar_pdf()

    if fallos:
        print(f"VERIFICACIÓN FALLIDA: {len(fallos)} problema(s)")
        for f in fallos:
            print("  - ERROR:", f)
        return 1
    print(f"VERIFICACIÓN OK: {figuras} figuras, {tablas} tablas, {total} palabras en capítulos y anexos")
    return 0


if __name__ == "__main__":
    sys.exit(main())
