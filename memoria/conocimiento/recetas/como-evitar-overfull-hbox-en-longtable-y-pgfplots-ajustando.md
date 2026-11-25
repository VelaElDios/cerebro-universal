---
tipo: "receta"
titulo: "Cómo evitar overfull hbox en longtable y pgfplots ajustando anchos de columna"
temas: ["latex", "longtable", "maquetacion", "overfull", "pgfplots"]
claves: ["L{...}", "p{...}", "width=0.85\\linewidth", "scale only axis", "ylabel style", "xshift"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/a1-desarrollo.tex (burndowns) y chapters/04-descripcion.tex (tabla RF)"]
confianza: "propuesto"
fecha: "2026-11-25"
actualizado: "2026-11-25"
---

Temas: [[latex]] · [[longtable]] · [[maquetacion]] · [[overfull]] · [[pgfplots]]

1. En `longtable`, usar columnas `L{...}` (que son `p{...}` alineadas arriba) y sumar anchos ≤ `\linewidth`. 2. En `pgfplots`, reducir `width` a `0.85\linewidth` o menos, activar `scale only axis`, y desplazar la etiqueta del eje Y con `ylabel style={anchor=east, xshift=-3pt}`. 3. Usar `\small` al inicio de `longtable` y `table` (`\AtBeginEnvironment{longtable}{\small}`). 4. `\renewcommand{\arraystretch}{1.15}` para aire entre filas. 5. `\setlength{\LTpre}{0pt}\setlength{\LTpost}{0pt}` para evitar espacio extra. 6. `\raggedbottom` global para que las páginas no intenten estirarse y fallen con "Infinite glue shrinkage" al partir longtables.

> Anchos que suman ≤ \linewidth (p. ej., 13,2 cm + 5 separadores = 15,31 cm ≤ 15,5 cm). En pgfplots: `width=0.85\linewidth`, `scale only axis`, `ylabel style={anchor=east, xshift=-3pt}` para que la etiqueta del eje Y no choque con la gráfica y no haya overfull hbox.
> — `chapters/a1-desarrollo.tex (burndowns) y chapters/04-descripcion.tex (tabla RF)` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
