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
Si existe defensa-sus.tex, también lo compila con esos datos. Y lee el texto de las conclusiones
del PDF (apartado 10 del anexo y la diapositiva de conclusiones): con una media de 38,75 y
"No aceptable" no puede haber frases positivas escritas a mano ("favorablemente", "confirmada"...).
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
# Frases que solo tienen sentido con un buen resultado: con los datos raros no pueden aparecer
# en las conclusiones. Si aparecen, es que el texto está escrito fijo en vez de salir de los datos.
FRASES_POSITIVAS = ("favorablemente", "confirmad", "satisfac", "supera", "por encima",
                    "excelente", "productiv", "rigurosamente", "cumplimiento")

TEMPORALES = ("*.aux", "*.log", "*.fls", "*.fdb_latexmk", "*.out", "*.toc", "*.bbl", "*.blg",
              "*.bcf", "*.run.xml", "*.synctex.gz", "*.pdf", "resultados.json")


def primeros_errores(log: Path, maximo: int = 6) -> list[str]:
    """Las líneas de error de LaTeX más útiles (archivo:línea o '!')."""
    if not log.exists():
        return []
    lineas = log.read_text(encoding="utf-8", errors="replace").splitlines()
    return [l for l in lineas if re.search(r"^!|^\S+\.(tex|lua|sty):\d+:|^\[\\directlua\]:\d+:", l)][:maximo]


def texto_pdf(pdf: Path) -> str | None:
    """Texto de un PDF con pdftotext o, si no está, con pypdf (se instala si hace falta)."""
    if shutil.which("pdftotext"):
        r = subprocess.run(["pdftotext", "-layout", str(pdf), "-"], capture_output=True, text=True, errors="replace")
        if r.returncode == 0:
            return r.stdout
    try:
        import pypdf
    except ImportError:
        subprocess.run([sys.executable, "-m", "pip", "install", "-q", "pypdf"], capture_output=True)
        try:
            import pypdf
        except ImportError:
            return None
    return "\n".join(pag.extract_text() or "" for pag in pypdf.PdfReader(str(pdf)).pages)


def tramo(texto: str, desde: str, hasta: tuple[str, ...]) -> str:
    """El trozo de texto entre el primer título que contiene `desde` y el siguiente corte."""
    i = texto.find(desde)
    if i < 0:
        return ""
    fin = min([j for j in (texto.find(h, i + len(desde)) for h in hasta) if j > 0] or [len(texto)])
    return texto[i:fin]


def revisar_conclusiones(nombre: str, seccion: str) -> list[str]:
    """Problemas de una sección de conclusiones generada con los datos raros."""
    if not seccion.strip():
        return [f"{nombre}: no encuentro la sección de conclusiones en el PDF"]
    plano = " ".join(seccion.split()).lower()
    problemas = []
    for frase in FRASES_POSITIVAS:
        if frase in plano:
            k = plano.index(frase)
            problemas.append(f"{nombre}: con media 38,75 y 'No aceptable' dice «…{plano[max(0, k - 60):k + 40]}…» "
                             f"(texto positivo escrito fijo: debe salir de los datos, como sus.imprimir_conclusion())")
    if "no aceptable" not in plano:
        problemas.append(f"{nombre}: las conclusiones no mencionan la aceptabilidad calculada ('No aceptable')")
    return problemas


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

        # Diapositivas (Fase 2) con los mismos datos raros, si existen
        defensa = copia / "defensa-sus.tex"
        if defensa.exists():
            d = subprocess.run(["latexmk", "-g", "-lualatex", "-interaction=nonstopmode", "-halt-on-error",
                                "-file-line-error", defensa.name], cwd=copia, capture_output=True, text=True,
                               errors="replace", env=entorno, timeout=600)
            if d.returncode != 0:
                print("PRUEBA CON DATOS RAROS FALLIDA: defensa-sus.tex no compila con pruebas/respuestas-raras.csv")
                for l in primeros_errores(copia / "defensa-sus.log"):
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
        # Las conclusiones tienen que depender de los datos
        problemas = []
        texto = texto_pdf(copia / "anexo-sus.pdf")
        if texto is None:
            print("AVISO: no hay pdftotext ni pypdf: no se revisa el texto de las conclusiones")
        else:
            problemas += revisar_conclusiones("anexo-sus.pdf (apartado 10)",
                                              tramo(texto, "Interpretación de resultados", ("Figura", "Referencias")))
            if defensa.exists():
                texto_d = texto_pdf(copia / "defensa-sus.pdf") or ""
                problemas += revisar_conclusiones("defensa-sus.pdf (diapositiva de conclusiones)",
                                                  tramo(texto_d, "Conclusiones", ("Trabajo de Fin de Grado",)))
        if problemas:
            print("PRUEBA CON DATOS RAROS FALLIDA: las conclusiones no se adaptan a los datos")
            for pr in problemas:
                print("  -", pr)
            return 1

        print("PRUEBA CON DATOS RAROS OK: " + salida.splitlines()[-1])
        return 0


if __name__ == "__main__":
    sys.exit(main())
