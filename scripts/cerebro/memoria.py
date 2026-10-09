"""
Memoria compartida del Cerebro: lecciones aprendidas, guardadas como notas de Obsidian.

  memoria/lecciones/<nombre>.md   una lección por nota (problema → solución → ejemplo)
  memoria/temas/<tema>.md         índice de cada tema; las lecciones enlazan aquí ([[latex]])
  memoria/indice.md               todas las lecciones

Cada lección empieza con una cabecera (frontmatter) así:

  ---
  titulo: "No meter código Lua dentro de \\directlua"
  temas: ["latex", "lua"]
  claves: ["directlua", "unexpected symbol"]
  estado: "confirmada"        (o "propuesta": la escribió una IA y falta que la revise una persona)
  veces: 1                    (cuántas veces ha salido el problema)
  fecha: "2026-10-05"
  ---

Antes de cada paso, el orquestador elige las lecciones que encajan con los "temas" del
proyecto y con el error que está saliendo (las "claves"), y se las pasa a las IAs recortadas:
así no repiten errores ya resueltos y no hace falta mandar la memoria entera.
"""

import json
import re
import unicodedata
from pathlib import Path

from . import nucleo

CARPETA = nucleo.RAIZ / "memoria"
LECCIONES = CARPETA / "lecciones"
TEMAS = CARPETA / "temas"
MAX_CHARS = 5000          # lo máximo que se manda a una IA en cada mensaje
CAMPOS = ("titulo", "temas", "claves", "estado", "veces", "fecha", "proyectos")


# ---------- Leer ----------

def _valor(texto: str):
    texto = texto.strip()
    try:
        return json.loads(texto)
    except json.JSONDecodeError:
        return texto.strip("'\"")


def leer(ruta: Path) -> dict | None:
    """Una lección: sus campos + "cuerpo" + "nombre". None si no tiene cabecera."""
    texto = ruta.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", texto, re.S)
    if not m:
        return None
    datos = {"nombre": ruta.stem, "cuerpo": m.group(2).strip()}
    for linea in m.group(1).splitlines():
        if ":" in linea:
            clave, valor = linea.split(":", 1)
            datos[clave.strip()] = _valor(valor)
    for lista in ("temas", "claves", "proyectos"):
        if isinstance(datos.get(lista), str):
            datos[lista] = [x.strip() for x in datos[lista].split(",") if x.strip()]
        datos.setdefault(lista, [])
    return datos


def todas() -> list[dict]:
    if not LECCIONES.exists():
        return []
    return [l for l in (leer(p) for p in sorted(LECCIONES.glob("*.md"))) if l]


# ---------- Elegir qué lecciones mandar ----------

def _puntos(leccion: dict, temas: set[str], contexto: str) -> float:
    """Más puntos si alguna clave aparece en el error/contexto actual; luego por tema."""
    aciertos = sum(1 for c in leccion["claves"] if c and c.lower() in contexto)
    de_tema = bool(temas & {t.lower() for t in leccion["temas"]})
    general = "general" in leccion["temas"]
    if not (aciertos or de_tema or general):
        return 0
    return (aciertos * 3 + de_tema * 1 + general * 0.5
            + (leccion.get("estado") == "confirmada") * 0.5
            + min(int(leccion.get("veces", 1) or 1), 5) * 0.1)


def seleccionar(temas: list[str], contexto: str, max_chars: int = MAX_CHARS) -> str:
    """Texto con las lecciones más útiles para este proyecto y este momento."""
    temas_set = {t.lower() for t in temas}
    contexto = contexto.lower()
    puntuadas = sorted(((p, l) for l in todas() if (p := _puntos(l, temas_set, contexto)) > 0),
                       key=lambda x: -x[0])
    trozos, usados = [], 0
    for _, l in puntuadas:
        aviso = "" if l.get("estado") == "confirmada" else " (propuesta, sin confirmar)"
        trozo = f"### {l.get('titulo', l['nombre'])}{aviso}\n{_sin_enlaces(l['cuerpo'])}"
        if usados + len(trozo) > max_chars:
            continue
        trozos.append(trozo)
        usados += len(trozo)
    if not trozos:
        return "(no hay lecciones guardadas sobre esto)"
    return "\n\n".join(trozos)


def _sin_enlaces(cuerpo: str) -> str:
    """Quita lo que solo sirve en Obsidian (línea de temas, origen) para ahorrar tokens."""
    lineas = [l for l in cuerpo.splitlines() if not re.match(r"^(Temas|Origen):", l)]
    texto = "\n".join(lineas).strip()
    return re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", r"\1", texto)


# ---------- Escribir ----------

def _nombre(titulo: str) -> str:
    """'No meter Lua en \\directlua' -> 'no-meter-lua-en-directlua'."""
    t = unicodedata.normalize("NFKD", titulo).encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")[:60].strip("-") or "leccion"


