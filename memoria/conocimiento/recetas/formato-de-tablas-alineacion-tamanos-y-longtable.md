---
tipo: "receta"
titulo: "Formato de tablas: alineación, tamaños y longtable"
temas: ["latex", "memoria", "tfg"]
claves: ["p{}", "m{}", "addlinespace", "small", "path", "texttt", "allowbreak", "longtable", "\\\\*"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[latex]] · [[memoria]] · [[tfg]]

Reglas de maquetación de tablas:
- Usar columnas `p{}` (alineación superior), nunca `m{}` (centrada verticalmente).
- Añadir `\addlinespace` entre filas para dar aire.
- Anchos totales ≤ `\linewidth`; cada columna debe caber palabras cortas sin partir (ej. «Id», «Hito», «RNF-01»).
- Texto de tablas en `\small`.
- Código y rutas: `\path{}` o `\texttt{}` + `\allowbreak` para evitar desbordes.
- Tablas largas → entorno `longtable`.
- Últimas filas (ej. fila «Total») unidas con `\\*` para que no queden solas en la página siguiente.

> **Ninguna fila se pisa con otra:** columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01).
> — `../../memoria/reglas-tfg.md`
