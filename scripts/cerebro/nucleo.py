"""
Piezas comunes a cualquier IA: rutas, hora, leer/escribir archivos y la bitácora.

Las IAs responden en un formato de bloques en vez de JSON, porque el código
(LaTeX sobre todo, lleno de barras invertidas) rompe el JSON con facilidad:

<<<RESUMEN>>>
texto
<<<ARCHIVO ruta/del/archivo.tex>>>
contenido completo
<<<FIN>>>

Para cambiar solo un trozo de un archivo que ya existe (sin reescribirlo entero):

<<<CAMBIAR ruta/del/archivo.tex>>>
<<<BUSCAR>>>
texto exacto que hay ahora (una sola vez en el archivo)
<<<POR>>>
texto nuevo
<<<FIN>>>
"""

import fnmatch
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
# Hasta 150.000 caracteres por archivo en los mensajes. Con 20.000 (lo de antes) los capítulos largos
# llegaban recortados a las IAs, que al reescribirlos enteros perdían o se inventaban el resto.
MAX_CHARS_ARCHIVO = 150_000
MARCA_RECORTE = "[... archivo recortado ...]"
# Un archivo que una IA reescribe entero y queda mucho más corto que el actual casi siempre está cortado
ENCOGER_MAX = 0.6        # el nuevo tiene que tener al menos el 60 % de los caracteres del actual
ENCOGER_DESDE = 6000     # ... si el actual tiene más de esto
MAX_CAMBIOS = 40         # bloques BUSCAR/POR por respuesta

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
                texto = texto[:MAX_CHARS_ARCHIVO] + "\n" + MARCA_RECORTE
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
    """Devuelve {"secciones": {NOMBRE: texto}, "archivos": {ruta: contenido}, "borrar": [rutas],
    "cambios": [(ruta, buscar, por)]}."""
    resultado = {"secciones": {}, "archivos": {}, "borrar": [], "cambios": []}
    actual, argumento, buffer = None, None, []
    estado = {"ruta": None, "buscar": None}   # dentro de un bloque CAMBIAR

    def cerrar():
        if actual is None:
            return
        contenido = "\n".join(buffer)
        if actual == "ARCHIVO" and argumento:
            resultado["archivos"][argumento.strip()] = _quitar_vallas(contenido) + "\n"
        elif actual == "BUSCAR" and estado["ruta"]:
            estado["buscar"] = contenido.strip("\n")
        elif actual == "POR" and estado["ruta"] and estado["buscar"]:
            resultado["cambios"].append((estado["ruta"], estado["buscar"], contenido.strip("\n")))
            estado["buscar"] = None
        elif actual not in ("FIN", "BUSCAR", "POR"):
            resultado["secciones"][actual] = contenido.strip()

    for linea in respuesta.splitlines():
        m = CABECERA.match(linea.strip())
        if m:
            cerrar()
            actual, argumento, buffer = m.group(1), m.group(2), []
            if actual == "BORRAR" and argumento:
                resultado["borrar"].append(argumento.strip())
                actual = None
            elif actual == "CAMBIAR":
                estado["ruta"], estado["buscar"] = (argumento or "").strip() or None, None
                actual = None
            elif actual == "FIN":
                estado["ruta"] = None
            elif actual not in ("BUSCAR", "POR"):
                estado["ruta"] = None
        else:
            buffer.append(linea)
    cerrar()
    return resultado


# ---------- Escribir en el proyecto ----------

NOMBRE_VALIDO = re.compile(r"^[\w][\w.\-]*$")  # letras/números al inicio; sin espacios


def ruta_segura(base: Path, relativa: str, estricta: bool = True) -> Path:
    """Impide que una IA escriba fuera de su carpeta (../../loquesea) o invente nombres raros
    (p. ej. «- borrado de archivos temporales»): cada parte de la ruta debe ser un nombre
    normal y el archivo tener extensión."""
    partes = relativa.strip().replace("\\", "/").split("/")
    if estricta and (not all(NOMBRE_VALIDO.match(x) for x in partes) or "." not in partes[-1]):
        raise ValueError(f"Nombre de archivo no válido: {relativa!r}")
    destino = (base / relativa.strip()).resolve()
    if base.resolve() not in destino.parents:
        raise ValueError(f"Ruta fuera de la carpeta permitida: {relativa}")
    return destino


def protegido(relativa: str, protegidos: list[str]) -> bool:
    """True si la ruta coincide con algún patrón de "protegidos" (p. ej. "figs/*")."""
    r = relativa.strip().replace("\\", "/").lstrip("./")
    return any(fnmatch.fnmatch(r, patron) for patron in protegidos)


