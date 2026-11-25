---
tipo: "receta"
titulo: "Formato de tablas: alineación superior, ancho controlado y longtable sin filas huérfanas"
temas: ["latex", "memoria", "tfg"]
claves: ["p{}", "m{}", "addlinespace", "linewidth", "small", "path", "texttt", "allowbreak", "longtable", "\\\\*"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[memoria]] · [[tfg]]

- Usar columnas `p{ancho}` (alineación superior), nunca `m{}` (centrada verticalmente).
- Añadir `\addlinespace` entre filas para aire.
- Sumar anchos ≤ `\linewidth`; cada columna debe caber palabras cortas sin partir (ej. «Id», «Hito», «RNF-01»).
- Texto de tablas en `\small`.
- Código y rutas: `\path{}` o `\texttt{}` + `\allowbreak` para evitar desbordes.
- Tablas largas → `longtable`; últimas filas (p. ej. Total) con `\\*` para que no queden solas en la siguiente página.

> Ninguna fila se pisa con otra: columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01).
> — `../../memoria/reglas-tfg.md`

Relacionado: [[reglas-de-maquetacion-de-javier-resumen-accionable]] · [[formato-de-tablas-alineacion-tamanos-y-longtable]] · [[tablas-de-latex-que-no-se-pisan-columnas-p-y-addlinespace]] · [[longtable-sin-fila-huerfana-al-final]]
