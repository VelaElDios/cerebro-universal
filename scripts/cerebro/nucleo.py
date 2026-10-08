"""
Piezas comunes a cualquier IA: rutas, hora, leer/escribir archivos y la bitácora.

Las IAs responden en un formato de bloques en vez de JSON, porque el código
(LaTeX sobre todo, lleno de barras invertidas) rompe el JSON con facilidad:

<<<RESUMEN>>>
texto
<<<ARCHIVO ruta/del/archivo.tex>>>
contenido completo
<<<FIN>>>
"""

import re
import shutil
from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

RAIZ = Path(__file__).resolve().parents[2]
ZONA = ZoneInfo("Europe/Madrid")

EXTENSIONES_TEXTO = {".tex", ".bib", ".lua", ".csv", ".md", ".txt", ".sty", ".cls", ".py", ".json", ".js", ".html", ".css"}
IGNORAR_COPIA = ("*.aux", "*.log", "*.fls", "*.fdb_latexmk", "*.out", "*.toc", "*.bbl",
                 "*.blg", "*.bcf", "*.run.xml", "*.synctex.gz", "*.lof", "*.lot",
                 # Beamer y restos de Biber cuando falla (*.bbl-SAVE-ERROR, *.bcf-SAVE-ERROR)
                 "*.nav", "*.snm", "*.vrb", "*-SAVE-ERROR")
MAX_CHARS_ARCHIVO = 20000

CABECERA = re.compile(r"^<<<([A-ZÁÉÍÓÚ_]+)(?:\s+(.+?))?>>>\s*$")


def ahora() -> datetime:
    return datetime.now(ZONA)


# ---------- Leer el proyecto para pasárselo a una IA ----------

def leer_carpeta(carpeta: Path) -> dict[str, str]:
    """Archivos de texto de una carpeta: {ruta relativa: contenido}."""
    archivos = {}
    if not carpeta.exists():
        return archivos
    for p in sorted(carpeta.rglob("*")):
        if p.is_file() and p.suffix.lower() in EXTENSIONES_TEXTO:
            texto = p.read_text(encoding="utf-8", errors="replace")
            if len(texto) > MAX_CHARS_ARCHIVO:
                texto = texto[:MAX_CHARS_ARCHIVO] + "\n[... archivo recortado ...]"
            archivos[p.relative_to(carpeta).as_posix()] = texto
    return archivos


def volcar(archivos: dict[str, str]) -> str:
    if not archivos:
        return "(carpeta vacía: todavía no hay archivos)"
    return "\n\n".join(f"<<<ARCHIVO {ruta}>>>\n{texto}\n<<<FIN>>>" for ruta, texto in archivos.items())


# ---------- Entender la respuesta de una IA ----------

def _quitar_vallas(texto: str) -> str:
    """Quita ```lenguaje ... ``` si la IA envolvió el contenido."""
    lineas = texto.strip("\n").splitlines()
    if lineas and lineas[0].strip().startswith("```"):
        lineas = lineas[1:]
    if lineas and lineas[-1].strip() == "```":
        lineas = lineas[:-1]
    return "\n".join(lineas)


def parsear(respuesta: str) -> dict:
    """Devuelve {"secciones": {NOMBRE: texto}, "archivos": {ruta: contenido}, "borrar": [rutas]}."""
    resultado = {"secciones": {}, "archivos": {}, "borrar": []}
    actual, argumento, buffer = None, None, []

    def cerrar():
        if actual is None:
            return
        contenido = "\n".join(buffer)
        if actual == "ARCHIVO" and argumento:
            resultado["archivos"][argumento.strip()] = _quitar_vallas(contenido) + "\n"
        elif actual != "FIN":
            resultado["secciones"][actual] = contenido.strip()

    for linea in respuesta.splitlines():
        m = CABECERA.match(linea.strip())
        if m:
            cerrar()
            actual, argumento, buffer = m.group(1), m.group(2), []
            if actual == "BORRAR" and argumento:
                resultado["borrar"].append(argumento.strip())
                actual = None
        else:
            buffer.append(linea)
    cerrar()
    return resultado


# ---------- Escribir en el proyecto ----------

def ruta_segura(base: Path, relativa: str) -> Path:
    """Impide que una IA escriba fuera de su carpeta (../../loquesea)."""
    destino = (base / relativa).resolve()
    if base.resolve() not in destino.parents:
        raise ValueError(f"Ruta fuera de la carpeta permitida: {relativa}")
    return destino


def aplicar(base: Path, archivos: dict[str, str], borrar: list[str], maximo: int) -> list[str]:
    cambiados = []
    for relativa, contenido in list(archivos.items())[:maximo]:
        try:
            destino = ruta_segura(base, relativa)
        except ValueError as e:
            print(f"  Ignorado: {e}")
            continue
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(contenido, encoding="utf-8")
        cambiados.append(relativa)
    for relativa in borrar:
        try:
            destino = ruta_segura(base, relativa)
        except ValueError as e:
            print(f"  Ignorado: {e}")
            continue
        if destino.is_file():
            destino.unlink()
            cambiados.append(f"(borrado) {relativa}")
    return cambiados


def promocionar(origen: Path, destino: Path):
    """Copia el borrador a final/, sin los archivos temporales de compilación."""
    if destino.exists():
        shutil.rmtree(destino)
    shutil.copytree(origen, destino, ignore=shutil.ignore_patterns(*IGNORAR_COPIA))


# ---------- Bitácora: la conversación entre IAs, legible en Obsidian ----------

def anotar(bitacora: Path, titulo: str, cuerpo: str):
    if not bitacora.exists():
        bitacora.write_text("# Bitácora del proyecto\n\nRegistro de lo que hace cada IA, paso a paso.\n", encoding="utf-8")
    with bitacora.open("a", encoding="utf-8") as f:
        f.write(f"\n## {ahora():%Y-%m-%d %H:%M} · {titulo}\n\n{cuerpo.strip()}\n")


def bitacora_reciente(bitacora: Path, chars: int = 8000) -> str:
    if not bitacora.exists():
        return "(sin entradas: es el primer paso del proyecto)"
    texto = bitacora.read_text(encoding="utf-8")
    return texto[-chars:] if len(texto) > chars else texto
