---
tipo: "receta"
titulo: "Tablas de LaTeX que no se pisan (columnas p y addlinespace)"
temas: ["latex", "tablas", "tfg"]
claves: ["newcolumntype", "m{", "p{", "addlinespace", "arraystretch", "longtable"]
proyectos: ["memoria-procesos"]
fuentes: ["include/extra.tex (memoria del Sprint 1)"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[tablas]] · [[tfg]]

Con columnas `m{}` las filas de varias líneas se descuadran y parecen montarse unas sobre otras. Arreglo en `include/extra.tex`:

```latex
\usepackage{etoolbox}
\newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}p{#1}}
\newcolumntype{C}[1]{>{\centering\let\newline\\\arraybackslash\hspace{0pt}}p{#1}}
\newcolumntype{R}[1]{>{\raggedleft\let\newline\\\arraybackslash\hspace{0pt}}p{#1}}
\renewcommand{\arraystretch}{1.15}
\AtBeginEnvironment{longtable}{\small}
\AtBeginEnvironment{table}{\small}
```

Además, cada fila del cuerpo termina en `\\ \addlinespace[3pt]`. Los anchos suman como mucho `\linewidth` y las columnas cortas (Id, Hito) tienen que caber sin partirse: `RNF-01` necesita unos 1,3 cm.

> Celdas alineadas arriba (p) en vez de centradas en vertical (m): las filas ya no se pisan
> — `include/extra.tex (memoria del Sprint 1)`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
