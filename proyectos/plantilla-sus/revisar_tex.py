#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
revisar_tex.py — Revisión rápida de los .tex del borrador ANTES de compilar.

Está FUERA de borrador/ a propósito: las IAs no pueden modificarlo.

Busca el error que más se repite en este proyecto: meter código Lua dentro de
\\directlua{...}. TeX procesa ese texto antes que Lua (convierte # en ##, se come
lo que va tras %, interpreta las \\...), así que solo se permiten llamadas simples:

    \\directlua{sus.get_stat("media", 1)}
    \\directlua{sus = dofile("sus-calculos.lua")}

Nada de local, function, if, for, tex.sprint con cadenas, %, \\, # ni ~.
(Usarlo dentro de \\edef o \\pgfmathsetmacro sí funciona en LuaTeX: no se revisa.)
También avisa de líneas que empiezan por -- o == (comentarios de Lua que LaTeX imprime).

Sale con código 1 e imprime archivo:línea de cada problema, o con 0 si todo está bien.
Uso:  python3 revisar_tex.py   (desde cualquier carpeta)
"""

import re
import sys
from pathlib import Path

BORRADOR = Path(__file__).resolve().parent / "borrador"

# Una sentencia permitida: [nombre =] funcion.con.puntos(argumentos simples)
ARG = r'(?:"[^"\\%#~]*"|[^()"\\%#~])*'
SENTENCIA = re.compile(r'(?:[A-Za-z_]\w*\s*=\s*)?[A-Za-z_][\w.:]*\(' + ARG + r'\)')


def bloques_directlua(texto: str):
    """Devuelve (posición, contenido) de cada \\directlua{...}, con llaves equilibradas."""
    for m in re.finditer(r'\\directlua\s*\{', texto):
        nivel, i = 1, m.end()
        while i < len(texto) and nivel:
            if texto[i] == "{":
                nivel += 1
            elif texto[i] == "}":
                nivel -= 1
            i += 1
        yield m.start(), texto[m.end():i - 1]


def sin_comentarios(linea: str) -> str:
    """Quita el comentario de una línea de TeX (lo que va tras un % no escapado)."""
    return re.split(r'(?<!\\)%', linea, maxsplit=1)[0]


def revisar(ruta: Path) -> list[str]:
    problemas = []
    lineas = ruta.read_text(encoding="utf-8", errors="replace").splitlines()
    texto = "\n".join(sin_comentarios(l) for l in lineas)
    nombre = ruta.relative_to(BORRADOR).as_posix()

    for pos, contenido in bloques_directlua(texto):
        num = texto.count("\n", 0, pos) + 1
        resto = SENTENCIA.sub("", contenido)
        if resto.strip(" \t\n;"):
            muestra = " ".join(contenido.split())[:90]
            problemas.append(f"{nombre}:{num}: \\directlua con código Lua dentro "
                             f"(solo se permiten llamadas a funciones de sus-calculos.lua): {muestra}")

    # Comentarios escritos como en Lua (-- ...) o líneas de ===: LaTeX los imprime como texto
    for num, linea in enumerate(texto.splitlines(), start=1):
        if re.match(r"\s*(--|==)", linea):
            problemas.append(f"{nombre}:{num}: línea que empieza por '{linea.strip()[:2]}': LaTeX la imprime "
                             f"como texto (en LaTeX los comentarios empiezan por %): {linea.strip()[:60]}")
    return problemas


def main():
    if not BORRADOR.exists():
        print("ERROR: no existe la carpeta borrador/")
        return 1
    problemas = []
    for ruta in sorted(BORRADOR.rglob("*.tex")):
        problemas += revisar(ruta)
    if problemas:
        print(f"REVISIÓN TEX FALLIDA: {len(problemas)} problema(s) antes de compilar")
        for p in problemas:
            print("  -", p)
        return 1
    print("REVISIÓN TEX OK: ningún \\directlua con código dentro")
    return 0


if __name__ == "__main__":
    sys.exit(main())