def _escribir(ruta: Path, datos: dict):
    cabecera = "\n".join(f"{c}: {json.dumps(datos[c], ensure_ascii=False)}"
                         for c in CAMPOS if c in datos)
    ruta.parent.mkdir(parents=True, exist_ok=True)
    ruta.write_text(f"---\n{cabecera}\n---\n\n{datos['cuerpo'].strip()}\n", encoding="utf-8")


def guardar_propuesta(bloque: str, proyecto: str) -> str | None:
    """Guarda la lección que propone el revisor (bloque <<<LECCION>>>, con líneas
    'titulo:', 'temas:', 'claves:', 'problema:', 'solucion:', 'ejemplo:').
    Si ya existe una con el mismo título, suma una vez. Devuelve el nombre o None."""
    campos, actual = {}, None
    for linea in bloque.splitlines():
        m = re.match(r"^\s*(titulo|título|temas|claves|problema|solucion|solución|ejemplo)\s*:\s*(.*)$",
                     linea, re.I)
        if m:
            actual = unicodedata.normalize("NFKD", m.group(1).lower()).encode("ascii", "ignore").decode()
            campos[actual] = m.group(2)
        elif actual:
            campos[actual] += "\n" + linea
    titulo = campos.get("titulo", "").strip()
    if not titulo or not campos.get("problema", "").strip() or not campos.get("solucion", "").strip():
        return None

    nombre = _nombre(titulo)
    ruta = LECCIONES / f"{nombre}.md"
    existente = leer(ruta) if ruta.exists() else None
    if existente:
        existente["veces"] = int(existente.get("veces", 1) or 1) + 1
        if proyecto not in existente["proyectos"]:
            existente["proyectos"].append(proyecto)
        _escribir(ruta, existente)
        return nombre

    def lista(texto):
        return [x.strip().strip("'\"") for x in texto.replace("\n", ",").split(",") if x.strip()]

    temas = [t.lower() for t in lista(campos.get("temas", ""))] or ["general"]
    claves = lista(campos.get("claves", ""))
    cuerpo = (f"Temas: {' · '.join(f'[[{t}]]' for t in temas)}\n\n"
              f"## Problema\n{campos['problema'].strip()}\n\n"
              f"## Solución\n{campos['solucion'].strip()}\n")
    if campos.get("ejemplo", "").strip():
        cuerpo += f"\n## Ejemplo\n{campos['ejemplo'].strip()}\n"
    cuerpo += f"\nOrigen: [[proyectos/{proyecto}/bitacora|{proyecto}]]"
    _escribir(ruta, {"titulo": titulo, "temas": temas, "claves": claves, "estado": "propuesta",
                     "veces": 1, "fecha": f"{nucleo.ahora():%Y-%m-%d}", "proyectos": [proyecto],
                     "cuerpo": cuerpo})
    reindexar()
    return nombre


def reindexar():
    """Rehace memoria/temas/<tema>.md y memoria/indice.md (para navegar y para el grafo)."""
    lecciones = todas()
    por_tema: dict[str, list[dict]] = {}
    for l in lecciones:
        for t in l["temas"]:
            por_tema.setdefault(t.lower(), []).append(l)

    def linea(l):
        marca = "" if l.get("estado") == "confirmada" else " · ⚠️ propuesta"
        return f"- [[{l['nombre']}|{l.get('titulo', l['nombre'])}]]{marca}"

    TEMAS.mkdir(parents=True, exist_ok=True)
    for tema, ls in por_tema.items():
        (TEMAS / f"{tema}.md").write_text(
            f"# {tema}\n\nLecciones sobre {tema} (este archivo se genera solo).\n\n"
            + "\n".join(linea(l) for l in ls) + "\n", encoding="utf-8")
    pendientes = [l for l in lecciones if l.get("estado") != "confirmada"]
    (CARPETA / "indice.md").write_text(
        "# Memoria del Cerebro\n\n"
        "Lecciones aprendidas por las IAs en todos los proyectos. Antes de cada paso se les pasan "
        "las que encajan con el proyecto y con el error del momento. Este archivo se genera solo.\n\n"
        "Para confirmar una lección propuesta: abrirla, revisarla y cambiar `estado` a `confirmada`.\n\n"
        f"## Temas\n\n{' · '.join(f'[[{t}]]' for t in sorted(por_tema))}\n\n"
        f"## Pendientes de revisar ({len(pendientes)})\n\n"
        + ("\n".join(linea(l) for l in pendientes) or "Ninguna.")
        + f"\n\n## Todas ({len(lecciones)})\n\n" + "\n".join(linea(l) for l in lecciones) + "\n",
        encoding="utf-8")
