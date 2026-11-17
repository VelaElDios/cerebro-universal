"""
El jardinero: cuida el vault para que crecer no lo llene de ruido. Proyecto de tipo "jardin"
(proyectos/jardinero/proyecto.json, una vez al día). En cada pasada:

  1. Comprueba citas de notas «propuestas»: busca en su fuente la frase más parecida; si está casi igual
     (≥ 90 %), pone la cita literal y la nota pasa a «verificado». Sin IA.
  2. Enlaza notas que hablan de lo mismo (embeddings) y todavía no se enlazaban. Sin IA.
  3. Fusiona notas repetidas (muy parecidas y del mismo tipo): una IA las junta sin perder datos, la otra
     se borra y los enlaces del vault pasan a la que queda.
  4. Busca contradicciones entre notas parecidas: si una IA ve que dicen cosas distintas, las marca a las
     dos («⚠️ Posible contradicción») y las baja a «propuesto» hasta que se aclare.

Todo queda en proyectos/jardinero/bitacora.md.
"""

import difflib
import json
import re
from pathlib import Path

from . import conocimiento, dataset, embeddings, mapas, nucleo, repos
from . import proveedores as prov

UMBRAL_ENLACE = 0.80
UMBRAL_DUPLICADO = 0.93
UMBRAL_CONTRADICCION = 0.82
MAX_FUSIONES = 6
MAX_CONTRADICCIONES = 6
MAX_ENLACES_POR_NOTA = 3
MIN_PARA_IA = 4 * 60

SISTEMA_FUSION = """Eres el JARDINERO de "Cerebro Universal", la memoria compartida de varias IAs. Te paso dos notas que
parecen decir lo mismo. Júntalas en UNA sola nota que no pierda ningún dato, paso ni código de ninguna de las
dos, sin repetir nada y sin inventar. Si se contradicen en algo, dilo en CONTRADICCION.

Responde EXACTAMENTE así:
<<<TITULO>>>
el mejor título para la nota fusionada
<<<CONTENIDO>>>
el contenido fusionado, en Markdown
<<<CONTRADICCION>>>
no   (o una frase con lo que no cuadra entre las dos)"""

SISTEMA_CONTRADICCION = """Eres el JARDINERO de "Cerebro Universal". Te paso dos notas sobre temas parecidos. ¿Se CONTRADICEN
(una cifra, una fecha, un nombre o una afirmación distinta sobre lo mismo)? Que hablen de cosas distintas
o que una amplíe a la otra NO es contradicción.

Responde EXACTAMENTE así:
<<<CONTRADICCION>>>
no   (o: si)
<<<EXPLICACION>>>
si la hay, una o dos frases: qué dice cada una."""


# ---------- utilidades ----------

def _leer_nota(ruta_rel: str) -> dict | None:
    from .memoria import leer
    ruta = nucleo.RAIZ / ruta_rel
    if not ruta.exists():
        return None
    n = leer(ruta)
    if n:
        n["ruta"] = ruta_rel
        for lista in ("fuentes",):
            if isinstance(n.get(lista), str):
                n[lista] = [n[lista]]
            n.setdefault(lista, [])
    return n


def _guardar_nota(n: dict):
    datos = {k: v for k, v in n.items() if k not in ("nombre", "ruta")}
    conocimiento._escribir(nucleo.RAIZ / n["ruta"], datos)


def _texto_fuente(carpeta_aprendizaje: Path, fuente: str) -> str | None:
    """Texto de la fuente de una nota (archivo del vault, de un repo descargado o transcripción guardada)."""
    fuente = re.sub(r"\s*\(.*?\)\s*$", "", fuente).strip()
    candidatos = []
    if fuente.startswith("repo:"):
        candidatos.append(("repo", fuente))
    else:
        candidatos += [nucleo.RAIZ / fuente.lstrip("./"), carpeta_aprendizaje / fuente]
        for proy in (nucleo.RAIZ / "proyectos").glob("*"):
            candidatos += [proy / fuente, proy / "borrador" / fuente]
    for c in candidatos:
        if c == ("repo", fuente):
            for proy in (nucleo.RAIZ / "proyectos").glob("*"):
                for _, ruta in repos.resolver(proy, fuente):
                    return ruta.read_text(encoding="utf-8", errors="replace")
            continue
        if isinstance(c, Path) and c.is_file() and c.suffix.lower() in (".md", ".txt", ".tex", ".json", ".py", ".js", ".bib"):
            return c.read_text(encoding="utf-8", errors="replace")
    trans = carpeta_aprendizaje / repos.CARPETA_REPOS / "datos" / "transcripciones"
    if trans.exists():
        nombre = conocimiento.nombre_de(fuente)[:80]
        t = trans / f"{nombre}.md"
        if t.exists():
            return t.read_text(encoding="utf-8").split("\n---\n", 1)[-1]
    return None


