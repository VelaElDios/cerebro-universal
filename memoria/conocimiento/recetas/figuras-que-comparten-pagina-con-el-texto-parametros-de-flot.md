---
tipo: "receta"
titulo: "Figuras que comparten página con el texto (parámetros de flotantes)"
temas: ["figuras", "latex", "tfg"]
claves: ["floatpagefraction", "topfraction", "textfraction", "height=0.42\\textheight"]
proyectos: ["memoria-procesos"]
fuentes: ["include/extra.tex (memoria del Sprint 1)"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[figuras]] · [[latex]] · [[tfg]]

LaTeX manda una figura a una página propia cuando no cabe con el texto. Para evitar páginas con una sola imagen:

```latex
\renewcommand{\topfraction}{0.85}
\renewcommand{\bottomfraction}{0.6}
\renewcommand{\textfraction}{0.12}
\renewcommand{\floatpagefraction}{0.8}
\setcounter{topnumber}{3}
\setcounter{totalnumber}{4}
```

Y las capturas, como mucho a `height=0.42\textheight,keepaspectratio`. Los diagramas grandes van dentro de `\begin{adjustbox}{max width=\textwidth,max totalheight=0.6\textheight}`.

> Figuras y tablas: que compartan página con el texto en vez de quedarse solas
> — `include/extra.tex (memoria del Sprint 1)`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
