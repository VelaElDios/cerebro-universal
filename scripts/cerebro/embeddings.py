"""
Búsqueda por significado: cada nota del cerebro tiene un «embedding» (un vector que resume de qué trata),
calculado gratis con la API de Gemini. Así una tarea encuentra las notas que hablan de lo mismo aunque
usen otras palabras, y el jardinero detecta notas repetidas o muy parecidas.

  memoria/mapas/embeddings.json   {"modelo", "dim", "notas": {ruta: {"md5": ..., "v": base64 de float16}}}

Solo se recalculan las notas nuevas o cambiadas. Sin GEMINI_API_KEY, o si la API falla, todo sigue
funcionando con la búsqueda por palabras clave (conocimiento.seleccionar): esto es una mejora, no una pieza
de la que dependa nada.
"""

import base64
import hashlib
import json
import math
import os
import re
import struct
import time
from pathlib import Path

from . import nucleo
from . import proveedores as prov

MODELOS = ["gemini-embedding-001", "text-embedding-004"]
DIM = 256
LOTE = 25                 # notas por petición (la capa gratuita cuenta cada nota)
MAX_CHARS_NOTA = 6000     # lo que se manda de cada nota (título + cuerpo)

_cache_consultas: dict[str, list[float]] = {}
_desactivado = False      # si la API falla una vez en esta ejecución, no se insiste


def ruta_indice() -> Path:
    return nucleo.RAIZ / "memoria" / "mapas" / "embeddings.json"


def _empaquetar(v: list[float]) -> str:
    return base64.b64encode(struct.pack(f"<{len(v)}e", *v)).decode()


def _desempaquetar(s: str) -> list[float]:
    datos = base64.b64decode(s)
    return list(struct.unpack(f"<{len(datos) // 2}e", datos))


def _normalizar(v: list[float]) -> list[float]:
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


def coseno(a: list[float], b: list[float]) -> float:
    """Los vectores se guardan normalizados: el coseno es el producto escalar."""
    return sum(x * y for x, y in zip(a, b))


def cargar() -> dict:
    ruta = ruta_indice()
    if ruta.exists():
        try:
            return json.loads(ruta.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"modelo": None, "dim": DIM, "notas": {}}


def vectores() -> dict[str, list[float]]:
    """{ruta de la nota: vector normalizado} de todo lo que ya tiene embedding."""
    return {r: _desempaquetar(d["v"]) for r, d in cargar().get("notas", {}).items()}


def _texto_nota(ruta: Path) -> str:
    texto = ruta.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", texto, re.S)
    if m:
        titulo = re.search(r'^titulo:\s*"?(.*?)"?\s*$', m.group(1), re.M)
        texto = (titulo.group(1) + "\n\n" if titulo else "") + m.group(2)
    return re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", r"\1", texto)[:MAX_CHARS_NOTA]


def notas_del_vault() -> list[Path]:
    raiz = nucleo.RAIZ
    rutas = []
    for carpeta in ("memoria/conocimiento", "memoria/lecciones"):
        base = raiz / carpeta
        if base.exists():
            rutas += sorted(base.rglob("*.md"))
    rutas += sorted((raiz / "proyectos").glob("*/estado.md"))
    return rutas


def _embeber(textos: list[str], tarea: str) -> tuple[list[list[float]], str]:
    """Llama a Gemini. Devuelve (vectores normalizados, modelo usado)."""
    global _desactivado
    clave = os.environ.get("GEMINI_API_KEY", "").strip()
    if not clave or _desactivado:
        raise RuntimeError("sin GEMINI_API_KEY")
    from google import genai
    from google.genai import types
    cliente = genai.Client(api_key=clave, http_options=types.HttpOptions(timeout=120_000))
    ultimo = None
    for modelo in MODELOS:
        for intento in range(3):
            try:
                r = cliente.models.embed_content(
                    model=modelo, contents=textos,
                    config=types.EmbedContentConfig(task_type=tarea, output_dimensionality=DIM))
                return [_normalizar(list(e.values)[:DIM]) for e in r.embeddings], modelo
            except Exception as e:
                ultimo = e
                # Cupo por minuto de la capa gratuita: esperar un minuto y repetir (si queda tiempo de paso)
                if ("429" in str(e) or "RESOURCE_EXHAUSTED" in str(e)) and prov.tiempo_restante() > 5 * 60:
                    print("  embeddings: cupo por minuto agotado, espero 65 s")
                    time.sleep(65)
                    continue
                break
    _desactivado = True
    raise RuntimeError(f"la API de embeddings no responde: {str(ultimo)[:200]}")


def actualizar(max_notas: int = 400) -> str:
    """Calcula los embeddings de las notas nuevas o cambiadas y quita los de las borradas."""
    indice = cargar()
    notas = indice.setdefault("notas", {})
    vivas, pendientes = set(), []
    for ruta in notas_del_vault():
        rel = ruta.relative_to(nucleo.RAIZ).as_posix()
        vivas.add(rel)
        texto = _texto_nota(ruta)
        huella = hashlib.md5(texto.encode("utf-8")).hexdigest()
        if notas.get(rel, {}).get("md5") != huella:
            pendientes.append((rel, texto, huella))
    borradas = [r for r in notas if r not in vivas]
    for r in borradas:
        del notas[r]
    hechas = 0
    try:
        for i in range(0, min(len(pendientes), max_notas), LOTE):
            lote = pendientes[i:i + LOTE]
            vecs, modelo = _embeber([t for _, t, _ in lote], "RETRIEVAL_DOCUMENT")
            if indice.get("modelo") not in (None, modelo):
                notas.clear()              # otro modelo: los vectores viejos no son comparables
                indice["modelo"] = modelo
                return actualizar(max_notas)
            indice["modelo"], indice["dim"] = modelo, DIM
            for (rel, _, huella), v in zip(lote, vecs):
                notas[rel] = {"md5": huella, "v": _empaquetar(v)}
                hechas += 1
    except RuntimeError as e:
        aviso = f" ({e})"
    else:
        aviso = ""
    if hechas or borradas:
        ruta_indice().parent.mkdir(parents=True, exist_ok=True)
        ruta_indice().write_text(json.dumps(indice, ensure_ascii=False), encoding="utf-8")
    return f"embeddings: {hechas} nuevos, {len(borradas)} quitados, {len(notas)} en total{aviso}"


def consulta(texto: str) -> list[float] | None:
    """Vector de una consulta (lo que está haciendo la IA). None si no hay API: se usa solo palabras clave."""
    texto = texto[-8000:]
    clave = hashlib.md5(texto.encode("utf-8")).hexdigest()
    if clave in _cache_consultas:
        return _cache_consultas[clave]
    try:
        v = _embeber([texto], "RETRIEVAL_QUERY")[0][0]
    except Exception:
        return None
    _cache_consultas[clave] = v
    return v


def parecidas(rutas_y_vectores: dict[str, list[float]], umbral: float) -> list[tuple[float, str, str]]:
    """Parejas de notas con un coseno ≥ umbral, de más a menos parecidas."""
    claves = sorted(rutas_y_vectores)
    res = []
    for i, a in enumerate(claves):
        va = rutas_y_vectores[a]
        for b in claves[i + 1:]:
            c = coseno(va, rutas_y_vectores[b])
            if c >= umbral:
                res.append((c, a, b))
    return sorted(res, reverse=True)