def _mejor_frase(cita: str, texto: str) -> tuple[float, str]:
    """La frase del texto que más se parece a la cita (ventanas de su mismo tamaño)."""
    cita_n = conocimiento.normalizar(cita)
    if not cita_n:
        return 0.0, ""
    lineas = [l.strip() for l in re.split(r"(?<=[.!?:;])\s+|\n+", texto) if l.strip()]
    mejor = (0.0, "")
    largo = len(cita_n)
    for i in range(len(lineas)):
        trozo = ""
        for j in range(i, min(i + 4, len(lineas))):
            trozo = (trozo + " " + lineas[j]).strip()
            r = difflib.SequenceMatcher(None, cita_n, conocimiento.normalizar(trozo)).ratio()
            if r > mejor[0]:
                mejor = (r, trozo)
            if len(conocimiento.normalizar(trozo)) > largo * 1.5:
                break
    return mejor


def _cita_de(cuerpo: str) -> tuple[str, str] | None:
    m = re.search(r"^> (.+)\n> — `([^`]+)`", cuerpo, re.M)
    return (m.group(1).strip(), m.group(2).strip()) if m else None


# ---------- 1. verificar citas ----------

def verificar_propuestas(carpeta: Path) -> list[str]:
    hechas = []
    for n in conocimiento.todas():
        if n.get("confianza") == "verificado":
            continue
        c = _cita_de(n["cuerpo"])
        if not c:
            continue
        cita, fuente = c
        texto = _texto_fuente(carpeta, fuente) or "".join(
            t for f in n.get("fuentes", []) if (t := _texto_fuente(carpeta, f)))
        if not texto:
            continue
        if conocimiento.normalizar(cita) in conocimiento.normalizar(texto):
            ratio, frase = 1.0, cita
        else:
            ratio, frase = _mejor_frase(cita, texto)
        if ratio >= 0.9 and frase:
            frase = re.sub(r"\s+", " ", frase).strip()
            n["cuerpo"] = n["cuerpo"].replace(f"> {cita}\n", f"> {frase}\n", 1).replace(" (cita sin comprobar)", "")
            n["confianza"] = "verificado"
            n["actualizado"] = f"{nucleo.ahora():%Y-%m-%d}"
            _guardar_nota(n)
            hechas.append(n["nombre"])
    return hechas


# ---------- 2. enlazar ----------

def enlazar_parecidas(vecs: dict[str, list[float]]) -> int:
    notas = {n["ruta"]: n for n in conocimiento.todas() if n.get("tipo") != "fuente"}
    rutas = [r for r in notas if r in vecs]
    nuevos = 0
    for r in rutas:
        n = notas[r]
        ya = set(re.findall(r"\[\[([^\]|#]+)", n["cuerpo"]))
        candidatas = sorted(((embeddings.coseno(vecs[r], vecs[o]), o) for o in rutas if o != r), reverse=True)
        anadir = [notas[o]["nombre"] for c, o in candidatas[:MAX_ENLACES_POR_NOTA]
                  if c >= UMBRAL_ENLACE and notas[o]["nombre"] not in ya]
        if not anadir:
            continue
        enlaces = " · ".join(f"[[{a}]]" for a in anadir)
        if "\nRelacionado:" in n["cuerpo"]:
            n["cuerpo"] = re.sub(r"(\nRelacionado: [^\n]*)", lambda m: m.group(1) + " · " + enlaces, n["cuerpo"], count=1)
        elif "\nOrigen:" in n["cuerpo"]:
            n["cuerpo"] = n["cuerpo"].replace("\nOrigen:", f"\nRelacionado: {enlaces}\n\nOrigen:", 1)
        else:
            n["cuerpo"] += f"\n\nRelacionado: {enlaces}\n"
        _guardar_nota(n)
        nuevos += len(anadir)
    return nuevos


# ---------- 3. fusionar repetidas ----------

