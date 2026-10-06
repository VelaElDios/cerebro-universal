#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
probar_datos_raros.py — Segunda prueba del proyecto plantilla-sus.

Está FUERA de borrador/ a propósito: las IAs no pueden modificarlo.

Los datos de ejemplo son "demasiado bonitos" (media exacta de 85, todos aceptables), así que
esconden fallos. Esta prueba copia el borrador a una carpeta temporal, cambia el CSV por
pruebas/respuestas-raras.csv y lo compila otra vez:

  - media con decimales (38,75) → detecta si algo se redondea mal
  - notas bajas (F, "El peor imaginable", "No aceptable") → la conclusión no puede ser siempre positiva
  - comentarios y perfiles con & % $ # _ { } ~ ^ y comillas → todo se tiene que escapar
  - un comentario vacío y una fila con un valor fuera de 1-5 → el documento debe avisar y excluirla

Luego comprueba con verificar.py que el resultados.json de esa compilación cuadra con el CSV raro.
No toca nada del borrador. Sale con 0 si todo va bien y con 1 si algo falla.
Uso:  python3 probar_datos_raros.py   (desde cualquier carpeta)
"""

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

CARPETA = Path(__file__).resolve().parent
BORRADOR = CARPETA / "borrador"
CSV_RARO = CARPETA / "pruebas" / "respuestas-raras.csv"
PRINCIPAL = "anexo-sus.tex"
TEMPORALES = ("*.aux", "*.log", "*.fls", "*.fdb_latexmk", "*.out", "*.toc", "*.bbl", "*.blg",
              "*.bcf", "*.run.xml", "*.synctex.gz", "*.pdf", "resultados.json")


def primeros_errores(log: Path, maximo: int = 6) -> list[str]:
    """Las líneas de error de LaTeX más útiles (archivo:línea o '!')."""
    if not log.exists():
        return []
    lineas = log.read_text(encoding="utf-8", errors="replace").splitlines()
    return [l for l in lineas if re.search(r"^!|^\S+\.(tex|lua|sty):\d+:|^\[\\directlua\]:\d+:", l)][:maximo]


def main():
    if not CSV_RARO.exists():
        print(f"ERROR: no existe {CSV_RARO.relative_to(CARPETA)}")
        return 1
    with tempfile.TemporaryDirectory(prefix="sus-raros-") as tmp:
        copia = Path(tmp) / "borrador"
        shutil.copytree(BORRADOR, copia, ignore=shutil.ignore_patterns(*TEMPORALES))
        (copia / "datos").mkdir(exist_ok=True)
        shutil.copy(CSV_RARO, copia / "datos" / "respuestas.csv")

        entorno = {**os.environ, "max_print_line": "1000"}
        r = subprocess.run(["latexmk", "-g", "-lualatex", "-interaction=nonstopmode", "-halt-on-error",
                            "-file-line-error", PRINCIPAL], cwd=copia, capture_output=True, text=True,
                           errors="replace", env=entorno, timeout=600)
        if r.returncode != 0:
            print("PRUEBA CON DATOS RAROS FALLIDA: el documento no compila con pruebas/respuestas-raras.csv")
            print("  (comentarios con & % $ # _ { } ~ ^ y comillas, notas bajas, una fila inválida)")
            for l in primeros_errores(copia / Path(PRINCIPAL).with_suffix(".log")):
                print("  -", l)
            return 1

        v = subprocess.run([sys.executable, str(CARPETA / "verificar.py"),
                            str(copia / "datos" / "respuestas.csv"), str(copia / "resultados.json")],
                           capture_output=True, text=True, errors="replace")
        salida = v.stdout.strip()
        if v.returncode != 0:
            print("PRUEBA CON DATOS RAROS FALLIDA: resultados.json no cuadra con pruebas/respuestas-raras.csv")
            print("\n".join("  " + l for l in salida.splitlines()))
            return 1
        print("PRUEBA CON DATOS RAROS OK: " + salida.splitlines()[-1])
        return 0


if __name__ == "__main__":
    sys.exit(main())
