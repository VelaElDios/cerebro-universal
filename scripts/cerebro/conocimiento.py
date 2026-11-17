"""
Conocimiento del Cerebro: lo que las IAs saben de los proyectos y de los temarios, guardado como
notas de Obsidian para que CUALQUIER IA (la que esté conectada hoy u otra local mañana) lo use
igual y no tenga que volver a deducirlo ni inventarlo.

  memoria/conocimiento/conceptos/   qué es algo (un término, una pieza de la arquitectura, un tema del temario)
  memoria/conocimiento/recetas/     cómo se hace algo en nuestros proyectos (pasos y código que funcionó)
  memoria/conocimiento/decisiones/  qué se eligió y por qué (para hacerlo igual la próxima vez)
  memoria/conocimiento/datos/       hechos concretos de un proyecto (cifras, fechas, nombres)
  memoria/conocimiento/fuentes/     una nota por documento aprendido (temario, documentación), con enlaces
                                    a todo lo que se sacó de él

Cada nota lleva una cabecera para que una máquina la pueda filtrar:

  ---
  tipo: "receta"
  titulo: "Agrupar capturas con subfigure"
  temas: ["latex", "figuras"]
  claves: ["subfigure", "subcaption"]
  proyectos: ["memoria-procesos"]
  fuentes: ["memoria/reglas-tfg.md"]
  confianza: "verificado"     (la cita aparece literal en la fuente) o "propuesto"
  fecha: "2026-11-16"
  actualizado: "2026-11-16"
  ---

Las IAs escriben notas con el bloque <<<CONOCIMIENTO>>> (ver FORMATO). Antes de cada paso se les pasan
las que encajan con el proyecto y con lo que están haciendo (seleccionar).
"""

import json
import re
import unicodedata
from pathlib import Path

from . import nucleo
from .memoria import leer

TIPOS = {"concepto": "conceptos", "receta": "recetas", "decision": "decisiones", "dato": "datos",
         "fuente": "fuentes"}
CAMPOS = ("tipo", "titulo", "temas", "claves", "proyectos", "fuentes", "confianza", "fecha", "actualizado")
MAX_CHARS = 7000          # conocimiento que se manda a una IA en cada mensaje
MAX_CONTENIDO = 4000      # lo más largo que puede ser el contenido de una nota nueva
MAX_NOTAS_POR_BLOQUE = 10

FORMATO = """<<<CONOCIMIENTO>>>
(OPCIONAL, pero muy valioso: es la memoria que heredan las demás IAs. Hasta 10 notas, separadas por una
línea con ---. Solo conocimiento ÚTIL PARA OTRA VEZ y que no esté ya en el CONOCIMIENTO DEL CEREBRO.)
tipo: concepto | receta | decision | dato
titulo: frase corta y concreta (p. ej. «Cómo se agrupan capturas con subfigure»)
temas: temas separados por comas (latex, saas, scrum...)
claves: palabras exactas con las que se buscaría (nombres de comandos, módulos, errores)
fuente: archivo de donde sale (p. ej. repo:saas/docs/documentacion-tecnica.md o chapters/04-descripcion.tex)
cita: frase LITERAL de esa fuente que lo demuestra (copiada tal cual; sin ella la nota queda «propuesta»)
relacionado: títulos de otras notas del cerebro con las que se enlaza, separados por comas
contenido:
la explicación, los pasos o el código, claros y completos para que otra IA lo pueda usar sin preguntar
---
tipo: ..."""


# ---------- Rutas (se calculan al usarlas: las pruebas cambian nucleo.RAIZ) ----------

def carpeta() -> Path:
    return nucleo.RAIZ / "memoria" / "conocimiento"


def nombre_de(titulo: str) -> str:
    t = unicodedata.normalize("NFKD", titulo).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60].strip("-") or "nota"


def normalizar(texto: str) -> str:
    """Para comparar citas: minúsculas, sin acentos raros, sin marcas de Markdown/LaTeX y espacios simples."""
    t = unicodedata.normalize("NFKC", texto).lower()
    t = re.sub(r"[`*_«»\"'“”‘’\\{}]", "", t)
    return re.sub(r"\s+", " ", t).strip()


# ---------- Leer ----------

def todas() -> list[dict]:
    base = carpeta()
    if not base.exists():
        return []
    notas = []
    for p in sorted(base.rglob("*.md")):
        n = leer(p)
        if n and n.get("tipo"):
            n["ruta"] = p.relative_to(nucleo.RAIZ).as_posix()
            for lista in ("fuentes",):
                if isinstance(n.get(lista), str):
                    n[lista] = [n[lista]]
                n.setdefault(lista, [])
            notas.append(n)
    return notas


