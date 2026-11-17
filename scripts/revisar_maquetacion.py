#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
revisar_maquetacion.py — Comprueba las reglas de maquetación de un TFG (memoria/reglas-tfg.md).

Se ejecuta desde la carpeta de la memoria (borrador/), DESPUÉS de compilar:
    python3 ../../../scripts/revisar_maquetacion.py [Memoria.pdf]

Mira el código (.tex) y el PDF. Sale con 1 si incumple alguna regla, explicando cuál y dónde.
Está fuera de borrador/ a propósito: las IAs no pueden tocarlo para aprobarse solas.
"""

import re
import shutil
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

DIR = Path.cwd()
PDF = DIR / (sys.argv[1] if len(sys.argv) > 1 else "Memoria.pdf")
fallos: list[str] = []


def leer(rel: str) -> str:
    p = DIR / rel
    return p.read_text(encoding="utf-8", errors="replace") if p.exists() else ""


def sin_comentarios(texto: str) -> str:
    return "\n".join(re.sub(r"(?<!\\)%.*", "", l) for l in texto.splitlines())


def tex_de_capitulos() -> dict[str, str]:
    return {str(p.relative_to(DIR)): sin_comentarios(p.read_text(encoding="utf-8", errors="replace"))
            for p in sorted((DIR / "chapters").glob("*.tex"))}


def incluidos(principal: str) -> set[str]:
    return {m + ".tex" for m in re.findall(r"\\input\{(chapters/[^}]+?)(?:\.tex)?\}", principal)}


# ---------- 1. Portada y plantilla ----------
principal = sin_comentarios(leer("Memoria.tex"))
if not re.search(r"\\input\{elements/portada\}", principal):
    fallos.append("Regla 1: Memoria.tex no incluye la portada oficial del TFG (\\input{elements/portada}).")
preambulo = sin_comentarios(leer("elements/preambulo.tex"))
if re.search(r"logouclm|logoesii|euroinf", preambulo):
    fallos.append("Regla 1: elements/preambulo.tex tiene una segunda portada (logos UCLM/ESII). "
                  "Solo vale la portada oficial de elements/portada.tex.")
for trozo, que in [("Declaración de autoría", "la declaración de autoría"), ("Resumen", "el Resumen"),
                   ("Abstract", "el Abstract")]:
    if not re.search(trozo, preambulo + principal + "".join(
            sin_comentarios(p.read_text(encoding="utf-8", errors="replace"))
            for p in (DIR / "elements").glob("*.tex")), re.I):
        fallos.append(f"Regla 2: falta {que} de la plantilla (elements/).")
for cmd in ("tableofcontents", "listoffigures", "listoftables", "bibliography"):
    if f"\\{cmd}" not in principal:
        fallos.append(f"Regla 2: Memoria.tex ya no tiene \\{cmd} de la plantilla.")

# ---------- 2. Colores, títulos y enlaces ----------
colores = sin_comentarios(leer("include/colores.tex"))
m = re.search(r"\\definecolor\{tema\}\{RGB\}\{\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\}", colores)
if not m or max(map(int, m.groups())) > 60:
    fallos.append("Regla 3: el color 'tema' de include/colores.tex no es negro: "
                  "\\definecolor{tema}{RGB}{0,0,0} (títulos en negro, sin azul).")
includes = "\n".join(sin_comentarios(leer(f"include/{n}")) for n in ("configuracion.tex", "extra.tex"))
if "hidelinks" not in includes:
    fallos.append("Regla 3: faltan \\hypersetup{hidelinks} (enlaces sin recuadros de color).")

# ---------- 3. Tablas: columnas alineadas arriba ----------
defs = re.findall(r"\\(?:re)?newcolumntype\{L\}\[1\]\{[^\n]*?\}([pmb])\{#1\}", includes)
if not defs or defs[-1] != "p":
    fallos.append("Regla 5: la columna L de las tablas tiene que ser p{} (alineada arriba), no m{}: "
                  "con m{} las filas de varias líneas se descuadran y parecen pisarse.")

# ---------- 4. Figuras repetidas y captions ----------
capitulos = tex_de_capitulos()
activos = incluidos(principal) or set(capitulos)
usos = defaultdict(list)
for rel, tex in capitulos.items():
    if rel not in activos:
        continue
    for n, linea in enumerate(tex.splitlines(), 1):
        for img in re.findall(r"\\includegraphics(?:\[[^\]]*\])?\{([^}]+)\}", linea):
            usos[img].append(f"{rel}:{n}")
        if "\\caption" in linea and re.search(r"(?<![<$\\])->|<-(?!>)", linea):
            fallos.append(f"Regla 11: {rel}:{n}: caption con '->'; usa $\\rightarrow$.")
# Diagramas de secuencia con demasiados participantes: salen diminutos al escalarlos (regla 16)
for rel, tex in capitulos.items():
    if rel not in activos:
        continue
    for m in re.finditer(r"\\begin\{sequencediagram\}(.*?)\\end\{sequencediagram\}", tex, re.S):
        participantes = len(re.findall(r"\\new(?:thread|inst)\b", m.group(1)))
        if participantes > 6:
            linea = tex[:m.start()].count("\n") + 1
            fallos.append(f"Regla 16: {rel}:{linea}: diagrama de secuencia con {participantes} participantes: "
                          "escalado sale diminuto. Como mucho 6 (agrupa participantes o pártelo en dos).")
for img, donde in usos.items():
    if len(donde) > 1:
        fallos.append(f"Regla 10: la imagen {img} sale {len(donde)} veces ({', '.join(donde)}). "
                      "Déjala una vez y en el resto pon \\ref a esa figura.")

# ---------- 5. El PDF, página a página ----------
if not PDF.exists():
    fallos.append(f"No existe {PDF.name}: compila antes de revisar la maquetación.")
elif not shutil.which("pdftotext"):
    fallos.append("Falta pdftotext (paquete poppler-utils) para revisar el PDF página a página.")
else:
    texto = subprocess.run(["pdftotext", "-layout", str(PDF), "-"], capture_output=True,
                           text=True, errors="replace").stdout
    paginas = texto.split("\f")
    if paginas and not paginas[-1].strip():
        paginas.pop()
    cap = re.compile(r"(Figura|Tabla)\s+[A-Z0-9]+\.\d+:")
    for i, pag in enumerate(paginas[1:], start=2):      # la 1 es la portada
        lineas = [l.strip() for l in pag.splitlines() if l.strip()]
        # fuera la cabecera y el número de página
        lineas = [l for l in lineas if not re.fullmatch(r"[ivxlcdm\d]+", l)]
        palabras = sum(len(l.split()) for l in lineas)
        figuras = len(re.findall(r"Figura\s+[A-Z0-9]+\.\d+:", pag))
        tablas = len(re.findall(r"Tabla\s+[A-Z0-9]+\.\d+:", pag))
        muestra = " ".join(" ".join(lineas).split()[:25])
        donde = f" Empieza así: «{muestra}»." if muestra else ""
        if palabras == 0:
            fallos.append(f"Regla 4: la página {i} del PDF está en blanco.")
        elif figuras == 1 and tablas == 0 and palabras < 40:
            fallos.append(f"Regla 8: la página {i} del PDF tiene solo una imagen ({palabras} palabras). "
                          "Hazla más pequeña o júntala con texto u otra figura." + donde)
        elif figuras + tablas == 0 and palabras < 15 and i < len(paginas):
            fallos.append(f"Regla 9: la página {i} del PDF está casi vacía ({palabras} palabras): "
                          "funde esa sección o línea suelta con la anterior (o acorta el párrafo que se desborda a esa página)." + donde)

if fallos:
    print("❌ Maquetación del TFG (memoria/reglas-tfg.md):")
    for f in fallos:
        print("  - " + f)
    sys.exit(1)
print("✅ Maquetación del TFG: cumple las reglas.")
