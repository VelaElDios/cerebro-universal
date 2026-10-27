"""
Fuentes de un proyecto, incluidos repositorios públicos de GitHub.

En proyecto.json:

  "repos":   {"saas": "https://github.com/usuario/repo"}        (o {"url": "...", "rama": "main"})
  "fuentes": ["fuentes/normas.md",                 archivo de la carpeta del proyecto
              "repo:saas/README.md",               archivo de un repo
              "repo:saas/docs/**/*.md",            patrones con * y **
              "repo:saas/@arbol"]                  lista de archivos del repo (su estructura)
  "copiar":  [{"desde": "repo:saas/docs/capturas/**/*.png", "a": "figs/capturas"}]

En cada paso los repos se descargan de nuevo (git clone --depth 1) en <proyecto>/.repos/<nombre>,
que git ignora: así las IAs leen siempre la última versión. Lo de "copiar" (imágenes, datos...)
se copia a borrador/ conservando las subcarpetas, y las IAs reciben la lista de imágenes con la
descripción que tengan en los Markdown del repo (el texto alternativo de ![...](...)).

Los tests de un proyecto pueden usar texto_fuentes() para comprobar datos contra lo mismo que
leyeron las IAs.
"""

import re
import shutil
import subprocess
from pathlib import Path

CARPETA_REPOS = ".repos"
MAX_CHARS_FUENTE = 120_000     # una fuente más larga se recorta (con aviso)
MAX_LINEAS_ARBOL = 400
EXTENSIONES_TEXTO = {".md", ".txt", ".csv", ".json", ".yml", ".yaml", ".tex", ".bib", ".py", ".js", ".ts",
                     ".html", ".css", ".sql", ".lua", ".mmd", ".toml", ".ini", ".env.example"}
IGNORAR_ARBOL = {".git", "node_modules", "dist", "build", "__pycache__", ".venv", "venv", ".next", "coverage"}
IMAGEN_MD = re.compile(r"!\[([^\]]*)\]\(\s*<?([^)\s>]+)>?(?:\s+\"[^\"]*\")?\s*\)")
IMAGEN_HTML = re.compile(r"<img\b[^>]*?\bsrc=[\"']([^\"']+)[\"'][^>]*?\balt=[\"']([^\"']*)[\"']", re.I)


class RepoNoDisponible(Exception):
    """No se ha podido descargar un repo: el paso no se da (sin él, las IAs inventarían)."""


# ---------- Descargar ----------

def _datos_repo(dato) -> tuple[str, str | None]:
    if isinstance(dato, str):
        return dato, None
    return dato["url"], dato.get("rama")


def preparar(carpeta: Path, cfg: dict) -> list[str]:
    """Descarga (de nuevo) cada repo de "repos". Devuelve una línea por repo con su commit."""
    info = []
    for nombre, dato in cfg.get("repos", {}).items():
        url, rama = _datos_repo(dato)
        destino = carpeta / CARPETA_REPOS / nombre
        if destino.exists():
            shutil.rmtree(destino)
        destino.parent.mkdir(parents=True, exist_ok=True)
        orden = ["git", "clone", "--depth", "1", "--quiet"] + (["--branch", rama] if rama else []) + [url, str(destino)]
        try:
            r = subprocess.run(orden, capture_output=True, text=True, timeout=180)
        except subprocess.TimeoutExpired:
            raise RepoNoDisponible(f"El repo {nombre} ({url}) tardó más de 3 min en descargarse")
        if r.returncode != 0:
            raise RepoNoDisponible(f"No se pudo descargar el repo {nombre} ({url}): {r.stderr.strip()[:200]}")
        commit = subprocess.run(["git", "-C", str(destino), "log", "-1", "--format=%h %ci"],
                                capture_output=True, text=True).stdout.strip()
        info.append(f"{nombre} @ {commit}")
    return info


def repos_listos(carpeta: Path, cfg: dict) -> bool:
    return all((carpeta / CARPETA_REPOS / n).is_dir() for n in cfg.get("repos", {}))


# ---------- Resolver rutas ----------

def _partir(carpeta: Path, entrada: str) -> tuple[Path, str, str]:
    """'repo:saas/docs/*.md' → (carpeta del repo, 'docs/*.md', 'repo:saas/'); 'fuentes/x.md' → (carpeta, ...)."""
    if entrada.startswith("repo:"):
        nombre, _, patron = entrada[5:].partition("/")
        return carpeta / CARPETA_REPOS / nombre, patron, f"repo:{nombre}/"
    return carpeta, entrada, ""


def resolver(carpeta: Path, entrada: str) -> list[tuple[str, Path]]:
    """[(etiqueta, ruta)] de los archivos que cumplen la entrada (puede tener * y **)."""
    base, patron, prefijo = _partir(carpeta, entrada)
    if not any(c in patron for c in "*?["):
        ruta = base / patron
        return [(prefijo + patron, ruta)] if ruta.is_file() else []
    rutas = sorted(p for p in base.glob(patron) if p.is_file() and ".git" not in p.relative_to(base).parts)
    return [(prefijo + p.relative_to(base).as_posix(), p) for p in rutas]