def por_titulo() -> dict[str, dict]:
    return {nombre_de(n.get("titulo", n["nombre"])): n for n in todas()}


# ---------- Elegir qué conocimiento mandar ----------

def _palabras(texto: str) -> set[str]:
    return {w for w in re.findall(r"[a-záéíóúñü0-9_\-\\]{5,}", texto.lower())}


def _puntos(n: dict, temas: set[str], contexto: str, palabras_ctx: set[str], proyecto: str) -> float:
    # Palabra entera: si no, una clave corta como «POR» casaría con «portada»
    claves = sum(1 for c in n.get("claves", []) if c and len(c) >= 3
                 and re.search(r"(?<![\w])" + re.escape(c.lower()) + r"(?![\w])", contexto))
    titulo = len(_palabras(n.get("titulo", "")) & palabras_ctx)
    de_tema = len(temas & {t.lower() for t in n.get("temas", [])})
    mismo = proyecto in n.get("proyectos", [])
    if not (claves or titulo or de_tema or mismo):
        return 0
    return (claves * 3 + titulo * 1 + de_tema * 1 + mismo * 1.5
            + (n.get("confianza") == "verificado") * 0.5
            + (n.get("tipo") in ("receta", "decision")) * 0.3)


def _cuerpo_limpio(cuerpo: str) -> str:
    lineas = [l for l in cuerpo.splitlines() if not re.match(r"^(Temas|Origen|Relacionado):", l)]
    texto = "\n".join(lineas).strip()
    return re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", r"\1", texto)


_usadas: list[str] = []   # rutas de las notas mandadas en el último mensaje (para cerebro/uso.py)


def ultimas_usadas() -> list[str]:
    return list(_usadas)


def seleccionar(temas: list[str], contexto: str, proyecto: str = "", max_chars: int = MAX_CHARS,
                semantica: bool = True) -> str:
    """Las notas más útiles para este proyecto y este momento, listas para meter en un mensaje.

    Mezcla tres señales: palabras clave y temas (siempre), parecido de significado con lo que se está
    haciendo (embeddings, si hay API) y cómo les ha ido a esas notas en pasos anteriores (uso.json)."""
    from . import embeddings, uso
    temas_set = {t.lower() for t in temas}
    ctx = contexto.lower()
    palabras_ctx = _palabras(ctx)
    vecs = embeddings.vectores() if semantica else {}
    q = embeddings.consulta(contexto) if vecs else None
    estad = uso.cargar()
    puntuadas = []
    for n in todas():
        if n.get("tipo") == "fuente":
            continue
        p = _puntos(n, temas_set, ctx, palabras_ctx, proyecto)
        if q is not None and n["ruta"] in vecs:
            c = embeddings.coseno(q, vecs[n["ruta"]])
            p += max(0.0, c - 0.55) * 20          # coseno 0,75 → +4 puntos
        if p <= 0:
            continue
        puntuadas.append((p + uso.bonificacion(estad, n["ruta"]), n))
    puntuadas.sort(key=lambda x: -x[0])
    trozos, usados = [], 0
    _usadas.clear()
    for _, n in puntuadas:
        marca = "verificado" if n.get("confianza") == "verificado" else "propuesto, compruébalo"
        de = ", ".join(n.get("proyectos", [])) or "general"
        trozo = (f"### [{n['tipo']}] {n.get('titulo', n['nombre'])} ({marca} · {de})\n"
                 f"{_cuerpo_limpio(n['cuerpo'])}")
        if len(trozo) > 2500:
            trozo = trozo[:2500] + f"\n[... sigue en {n['ruta']} ...]"
        if usados + len(trozo) > max_chars:
            continue
        trozos.append(trozo)
        _usadas.append(n["ruta"])
        usados += len(trozo)
    if not trozos:
        return "(todavía no hay conocimiento guardado sobre esto: lo que aprendas, guárdalo en CONOCIMIENTO)"
    return "\n\n".join(trozos)


def mapa_textual(max_titulos: int = 8, max_chars: int = 4000) -> str:
    """Índice corto de todo lo que sabe el cerebro, por temas, para que la IA sepa qué existe."""
    por_tema: dict[str, list[str]] = {}
    for n in todas():
        for t in n.get("temas", []) or ["general"]:
            por_tema.setdefault(t.lower(), []).append(n.get("titulo", n["nombre"]))
    if not por_tema:
        return "(el mapa está vacío)"
    lineas = []
    for tema, titulos in sorted(por_tema.items(), key=lambda x: -len(x[1])):
        extra = f" (+{len(titulos) - max_titulos} más)" if len(titulos) > max_titulos else ""
        lineas.append(f"- {tema} ({len(titulos)}): " + " · ".join(titulos[:max_titulos]) + extra)
    texto = ""
    for i, l in enumerate(lineas):
        if len(texto) + len(l) > max_chars:
            return texto + f"- (+{len(lineas) - i} temas más en memoria/indice.md)"
        texto += l + "\n"
    return texto.rstrip()


