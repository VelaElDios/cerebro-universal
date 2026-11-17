---
tipo: "receta"
titulo: "Formato de tablas: alineación superior, ancho controlado y código con path/texttt+allowbreak"
temas: ["latex", "memoria", "tablas", "tfg"]
claves: ["p{}", "m{}", "addlinespace", "linewidth", "small", "path", "texttt", "allowbreak"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[latex]] · [[memoria]] · [[tablas]] · [[tfg]]

1) Usar `p{ancho}` en lugar de `m{}` para alinear contenido arriba. 2) Añadir `\addlinespace` entre filas para aire. 3) Sumar anchos ≤ `\linewidth`. 4) Asegurar ancho suficiente para que no se partan palabras cortas. 5) Poner todo el texto de la tabla en `\small`. 6) Rutas y código con `\path{}` o `\texttt{}\allowbreak{}` para evitar desbordes.

> Ninguna fila se pisa con otra: columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01). Texto de las tablas en `\small`. El código y las rutas van con `\path{}` o con `\texttt{}` más `\allowbreak`, para que no se salgan del margen.
> — `../../memoria/reglas-tfg.md` (cita sin comprobar)
