---
tipo: "receta"
titulo: "Reglas de maquetación de tablas en LaTeX (alineación, anchos, longtable, código y rutas)"
temas: ["latex", "memoria", "tablas", "tfg"]
claves: ["p{}", "m{}", "addlinespace", "linewidth", "small", "path", "texttt", "allowbreak", "longtable", "\\\\*"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-19"
---

Temas: [[latex]] · [[memoria]] · [[tablas]] · [[tfg]]

Temas: [[latex]] · [[memoria]] · [[tablas]] · [[tfg]]

1) Usar columnas `p{ancho}` (alineación superior), nunca `m{}`.
2) Añadir `\addlinespace` entre filas para aire.
3) Sumar anchos ≤ `\linewidth`.
4) Asegurar ancho suficiente para que no se partan palabras cortas (Id, Hito, RNF-01).
5) Texto de las tablas en `\small`.
6) Código y rutas con `\path{}` o `\texttt{}` + `\allowbreak` para evitar desbordes.
7) Tablas largas en `longtable`; últimas filas (p.ej. Total) unidas con `\\*` para evitar huérfanas.

> Ninguna fila se pisa con otra: columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01). Texto de las tablas en `\small`. El código y las rutas van con `\path{}` o con `\texttt{}` más `\allowbreak`, para que no se salgan del margen.
> — `../../memoria/reglas-tfg.md` (cita sin comprobar en nota original A; nota B marcada como verificada)

Relacionado: [[tablas-de-latex-que-no-se-pisan-columnas-p-y-addlinespace]] · [[tablas-largas-en-longtable-con-ultima-fila-acompanada]] · [[que-la-ultima-fila-de-una-longtable-no-se-quede-sola-en-otra]]

> Ninguna fila se pisa con otra: columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01). Texto de las tablas en `\small`. El código y las rutas van con `\path{}` o con `\texttt{}` más `\allowbreak`, para que no se salgan del margen.
> — `../../memoria/reglas-tfg.md` (cita sin comprobar)
> Ninguna fila se pisa con otra: columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01).
> — `../../memoria/reglas-tfg.md`


> ⚠️ Posible contradicción al fusionar: La nota A califica la receta como "propuesto" y la cita como "sin comprobar"; la nota B la titula "verificado".

Fusionada con: Formato de tablas: alineación superior, ancho controlado y código con path/texttt+allowbreak
