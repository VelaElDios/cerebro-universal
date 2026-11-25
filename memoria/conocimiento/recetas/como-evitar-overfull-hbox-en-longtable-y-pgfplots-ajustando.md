---
tipo: "receta"
titulo: "Cómo evitar overfull hbox en longtable y pgfplots ajustando anchos de columna"
temas: ["latex", "longtable", "maquetacion", "overfull", "pgfplots", "tablas"]
claves: ["L{...}", "p{...}", "width=0.85\\linewidth", "scale only axis", "ylabel style", "xshift"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/a1-desarrollo.tex (burndowns) y chapters/04-descripcion.tex (tabla RF)", "chapters/04-descripcion.tex (tablas de requisitos) y chapters/03-propuesta.tex (tabla herramientas)"]
confianza: "propuesto"
fecha: "2026-11-25"
actualizado: "2026-11-25"
---

Temas: [[latex]] · [[longtable]] · [[maquetacion]] · [[overfull]] · [[pgfplots]]

1. En `longtable`, usar columnas `L{...}` (que son `p{...}` alineadas arriba) y sumar anchos ≤ `\linewidth`. 2. En `pgfplots`, reducir `width` a `0.85\linewidth` o menos, activar `scale only axis`, y desplazar la etiqueta del eje Y con `ylabel style={anchor=east, xshift=-3pt}`. 3. Usar `\small` al inicio de `longtable` y `table` (`\AtBeginEnvironment{longtable}{\small}`). 4. `\renewcommand{\arraystretch}{1.15}` para aire entre filas. 5. `\setlength{\LTpre}{0pt}\setlength{\LTpost}{0pt}` para evitar espacio extra. 6. `\raggedbottom` global para que las páginas no intenten estirarse y fallen con "Infinite glue shrinkage" al partir longtables.

> Anchos que suman ≤ \linewidth (p. ej., 13,2 cm + 5 separadores = 15,31 cm ≤ 15,5 cm). En pgfplots: `width=0.85\linewidth`, `scale only axis`, `ylabel style={anchor=east, xshift=-3pt}` para que la etiqueta del eje Y no choque con la gráfica y no haya overfull hbox.
> — `chapters/a1-desarrollo.tex (burndowns) y chapters/04-descripcion.tex (tabla RF)` (cita sin comprobar)

## Ampliación (2026-11-25, memoria-procesos)
Para que las tablas `longtable` no se salgan del margen (overfull hbox):
1. Usar columnas `p{ancho}` (alineadas arriba) en lugar de `m{}` o `c`. La suma de anchos + 2\tabcolsep por columna ≤ `\linewidth`.
2. Poner `\small` al inicio de la tabla (o `\AtBeginEnvironment{longtable}{\small}` en preámbulo).
3. Para celdas con texto largo, usar `\multirow{n}{=}{texto}` (el `=` usa el ancho natural de la columna) en lugar de `\multirow{n}{*}{texto}`.
4. En `pgfplots`, reducir el ancho del eje con `width=0.85\linewidth` y `scale only axis` para que la etiqueta del eje Y no choque.
5. Añadir `\setlength{\emergencystretch}{3em}` en el preámbulo para dar tolerancia a la justificación.
6. Si persiste overfull, reducir ligeramente los anchos de columna o abreviar encabezados.
7. Comprobar en el log de LaTeX: «Overfull \hbox (XX pt too wide)».

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
