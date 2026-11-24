---
tipo: "receta"
titulo: "Figuras que comparten página con el texto (parámetros de flotantes)"
temas: ["figuras", "latex", "tfg", "memoria"]
claves: ["floatpagefraction", "topfraction", "textfraction", "height=0.42\\textheight"]
proyectos: ["memoria-procesos"]
fuentes: ["include/extra.tex (memoria del Sprint 1)", "../../memoria/reglas-tfg.md"]
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

## Ampliación (2026-11-16, )
Para evitar páginas con una sola imagen:
- Capturas de pantalla: limitar altura a `height=0.42\textheight` (máximo 42% de la altura de texto).
- Diagramas grandes: usar `max totalheight` (requiere `graphicx` con `adjustbox` o similar) para que escalen si superan el espacio.
- Especificador de flotante `[htbp]` (here, top, bottom, page) en todas las figuras.
- Relajar parámetros internos de LaTeX para flotantes (p. ej. `\setcounter{topnumber}{3}`, `\setcounter{bottomnumber}{3}`, `\setcounter{totalnumber}{4}`, `\renewcommand{\topfraction}{0.9}`, `\renewcommand{\bottomfraction}{0.9}`, `\renewcommand{\textfraction}{0.1}`, `\renewcommand{\floatpagefraction}{0.8}`) para que LaTeX permita varias figuras y texto en la misma página.

Relacionado: [[figuras-ninguna-pagina-con-una-sola-imagen-limites-de-altura]] · [[limitar-altura-de-capturas-para-evitar-paginas-con-una-sola]] · [[arreglar-pagina-con-una-sola-imagen-regla-8-agrupando-en-sub]] · [[limitar-altura-de-capturas-para-evitar-paginas-con-una-sola]] · [[reglas-de-figuras-tamano-flotantes-y-nada-de-paginas-solas]] · [[figuras-sin-paginas-solas-ni-casi-vacias-limites-de-altura-y]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