def arbol(base: Path) -> str:
    """Lista de archivos del repo (sin node_modules, .git...), para que las IAs vean su estructura."""
    lineas = []
    for p in sorted(base.rglob("*")):
        partes = p.relative_to(base).parts
        if any(x in IGNORAR_ARBOL for x in partes) or not p.is_file():
            continue
        lineas.append(p.relative_to(base).as_posix())
    if len(lineas) > MAX_LINEAS_ARBOL:
        lineas = lineas[:MAX_LINEAS_ARBOL] + [f"[... {len(lineas) - MAX_LINEAS_ARBOL} archivos más ...]"]
    return "\n".join(lineas)


# ---------- Leer las fuentes ----------

def fuentes(carpeta: Path, cfg: dict) -> list[tuple[str, str]]:
    """[(etiqueta, texto)] de todas las fuentes, en el orden de proyecto.json."""
    res = []
    for entrada in cfg.get("fuentes", []):
        base, patron, prefijo = _partir(carpeta, entrada)
        if patron == "@arbol":
            res.append((entrada, arbol(base) if base.is_dir() else "(el repo no está descargado)"))
            continue
        encontrados = resolver(carpeta, entrada)
        if not encontrados:
            res.append((entrada, "(falta esta fuente: no hay ningún archivo que coincida)"))
        for etiqueta, ruta in encontrados:
            if ruta.suffix.lower() not in EXTENSIONES_TEXTO and not ruta.name.endswith(".env.example"):
                continue   # imágenes y binarios no se mandan como texto (para eso está "copiar")
            texto = ruta.read_text(encoding="utf-8", errors="replace")
            if len(texto) > MAX_CHARS_FUENTE:
                texto = texto[:MAX_CHARS_FUENTE] + f"\n[... fuente recortada: tiene {len(texto)} caracteres ...]"
            res.append((etiqueta, texto))
    return res


def texto_fuentes(carpeta: Path, cfg: dict) -> str:
    """Todas las fuentes juntas, como las reciben las IAs."""
    return "\n\n".join(f"<<<FUENTE {e}>>>\n{t}\n<<<FIN>>>" for e, t in fuentes(carpeta, cfg))


# ---------- Copiar archivos (imágenes) al borrador ----------

def _base_fija(patron: str) -> str:
    """Parte del patrón antes del primer comodín: 'docs/capturas/**/*.png' → 'docs/capturas'."""
    partes = []
    for p in patron.split("/"):
        if any(c in p for c in "*?["):
            break
        partes.append(p)
    return "/".join(partes)


def copias(carpeta: Path, cfg: dict) -> list[tuple[str, Path, str]]:
    """[(etiqueta de origen, ruta de origen, ruta destino relativa a borrador/)]."""
    res = []
    for regla in cfg.get("copiar", []):
        base, patron, _ = _partir(carpeta, regla["desde"])
        fija = _base_fija(patron)
        for etiqueta, ruta in resolver(carpeta, regla["desde"]):
            relativa = ruta.relative_to(base / fija) if fija else ruta.relative_to(base)
            res.append((etiqueta, ruta, (Path(regla["a"]) / relativa).as_posix()))
    return res


def copiar(carpeta: Path, cfg: dict) -> list[str]:
    """Copia a borrador/ lo de "copiar" que sea nuevo o haya cambiado. Devuelve lo copiado."""
    copiados = []
    for _, origen, destino_rel in copias(carpeta, cfg):
        destino = carpeta / "borrador" / destino_rel
        if destino.exists() and destino.read_bytes() == origen.read_bytes():
            continue
        destino.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(origen, destino)
        copiados.append(destino_rel)
    return copiados


def descripciones(carpeta: Path, cfg: dict) -> dict[str, str]:
    """{ruta de la imagen dentro de su repo/carpeta: texto alternativo} sacado de los Markdown del repo."""
    desc = {}
    bases = [carpeta / CARPETA_REPOS / n for n in cfg.get("repos", {})] + [carpeta]
    for base in bases:
        if not base.is_dir():
            continue
        for md in base.rglob("*.md"):
            if any(x in IGNORAR_ARBOL for x in md.relative_to(base).parts):
                continue
            texto = md.read_text(encoding="utf-8", errors="replace")
            pares = [(alt, src) for alt, src in IMAGEN_MD.findall(texto)] + \
                    [(alt, src) for src, alt in IMAGEN_HTML.findall(texto)]
            for alt, src in pares:
                if src.startswith(("http://", "https://")) or not alt.strip():
                    continue
                try:
                    ruta = (md.parent / src).resolve().relative_to(base.resolve())
                except ValueError:
                    continue
                desc.setdefault(str(base.resolve() / ruta), alt.strip())
    return desc


def lista_imagenes(carpeta: Path, cfg: dict) -> str:
    """Texto para las IAs: cada imagen copiada al borrador y qué muestra."""
    desc = descripciones(carpeta, cfg)
    lineas = []
    for _, origen, destino_rel in copias(carpeta, cfg):
        que = desc.get(str(origen.resolve()), "(sin descripción en el repo)")
        lineas.append(f"- `{destino_rel}`: {que}")
    return "\n".join(lineas)