# ---------- Escribir ----------

def _escribir(ruta: Path, datos: dict):
    cabecera = "\n".join(f"{c}: {json.dumps(datos[c], ensure_ascii=False)}" for c in CAMPOS if c in datos)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(f"---\n{cabecera}\n---\n\n{datos['cuerpo'].strip()}\n", encoding="utf-8")


def _lista(texto: str) -> list[str]:
    return [x.strip().strip("'\"[]") for x in re.split(r"[,\n]", texto) if x.strip().strip("'\"[]")]


def _entradas(bloque: str) -> list[dict]:
    """Parte el bloque CONOCIMIENTO en notas (separadas por --- o por un nuevo «tipo:»)."""
    notas, actual, campo = [], {}, None
    patron = re.compile(r"^\s*(tipo|titulo|título|temas|claves|fuente|cita|relacionado|contenido)\s*:\s*(.*)$", re.I)
    for linea in bloque.splitlines():
        if linea.strip().startswith("<<<"):
            continue
        m = patron.match(linea) if campo != "contenido" or re.match(r"^\s*tipo\s*:", linea, re.I) else None
        if linea.strip() == "---" or (m and m.group(1).lower() == "tipo" and actual.get("tipo")):
            if actual:
                notas.append(actual)
            actual, campo = {}, None
            if linea.strip() == "---":
                continue
        if m:
            campo = unicodedata.normalize("NFKD", m.group(1).lower()).encode("ascii", "ignore").decode()
            actual[campo] = m.group(2)
        elif campo:
            actual[campo] = actual.get(campo, "") + "\n" + linea
    if actual:
        notas.append(actual)
    return notas[:MAX_NOTAS_POR_BLOQUE]


def guardar(bloque: str, proyecto: str, verificacion: str = "", fuente_por_defecto: str = "",
            temas_extra: list[str] | None = None) -> list[str]:
    """Guarda las notas de un bloque <<<CONOCIMIENTO>>>. `verificacion` es el texto contra el que se
    comprueban las citas (fuentes y archivos del borrador). Devuelve los nombres guardados."""
    guardadas = []
    existentes = por_titulo()
    texto_norm = normalizar(verificacion) if verificacion else ""
    hoy = f"{nucleo.ahora():%Y-%m-%d}"
    for e in _entradas(bloque):
        tipo = unicodedata.normalize("NFKD", e.get("tipo", "").strip().lower()).encode("ascii", "ignore").decode()
        titulo = e.get("titulo", "").strip().strip("«»\"")
        contenido = e.get("contenido", "").strip()
        if tipo not in TIPOS or tipo == "fuente" or not titulo or len(contenido) < 20:
            continue
        contenido = contenido[:MAX_CONTENIDO]
        cita = e.get("cita", "").strip().strip("«»\"").strip()
        verificada = bool(cita) and len(normalizar(cita)) >= 12 and normalizar(cita) in texto_norm
        fuente = e.get("fuente", "").strip() or fuente_por_defecto
        temas = sorted({t.lower() for t in _lista(e.get("temas", "")) + (temas_extra or [])}) or ["general"]
        claves = _lista(e.get("claves", ""))
        relacionados = [r for r in _lista(e.get("relacionado", "")) if nombre_de(r) in existentes]
        nombre = nombre_de(titulo)

        if nombre in existentes:
            n = existentes[nombre]
            ruta = nucleo.RAIZ / n["ruta"]
            cambiado = False
            if proyecto and proyecto not in n["proyectos"]:
                n["proyectos"].append(proyecto)
                cambiado = True
            for t in temas:
                if t not in [x.lower() for x in n["temas"]]:
                    n["temas"].append(t)
                    cambiado = True
            if fuente and fuente not in n["fuentes"]:
                n["fuentes"].append(fuente)
                cambiado = True
            if verificada and n.get("confianza") != "verificado":
                n["confianza"] = "verificado"
                cambiado = True
            # Lo nuevo solo se añade si aporta algo que no estaba
            if normalizar(contenido)[:200] not in normalizar(n["cuerpo"]):
                n["cuerpo"] = (n["cuerpo"].replace("\nOrigen:", f"\n## Ampliación ({hoy}, {proyecto})\n{contenido}\n\nOrigen:", 1)
                               if "\nOrigen:" in n["cuerpo"] else n["cuerpo"] + f"\n\n## Ampliación ({hoy}, {proyecto})\n{contenido}")
                cambiado = True
            if cambiado:
                n["actualizado"] = hoy
                _escribir(ruta, n)
                guardadas.append(nombre)
            continue

        cuerpo = f"Temas: {' · '.join(f'[[{t}]]' for t in temas)}\n\n{contenido}\n"
        if cita:
            cuerpo += f"\n> {cita}\n> — `{fuente or 'sin fuente'}`" + ("" if verificada else " (cita sin comprobar)") + "\n"
        if relacionados:
            cuerpo += "\nRelacionado: " + " · ".join(f"[[{existentes[nombre_de(r)]['nombre']}]]" for r in relacionados) + "\n"
        if proyecto:
            cuerpo += f"\nOrigen: [[proyectos/{proyecto}/estado|{proyecto}]]\n"
        datos = {"tipo": tipo, "titulo": titulo, "temas": temas, "claves": claves,
                 "proyectos": [proyecto] if proyecto else [], "fuentes": [fuente] if fuente else [],
                 "confianza": "verificado" if verificada else "propuesto", "fecha": hoy, "actualizado": hoy,
                 "cuerpo": cuerpo}
        ruta = carpeta() / TIPOS[tipo] / f"{nombre}.md"
        _escribir(ruta, datos)
        existentes[nombre] = {**datos, "nombre": nombre, "ruta": ruta.relative_to(nucleo.RAIZ).as_posix()}
        guardadas.append(nombre)
    return guardadas


