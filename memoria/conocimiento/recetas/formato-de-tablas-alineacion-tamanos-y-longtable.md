---
tipo: "receta"
titulo: "Reglas de maquetación de tablas en LaTeX: alineación, anchos, longtable, código y rutas"
temas: ["latex", "memoria", "tablas", "tfg"]
claves: ["p{}", "m{}", "addlinespace", "small", "path", "texttt", "allowbreak", "longtable", "\\\\*", "linewidth"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-21"
actualizado: "2026-11-22"
---

Temas: [[latex]] · [[memoria]] · [[tablas]] · [[tfg]]

Temas: [[latex]] · [[memoria]] · [[tablas]] · [[tfg]]

Reglas (7 puntos):
1. Usar columnas `p{ancho}` (alineación superior), nunca `m{}` (centrada verticalmente).
2. Añadir `\addlinespace` entre filas para dar aire.
3. Sumar anchos ≤ `\linewidth`.
4. Asegurar ancho suficiente para que no se partan palabras cortas (ej. «Id», «Hito», «RNF-01»).
5. Texto de las tablas en `\small`.
6. Código y rutas con `\path{}` o `\texttt{}` + `\allowbreak` para evitar desbordes.
7. Tablas largas → entorno `longtable`; últimas filas (p.ej. fila «Total») unidas con `\\*` para evitar huérfanas.

> **Resumen de estilo:** Ninguna fila se pisa con otra: columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01). Texto de las tablas en `\small`. El código y las rutas van con `\path{}` o con `\texttt{}` más `\allowbreak`, para que no se salgan del margen.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[tablas-de-latex-que-no-se-pisan-columnas-p-y-addlinespace]] · [[tablas-largas-en-longtable-con-ultima-fila-acompanada]] · [[longtable-sin-fila-huerfana-al-final]] · [[formato-de-tablas-alineacion-superior-ancho-controlado-y-lon]]

> **Ninguna fila se pisa con otra:** columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01).
> — `../../memoria/reglas-tfg.md`
> Ninguna fila se pisa con otra: columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01). Texto de las tablas en `\small`. El código y las rutas van con `\path{}` o con `\texttt{}` más `\allowbreak`, para que no se salgan del margen.
> — `../../memoria/reglas-tfg.md` (cita sin comprobar en nota original A; nota B marcada como verificada)
> Ninguna fila se pisa con otra: columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01). Texto de las tablas en `\small`. El código y las rutas van con `\path{}` o con `\texttt{}` más `\allowbreak`, para que no se salgan del margen.
> — `../../memoria/reglas-tfg.md` (cita sin comprobar)
> Ninguna fila se pisa con otra: columnas alineadas arriba (`p{}`, nunca `m{}`) y algo de aire entre filas (`\addlinespace`). Los anchos suman como mucho `\linewidth` y cada columna es lo bastante ancha para que no se partan las palabras cortas (Id, Hito, RNF-01).
> — `../../memoria/reglas-tfg.md`


> ⚠️ Posible contradicción al fusionar: Estado de verificación contradictorio: la cabecera de la Nota A dice "verificado", la de la Nota B dice "propuesto"; además, la propia Nota B incluye un aviso que invierte esa atribución (dice que A es "propuesto" y B "verificado"). La cita a `../../memoria/reglas-tfg.md` aparece en A sin advertencia y en B como "cita sin comprobar en nota original A; nota B marcada como verificada".

Fusionada con: Reglas de maquetación de tablas en LaTeX (alineación, anchos, longtable, código y rutas)