def aplicar(base: Path, archivos: dict[str, str], borrar: list[str], maximo: int,
            protegidos: list[str] = ()) -> list[str]:
    """Escribe y borra los archivos que pide una IA. Los "protegidos" del proyecto no se tocan:
    se apunta en la lista de cambios para que salga en la bitácora."""
    cambiados = []
    for relativa, contenido in list(archivos.items())[:maximo]:
        if protegido(relativa, protegidos):
            print(f"  Ignorado (protegido): {relativa}")
            cambiados.append(f"(protegido, no se escribió) {relativa}")
            continue
        try:
            destino = ruta_segura(base, relativa)
        except ValueError as e:
            print(f"  Ignorado: {e}")
            continue
        if MARCA_RECORTE in contenido:
            cambiados.append(f"(rechazado: copia el aviso de archivo recortado; usa CAMBIAR) {relativa}")
            continue
        if destino.is_file():
            antes = len(destino.read_text(encoding="utf-8", errors="replace"))
            if antes > ENCOGER_DESDE and len(contenido) < ENCOGER_MAX * antes:
                print(f"  Rechazado (encoge de {antes} a {len(contenido)} caracteres): {relativa}")
                cambiados.append(f"(rechazado: el archivo nuevo es mucho más corto que el actual, "
                                 f"{len(contenido)} de {antes} caracteres; para cambiar un trozo usa CAMBIAR) {relativa}")
                continue
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text(contenido, encoding="utf-8")
        cambiados.append(relativa)
    for relativa in borrar:
        if protegido(relativa, protegidos):
            cambiados.append(f"(protegido, no se borró) {relativa}")
            continue
        try:
            destino = ruta_segura(base, relativa, estricta=False)
        except ValueError as e:
            print(f"  Ignorado: {e}")
            continue
        if destino.is_file():
            destino.unlink()
            cambiados.append(f"(borrado) {relativa}")
    return cambiados


def aplicar_cambios(base: Path, cambios: list[tuple[str, str, str]], protegidos: list[str] = ()) -> list[str]:
    """Aplica bloques CAMBIAR (buscar → por). El texto buscado tiene que estar exactamente una vez;
    si no, ese cambio no se aplica y se apunta para que la IA lo sepa."""
    resultado = []
    for ruta, buscar, por in cambios[:MAX_CAMBIOS]:
        if protegido(ruta, protegidos):
            resultado.append(f"(protegido, no se cambió) {ruta}")
            continue
        try:
            destino = ruta_segura(base, ruta, estricta=False)
        except ValueError as e:
            resultado.append(f"(no aplicado: {e}) {ruta}")
            continue
        if not destino.is_file():
            resultado.append(f"(no aplicado: no existe el archivo) {ruta}")
            continue
        texto = destino.read_text(encoding="utf-8", errors="replace")
        veces = texto.count(buscar)
        if veces == 0:
            # Segunda oportunidad: sin los espacios del final de cada línea
            limpio = lambda s: "\n".join(l.rstrip() for l in s.split("\n"))
            if limpio(texto).count(limpio(buscar)) == 1:
                texto, buscar, veces = limpio(texto), limpio(buscar), 1
        if veces != 1:
            motivo = "no encuentro el texto" if veces == 0 else f"el texto aparece {veces} veces"
            resultado.append(f"(no aplicado: {motivo}: «{buscar.strip()[:60]}») {ruta}")
            continue
        destino.write_text(texto.replace(buscar, por, 1), encoding="utf-8")
        resultado.append(f"(cambio) {ruta}")
    return resultado


def foto(base: Path) -> dict[str, bytes]:
    """Copia en memoria de los archivos de texto de una carpeta, para poder deshacer un paso."""
    if not base.exists():
        return {}
    return {p.relative_to(base).as_posix(): p.read_bytes() for p in base.rglob("*")
            if p.is_file() and p.suffix.lower() in EXTENSIONES_TEXTO}


def restaurar(base: Path, copia: dict[str, bytes]) -> list[str]:
    """Deja los archivos de texto como en la copia: los cambiados vuelven atrás y los nuevos se borran."""
    tocados = []
    for relativa, contenido in foto(base).items():
        if relativa not in copia:
            (base / relativa).unlink()
            tocados.append(relativa)
        elif contenido != copia[relativa]:
            (base / relativa).write_bytes(copia[relativa])
            tocados.append(relativa)
    for relativa, contenido in copia.items():
        if not (base / relativa).exists():
            (base / relativa).parent.mkdir(parents=True, exist_ok=True)
            (base / relativa).write_bytes(contenido)
            tocados.append(relativa)
    return tocados


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