def _redirigir_enlaces(viejo: str, nuevo: str):
    """Cambia [[viejo]] por [[nuevo]] en todo el vault (conocimiento, lecciones, temas, proyectos)."""
    patron = re.compile(r"\[\[(?:[^\]|]*/)?" + re.escape(viejo) + r"(\|[^\]]*)?\]\]")
    for base in ("memoria", "proyectos"):
        for p in (nucleo.RAIZ / base).rglob("*.md"):
            if "/borrador/" in p.as_posix() or "/final/" in p.as_posix() or "/.repos/" in p.as_posix():
                continue
            t = p.read_text(encoding="utf-8", errors="replace")
            if viejo in t:
                t2 = patron.sub(lambda m: f"[[{nuevo}{m.group(1) or ''}]]", t)
                if t2 != t:
                    p.write_text(t2, encoding="utf-8")


def fusionar(a: dict, b: dict, config, proveedores, proyecto: str) -> str | None:
    mensaje = (f"# NOTA A ({a['tipo']}, {a.get('confianza')})\n# {a.get('titulo')}\n{a['cuerpo']}\n\n"
               f"# NOTA B ({b['tipo']}, {b.get('confianza')})\n# {b.get('titulo')}\n{b['cuerpo']}")
    texto, ia, modelo = prov.pedir_rol("jardinero", config, proveedores, SISTEMA_FUSION, mensaje)
    dataset.registrar(proyecto, "jardinero", "fusionar", ia, modelo, SISTEMA_FUSION, mensaje, texto)
    s = nucleo.parsear(texto)["secciones"]
    contenido = s.get("CONTENIDO", "").strip()
    def nucleo_de(cuerpo):   # el contenido sin metadatos (temas, citas, enlaces, origen)
        return "\n".join(l for l in cuerpo.splitlines()
                         if l.strip() and not re.match(r"^(>|Temas:|Origen:|Relacionado:|Fusionada con:)", l))
    if len(contenido) < 0.6 * max(len(nucleo_de(a["cuerpo"])), len(nucleo_de(b["cuerpo"]))):
        return None    # demasiado corta: probablemente ha perdido datos
    # Se queda la más antigua (o la verificada); la otra desaparece
    queda, se_va = (a, b) if (a.get("confianza") == "verificado" or b.get("confianza") != "verificado") else (b, a)
    citas = "\n".join(dict.fromkeys(re.findall(r"^> .+\n> — `[^`]+`.*$", a["cuerpo"] + "\n" + b["cuerpo"], re.M)))
    temas = sorted({t.lower() for t in a.get("temas", []) + b.get("temas", [])})
    queda["titulo"] = s.get("TITULO", "").strip() or queda.get("titulo")
    for campo in ("temas", "claves", "proyectos", "fuentes"):
        queda[campo] = list(dict.fromkeys(list(a.get(campo, [])) + list(b.get(campo, []))))
    queda["temas"] = temas
    queda["confianza"] = "verificado" if a.get("confianza") == b.get("confianza") == "verificado" else "propuesto"
    queda["actualizado"] = f"{nucleo.ahora():%Y-%m-%d}"
    contra = s.get("CONTRADICCION", "no").strip()
    aviso = "" if contra.lower().startswith("no") else f"\n\n> ⚠️ Posible contradicción al fusionar: {contra}\n"
    if aviso:
        queda["confianza"] = "propuesto"
    origen = re.search(r"\nOrigen: .*", queda["cuerpo"])
    queda["cuerpo"] = (f"Temas: {' · '.join(f'[[{t}]]' for t in temas)}\n\n{contenido}\n" + (f"\n{citas}\n" if citas else "")
                       + aviso + f"\nFusionada con: {se_va.get('titulo')}\n" + (origen.group(0) + "\n" if origen else ""))
    _guardar_nota(queda)
    (nucleo.RAIZ / se_va["ruta"]).unlink()
    _redirigir_enlaces(se_va["nombre"], queda["nombre"])
    return f"[[{queda['nombre']}]] ← {se_va.get('titulo')}"


# ---------- 4. contradicciones ----------

def revisar_contradiccion(a: dict, b: dict, config, proveedores, proyecto: str) -> str | None:
    mensaje = f"# NOTA A\n# {a.get('titulo')}\n{a['cuerpo']}\n\n# NOTA B\n# {b.get('titulo')}\n{b['cuerpo']}"
    texto, ia, modelo = prov.pedir_rol("jardinero", config, proveedores, SISTEMA_CONTRADICCION, mensaje)
    dataset.registrar(proyecto, "jardinero", "contradiccion", ia, modelo, SISTEMA_CONTRADICCION, mensaje, texto)
    s = nucleo.parsear(texto)["secciones"]
    if not s.get("CONTRADICCION", "no").strip().lower().startswith("s"):
        return None
    explicacion = s.get("EXPLICACION", "").strip()[:500]
    for x, y in ((a, b), (b, a)):
        if f"Posible contradicción con [[{y['nombre']}]]" in x["cuerpo"]:
            continue
        x["cuerpo"] += f"\n\n> ⚠️ Posible contradicción con [[{y['nombre']}]]: {explicacion}\n"
        x["confianza"] = "propuesto"
        _guardar_nota(x)
    return f"[[{a['nombre']}]] ↔ [[{b['nombre']}]]: {explicacion}"


