#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
revisar_figuras.py — Los «ojos» del cerebro: mira de verdad los diagramas del PDF.

Las IAs que escriben la memoria solo leen el código LaTeX, y desde el código no se ve que una flecha cruza
una caja o que las letras han quedado diminutas. Este script convierte en imagen cada página donde hay un
diagrama dibujado (TikZ, diagramas de secuencia, pgfplots) y le pregunta a Gemini (gratis, ve imágenes)
si tiene alguno de los fallos de las reglas 16-18 de memoria/reglas-tfg.md.

Antes de preguntar a Gemini se hace una revisión GEOMÉTRICA exacta (scripts/revisar_geometria.py): con las
coordenadas reales del PDF mira si alguna línea pasa por encima de letras, si se pisan cajas, si hay palabras
partidas con guion o si las letras han quedado diminutas. Eso no depende de la IA: si falla, falla.

Se ejecuta desde la carpeta de la memoria (borrador/), DESPUÉS de compilar:
    python3 ../../../scripts/revisar_figuras.py Memoria.pdf

- Solo se pregunta por las páginas que han cambiado: el resultado de cada imagen se guarda en
  ../.revision-figuras.json (fuera de borrador/, las IAs no lo pueden tocar).
- Sin GEMINI_API_KEY, o si Gemini no responde o se acaba el cupo, avisa y no bloquea (sale con 0).
- Sale con 1 si algún diagrama tiene fallos, diciendo cuál, en qué página, en qué archivo y qué le pasa.
"""

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

DIR = Path.cwd()
PDF = DIR / (sys.argv[1] if len(sys.argv) > 1 else "Memoria.pdf")
CACHE = DIR.parent / ".revision-figuras.json"
MODELOS_POR_DEFECTO = ["gemini-flash-latest", "gemini-3.5-flash-lite"]


def modelos_gemini() -> list[str]:
    """Los mismos modelos de Gemini que usa el resto del cerebro (config/ias.json), en su orden."""
    try:
        cfg = json.loads((Path(__file__).resolve().parents[1] / "config" / "ias.json").read_text(encoding="utf-8"))
        res = []
        for p in cfg.get("proveedores", {}).values():
            if p.get("tipo") == "gemini":
                res += [m for m in p.get("modelos", []) if m not in res]
        return res or MODELOS_POR_DEFECTO
    except Exception:
        return MODELOS_POR_DEFECTO


MODELOS = modelos_gemini()
_descartados: dict[str, str] = {}   # modelo → por qué no se usa más en esta ejecución (404, cupo agotado)
VERSION = "v2"   # cambiarla invalida los veredictos guardados (p. ej. si se mejora el prompt)
DIBUJO = re.compile(r"\\begin\{(tikzpicture|sequencediagram|axis)\}")

PROMPT = """Eres revisor de maquetación de un Trabajo Fin de Grado. En esta página hay un diagrama: «{figura}».
Mira SOLO ese diagrama (no las capturas de pantalla ni el texto de alrededor). Recorre UNA A UNA cada línea y
cada flecha, de dónde sale y a dónde llega, y comprueba si por el camino pasa por encima de otra caja o de algún
texto. Después mira cada caja. Sé exigente: un revisor humano lo va a mirar con lupa. Fallos a buscar:

1. Una línea o flecha que ATRAVIESA una caja o pasa por encima de un texto (no cuenta si solo llega al borde).
2. Cajas que se PISAN o se tapan unas a otras, o un texto que se sale de su caja.
3. Palabras o rutas PARTIDAS dentro de una caja con guion o corte raro (p. ej. «sr-c/services», «repo-sitories»).
4. Etiquetas de flechas encima de cajas o de otras etiquetas, de forma que no se leen.
5. Letras del diagrama mucho MÁS PEQUEÑAS que las del pie de figura (se leen con dificultad).
6. Partes del diagrama CORTADAS por el borde de la página o del área de texto.