def guardar_fuente(titulo: str, etiqueta: str, temas: list[str], notas: list[str], proyecto: str = "",
                   resumen: str = "") -> str:
    """Nota-índice de un documento aprendido: enlaza todo lo que se sacó de él (un nodo grande del mapa)."""
    nombre = "fuente-" + nombre_de(titulo)
    hoy = f"{nucleo.ahora():%Y-%m-%d}"
    cuerpo = (f"Temas: {' · '.join(f'[[{t}]]' for t in temas) or '[[general]]'}\n\n"
              f"Documento aprendido: `{etiqueta}`.\n\n" + (f"## Resumen\n{resumen.strip()}\n\n" if resumen else "")
              + f"## Lo que se sacó de él ({len(notas)})\n" + "\n".join(f"- [[{n}]]" for n in sorted(set(notas))) + "\n")
    if proyecto:
        cuerpo += f"\nOrigen: [[proyectos/{proyecto}/estado|{proyecto}]]\n"
    _escribir(carpeta() / TIPOS["fuente"] / f"{nombre}.md",
              {"tipo": "fuente", "titulo": titulo, "temas": temas, "claves": [], "proyectos": [proyecto] if proyecto else [],
               "fuentes": [etiqueta], "confianza": "verificado", "fecha": hoy, "actualizado": hoy, "cuerpo": cuerpo})
    return nombre


# ---------- Ficha de estado de un proyecto (el «traspaso» entre IAs) ----------

def guardar_estado(carpeta_proyecto: Path, texto: str, temas: list[str]):
    """La ficha corta del proyecto que reescribe el revisor en cada paso: qué es, decisiones, convenciones,
    estado y siguiente. La siguiente IA la lee antes que nada."""
    texto = texto.strip()
    if len(texto) < 80:
        return False
    nombre = carpeta_proyecto.name
    hoy = f"{nucleo.ahora():%Y-%m-%d %H:%M}"
    cab = {"tipo": "proyecto", "titulo": nombre, "temas": temas, "actualizado": hoy}
    cabecera = "\n".join(f"{c}: {json.dumps(v, ensure_ascii=False)}" for c, v in cab.items())
    enlaces = " · ".join(f"[[{t}]]" for t in temas)
    (carpeta_proyecto / "estado.md").write_text(
        f"---\n{cabecera}\n---\n\n# {nombre}\n\nTemas: {enlaces}\n\n{texto[:6000]}\n\n"
        f"Bitácora completa: [[proyectos/{nombre}/bitacora|bitácora]] · Spec: [[proyectos/{nombre}/spec|spec]]\n",
        encoding="utf-8")
    return True


def leer_estado(carpeta_proyecto: Path) -> str:
    ruta = carpeta_proyecto / "estado.md"
    if not ruta.exists():
        return "(todavía no hay ficha: escríbela tú en el bloque ESTADO)"
    texto = ruta.read_text(encoding="utf-8")
    texto = re.sub(r"^---\n.*?\n---\n", "", texto, flags=re.S)
    return re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", r"\1", texto).strip()
