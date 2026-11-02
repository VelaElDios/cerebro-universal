#!/usr/bin/env python3
"""
revisar_umlsd.py — Revisión ANTES de compilar de los diagramas de secuencia (pgf-umlsd).

Está fuera de borrador/ (las IAs no lo pueden tocar). Se ejecuta desde borrador/.
pgf-umlsd usa los textos de los mensajes para nombrar nodos de TikZ, así que algunos caracteres rompen
la compilación con errores muy poco claros («Missing \\endcsname inserted», «A node must have a
(possibly empty) label text», «Use of \\mess doesn't match its definition»). LaTeX se para en el
PRIMERO; este script los dice TODOS de una vez, con su línea.

Prohibido dentro de \\mess{…}{TEXTO}{…}, \\begin{call}{…}{TEXTO}{…}{RESPUESTA}, callself y \\newinst:
  - \\#, \\_, \\&, \\%, \\$, \\{, \\} y cualquier comando (\\texttt, \\textbf…): escribir el texto sin ellos
    (p. ej. «juego perfiles» o «juego-perfiles» en vez de «juego\\_perfiles»).
  - #, &, $, _, ^ y ~ tampoco sin barra.
  - Paréntesis en \\mess (TikZ los lee como coordenadas): «ponerUsuario → /jugar», sin «()».
  - Cada participante que se use en \\mess o call tiene que estar declarado con \\newthread o \\newinst.
Sale con 1 si encuentra algo.
"""
import re
import sys
from pathlib import Path

PROHIBIDO = re.compile(r"\\[#_{}&%$^~]|\\[A-Za-z]+|[#&$^_~]")


def argumentos(texto: str, pos: int, n: int) -> list[tuple[int, str]]:
    """Lee n argumentos {…} (con llaves anidadas) desde pos. Devuelve [(posición, contenido)]."""
    res = []
    for _ in range(n):
        while pos < len(texto) and texto[pos] in " \t\n[":
            if texto[pos] == "[":                       # argumento opcional [..]
                pos = texto.index("]", pos) + 1
            else:
                pos += 1
        if pos >= len(texto) or texto[pos] != "{":
            break
        nivel, inicio = 0, pos
        while pos < len(texto):
            c = texto[pos]
            if c == "\\":
                pos += 2
                continue
            if c == "{":
                nivel += 1
            elif c == "}":
                nivel -= 1
                if nivel == 0:
                    break
            pos += 1
        res.append((inicio + 1, texto[inicio + 1:pos]))
        pos += 1
    return res


def revisar(nombre: str, texto: str) -> list[str]:
    fallos = []
    linea = lambda p: texto.count("\n", 0, p) + 1
    for d in re.finditer(r"\\begin\{sequencediagram\}.*?\\end\{sequencediagram\}", texto, flags=re.S):
        bloque, base = d.group(0), d.start()
        declarados = set()
        for m in re.finditer(r"\\new(?:thread|inst)\b", bloque):
            a = argumentos(bloque, m.end(), 1)
            if a:
                declarados.add(a[0][1].strip())
        for patron, posiciones in ((r"\\mess\b", (0, 2)), (r"\\begin\{call\}", (0, 2)),
                                   (r"\\begin\{callself\}", (0,))):
            for m in re.finditer(patron, bloque):
                args = argumentos(bloque, m.end(), max(posiciones) + 1)
                for i in posiciones:
                    if i < len(args) and args[i][1].strip() not in declarados:
                        fallos.append(f"{nombre}:{linea(base + args[i][0])}: el participante «{args[i][1].strip()}» "
                                      "no está declarado con \\newthread o \\newinst en este diagrama")
        orden = [(r"\\mess\b", 3, [1], True), (r"\\begin\{call\}", 4, [1, 3], False),
                 (r"\\begin\{callself\}", 3, [1, 2], False), (r"\\newinst\b", 2, [1], False),
                 (r"\\newthread\b", 2, [1], False)]
        for patron, n, cuales, sin_parentesis in orden:
            for m in re.finditer(patron, bloque):
                args = argumentos(bloque, m.end(), n)
                for i in cuales:
                    if i >= len(args):
                        continue
                    pos, arg = args[i]
                    l = linea(base + pos)
                    for p in PROHIBIDO.finditer(arg):
                        fallos.append(f"{nombre}:{l}: en un diagrama de secuencia no puede ir «{p.group(0)}» "
                                      f"(texto «{arg.strip()[:60]}»): escríbelo sin él")
                        break
                    if sin_parentesis and re.search(r"[()]", arg):
                        fallos.append(f"{nombre}:{l}: en \\mess no puede haber paréntesis (texto "
                                      f"«{arg.strip()[:60]}»): quítalos, p. ej. «ponerUsuario → /jugar»")
    return fallos


def main():
    fallos = []
    rutas = sorted(Path("chapters").glob("*.tex"))
    if not rutas:
        print("revisar_umlsd.py: no encuentro chapters/*.tex (se ejecuta desde borrador/)")
        return 1
    for ruta in rutas:
        texto = "\n".join(re.split(r"(?<!\\)%", l, maxsplit=1)[0] for l in
                          ruta.read_text(encoding="utf-8", errors="replace").splitlines())
        fallos += revisar(f"chapters/{ruta.name}", texto)
    if fallos:
        print(f"REVISIÓN DE DIAGRAMAS FALLIDA: {len(fallos)} problema(s) (se arreglan todos a la vez)")
        for f in fallos:
            print(f)
        return 1
    print("Diagramas de secuencia: OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
