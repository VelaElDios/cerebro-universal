---
tipo: "dato"
titulo: "Secuencia exacta de instrucciones y registros del ejemplo de marcador (ciclos 1-9)"
temas: ["ac", "arquitectura", "ejemplo", "fadd.d", "fdiv.d", "fld", "fmul.d", "fsub.d", "instrucciones", "registros", "scoreboard"]
claves: ["f6", "f2", "f4", "f8", "f0", "f10", "f12", "x2", "x3", "34", "45"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[ejemplo]] · [[fadd.d]] · [[fdiv.d]] · [[fld]] · [[fmul.d]] · [[fsub.d]] · [[instrucciones]] · [[registros]] · [[scoreboard]]

Código completo del fragmento (6 instrucciones, 7 registros FP, 2 registros base enteros):

| # | Instrucción | Significado | Destino | Fuentes |
|---|-------------|-------------|---------|---------|
| 1 | `fld f6, 34(x2)` | Carga double desde Mem[x2+34] | f6 | x2 |
| 2 | `fld f2, 45(x3)` | Carga double desde Mem[x3+45] | f2 | x3 |
| 3 | `fmul.d f0, f2, f4` | f0 = f2 × f4 | f0 | f2, f4 |
| 4 | `fsub.d f8, f6, f2` | f8 = f6 − f2 | f8 | f6, f2 |
| 5 | `fdiv.d f10, f0, f6` | f10 = f0 / f6 | f10 | f0, f6 |
| 6 | `fadd.d f6, f8, f2` | f6 = f8 + f2 | f6 | f8, f2 |

Registros FP involucrados: **f0, f2, f4, f6, f8, f10, f12** (f12 no se usa). Registros base: **x2, x3**.
Offsets: 34 y 45 (bytes, alineados a 8 para double).

Grafo de dependencias:
- f2: producida por #2 → consumida por #3, #4, #6
- f6: producida por #1 → consumida por #4, #5; **re-escrita por #6** (WAW+WAR)
- f0: producida por #3 → consumida por #5
- f8: producida por #4 → consumida por #6
- f4: solo leída (valor inicial en registro)
- f10, f12: solo escritas

Este grafo es el que el marcador resuelve dinámicamente ciclo a ciclo.

> fld f6, 34(x2) fld f2, 45(x3) fmul.d f0, f2, f4 fsub.d f8, f6, f2 fdiv.d f10, f0, f6 fadd.d f6, f8, f2
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[como-leer-la-evolucion-ciclo-a-ciclo-de-un-marcador-con-carg]] · [[latencias-de-unidades-funcionales-en-el-ejemplo-de-marcador]]