Responde SOLO con JSON, sin nada más:
{{"ok": true}}  o  {{"ok": false, "problemas": ["descripción concreta de cada fallo: qué elemento y dónde"]}}"""


def leer(ruta: Path) -> str:
    return ruta.read_text(encoding="utf-8", errors="replace") if ruta.exists() else ""


def sin_comentarios(texto: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*", "", l) for l in texto.splitlines())


def figuras_dibujadas() -> dict[str, tuple[str, int]]:
    """{label: (archivo, línea)} de las figuras que llevan un dibujo (no una imagen)."""
    res = {}
    for p in sorted((DIR / "chapters").glob("*.tex")):
        tex = sin_comentarios(leer(p))
        for m in re.finditer(r"\\begin\{figure\*?\}(.*?)\\end\{figure\*?\}", tex, re.S):
            if not DIBUJO.search(m.group(1)):
                continue
            for etiqueta in re.findall(r"\\label\{(fig:[^}]+)\}", m.group(1)):
                res[etiqueta] = (p.relative_to(DIR).as_posix(), tex[:m.start()].count("\n") + 1)
    return res


def numeros(etiquetas) -> dict[str, str]:
    """{label: «3.1»} sacado del .aux de la compilación."""
    aux = leer(PDF.with_suffix(".aux"))
    res = {}
    for e in etiquetas:
        m = re.search(r"\\newlabel\{" + re.escape(e) + r"\}\{\{([^}]+)\}", aux)
        if m:
            res[e] = m.group(1)
    return res


def pagina_de(numero: str, paginas: list[str]) -> int | None:
    patron = re.compile(r"Figura\s+" + re.escape(numero) + r"\s*:")
    for i, texto in enumerate(paginas, start=1):
        if patron.search(texto):
            return i
    return None


def imagen(pagina: int) -> bytes:
    base = DIR.parent / ".figura-tmp"
    subprocess.run(["pdftoppm", "-r", "170", "-png", "-singlefile", "-f", str(pagina), "-l", str(pagina),
                    str(PDF), str(base)], check=True, capture_output=True, timeout=120)
    datos = (base.with_suffix(".png")).read_bytes()
    base.with_suffix(".png").unlink()
    return datos


def preguntar(png: bytes, figura: str) -> dict:
    from google import genai
    from google.genai import types
    cliente = genai.Client(api_key=os.environ["GEMINI_API_KEY"], http_options=types.HttpOptions(timeout=120_000))
    errores = []
    for modelo in MODELOS:
        if modelo in _descartados:
            errores.append(f"{modelo}: {_descartados[modelo]}")
            continue
        try:
            r = cliente.models.generate_content(
                model=modelo,
                contents=[types.Part.from_bytes(data=png, mime_type="image/png"), PROMPT.format(figura=figura)],
                config=types.GenerateContentConfig(temperature=0.0, response_mime_type="application/json"))
            texto = re.sub(r"^```(?:json)?|```$", "", (r.text or "").strip()).strip()
            datos = json.loads(texto)
            if isinstance(datos, dict) and "ok" in datos:
                return datos
        except Exception as e:
            texto = str(e)
            corto = ("no existe (404)" if "404" in texto or "NOT_FOUND" in texto else
                     "cupo gratuito agotado (429)" if "429" in texto or "RESOURCE_EXHAUSTED" in texto else texto[:120])
            if corto.endswith(")"):
                _descartados[modelo] = corto      # no se insiste con ese modelo en el resto de figuras
            errores.append(f"{modelo}: {corto}")
    raise RuntimeError("; ".join(errores) or "sin modelos de Gemini")


def main() -> int:
    if not PDF.exists():
        print(f"❌ No existe {PDF.name}: compila antes de revisar las figuras.")
        return 1
    figuras = figuras_dibujadas()
    if not figuras:
        print("✅ Figuras: no hay diagramas dibujados que revisar.")
        return 0
    try:
        sys.path.insert(0, str(Path(__file__).resolve().parent))
        import revisar_geometria as geometria
        import pdfplumber  # noqa: F401
    except ImportError:
        geometria = None
        print("⚠️ Figuras: sin pdfplumber no hago la revisión geométrica (pip install pdfplumber).")
    if not os.environ.get("GEMINI_API_KEY"):
        print("⚠️ Figuras: sin GEMINI_API_KEY Gemini no mira los diagramas (solo la revisión geométrica).")
    texto = subprocess.run(["pdftotext", "-layout", str(PDF), "-"], capture_output=True, text=True,
                           errors="replace", timeout=120).stdout
    paginas = texto.split("\f")
    nums = numeros(figuras)
    cache = json.loads(leer(CACHE) or "{}")
    fallos, sin_revisar, revisadas = [], [], 0
    for etiqueta, (archivo, linea) in figuras.items():
        numero = nums.get(etiqueta)
        pagina = pagina_de(numero, paginas) if numero else None
        if not pagina:
            continue
        nombre = f"Figura {numero} ({etiqueta})"
        png = imagen(pagina) if os.environ.get("GEMINI_API_KEY") else b""
        # 1) Geometría exacta (sin IA)
        if geometria:
            try:
                problemas = geometria.revisar(PDF, numero, pagina)
            except Exception as e:
                problemas = []
                print(f"⚠️ Figuras: la revisión geométrica de {nombre} falló ({e}); sigo con Gemini.")
            if problemas:
                fallos.append(f"Reglas 16-18: {nombre}, página {pagina} del PDF, {archivo}:{linea} (medido en el "
                              f"PDF): " + "; ".join(problemas))
                continue
        if not os.environ.get("GEMINI_API_KEY"):
            continue
        # 2) Gemini mira la imagen
        clave = hashlib.md5(png + (VERSION + etiqueta).encode()).hexdigest()
        if clave not in cache:
            try:
                cache[clave] = preguntar(png, f"Figura {numero}")
            except Exception as e:
                sin_revisar.append(f"{nombre}: {e}")
                continue
        revisadas += 1
        r = cache[clave]
        if not r.get("ok", True):
            problemas = "; ".join(str(p) for p in r.get("problemas", [])) or "tiene fallos de dibujo"
            fallos.append(f"Reglas 16-18: {nombre}, página {pagina} del PDF, {archivo}:{linea}: {problemas}")
    CACHE.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")
    for s in sin_revisar:
        print(f"⚠️ Figuras: Gemini no pudo mirar {s}. No bloquea y NO hay que revisarlo a mano: la medición "
              "geométrica del PDF ya lo ha comprobado.")
    if fallos:
        print("❌ Diagramas con fallos (medidos en el PDF o vistos por Gemini):")
        for f in fallos:
            print("  - " + f)
        return 1
    print(f"✅ Figuras: {len(figuras)} diagramas medidos en el PDF"
          + (f" y {revisadas} revisados a ojo por Gemini" if revisadas else "") + ", sin fallos.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
