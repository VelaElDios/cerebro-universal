---
tipo: "receta"
titulo: "Reglas de maquetación de tablas (alineación, anchos, longtable)"
temas: ["latex", "memoria", "tablas", "tfg"]
claves: ["p{}", "m{}", "addlinespace", "linewidth", "small", "path", "texttt", "allowbreak", "longtable", "\\\\*"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[latex]] · [[memoria]] · [[tablas]] · [[tfg]]

1) Usar columnas `p{ancho}` (alineación superior), nunca `m{}`. 2) Añadir `\addlinespace` entre filas para aire. 3) Sumar anchos ≤ `\linewidth`. 4) Asegurar ancho suficiente para que no se partan palabras cortas (Id, Hito, RNF-01). 5) Texto en `\small`. 6) Código/rutas con `\path{}` o `\texttt{}` + `\allowbreak`. 7) Tablas largas en `longtable`; últimas filas (p.ej. Total) unidas con `\\*` para evitar huérfanas.

> Ninguna fila se pisa con otra: columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01).
> — `../../memoria/reglas-tfg.md`