# ---------- la pasada completa ----------

def ejecutar(carpeta: Path, cfg: dict, cfg_ruta: Path, bitacora: Path) -> str:
    config, proveedores = prov.cargar(nucleo.RAIZ / "config" / "ias.json")
    roles = config.get("roles", {})
    config = {**config, "roles": {**roles, "jardinero": cfg.get("roles", {}).get("jardinero")
                                  or roles.get("jardinero") or roles.get("revisor", [])}}
    # Las fuentes de las notas pueden estar en los repos (se descargan como en el aprendizaje)
    apr = nucleo.RAIZ / "proyectos" / "aprendizaje"
    if (apr / "proyecto.json").exists():
        try:
            from . import aprender
            aprender.preparar_repos(apr, json.loads((apr / "proyecto.json").read_text(encoding="utf-8")))
        except Exception as e:
            print(f"No pude descargar los repos de las fuentes: {e}")
    apuntes = []

    verificadas = verificar_propuestas(apr)
    apuntes.append(f"- ✅ Citas comprobadas: {len(verificadas)} notas pasan a verificado"
                   + (": " + " · ".join(f"[[{v}]]" for v in verificadas[:20]) if verificadas else ""))

    print(embeddings.actualizar())
    vecs = embeddings.vectores()
    if not vecs:
        apuntes.append("- (sin embeddings: no se puede buscar repetidas ni enlazar por significado)")
    else:
        notas = {n["ruta"]: n for n in conocimiento.todas() if n.get("tipo") != "fuente"}
        vecs_notas = {r: v for r, v in vecs.items() if r in notas}
        pares = embeddings.parecidas(vecs_notas, UMBRAL_CONTRADICCION)
        fusiones, revisadas = [], []
        tocadas: set[str] = set()
        for c, ra, rb in pares:
            if len(fusiones) >= MAX_FUSIONES or prov.tiempo_restante() < MIN_PARA_IA:
                break
            if c < UMBRAL_DUPLICADO or ra in tocadas or rb in tocadas:
                continue
            a, b = _leer_nota(ra), _leer_nota(rb)
            if not a or not b or a.get("tipo") != b.get("tipo"):
                continue
            try:
                r = fusionar(a, b, config, proveedores, carpeta.name)
            except (RuntimeError, prov.TiempoAgotado) as e:
                apuntes.append(f"- fusiones paradas: {e}")
                break
            if r:
                fusiones.append(r)
                tocadas |= {ra, rb}
        for c, ra, rb in pares:
            if len(revisadas) >= MAX_CONTRADICCIONES or prov.tiempo_restante() < MIN_PARA_IA:
                break
            if c >= UMBRAL_DUPLICADO or ra in tocadas or rb in tocadas:
                continue
            a, b = _leer_nota(ra), _leer_nota(rb)
            if not a or not b or not (re.search(r"\d", a["cuerpo"]) and re.search(r"\d", b["cuerpo"])):
                continue     # sin cifras es raro que se contradigan en algo comprobable
            try:
                r = revisar_contradiccion(a, b, config, proveedores, carpeta.name)
            except (RuntimeError, prov.TiempoAgotado) as e:
                apuntes.append(f"- contradicciones paradas: {e}")
                break
            tocadas |= {ra, rb}
            if r:
                revisadas.append(r)
        apuntes.append(f"- 🔀 Notas repetidas fusionadas: {len(fusiones)}" + "".join(f"\n  - {f}" for f in fusiones))
        apuntes.append(f"- ⚠️ Contradicciones encontradas: {len(revisadas)}" + "".join(f"\n  - {r}" for r in revisadas))
        print(embeddings.actualizar())
        enlaces = enlazar_parecidas(embeddings.vectores())
        apuntes.append(f"- 🔗 Enlaces nuevos entre notas parecidas: {enlaces}")

    mapas.generar()
    resumen = "\n".join(apuntes)
    nucleo.anotar(bitacora, "🌱 Pasada del jardinero", resumen)
    return resumen
