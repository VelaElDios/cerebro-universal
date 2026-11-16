---
tipo: "receta"
titulo: "Corregir páginas con una sola imagen (Regla 8)"
temas: ["latex", "maquetacion", "reglas-tfg", "maquetación"]
claves: ["regla 8", "página sola imagen", "height", "subfigure"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[maquetacion]] · [[reglas-tfg]]

Para evitar páginas con una sola imagen:
1. Reducir `height` de las capturas a `0.42\textheight` como máximo (ya se usa `height=0.72\textheight` en el borrador, hay que bajarlo).
2. Añadir `keepaspectratio` para que no se deformen.
3. Agrupar capturas relacionadas en `subfigure` (dos por fila) para que ocupen menos alto.
4. Añadir texto explicativo antes/después de la figura para que la página no quede solo con la imagen.
5. Usar `[htbp]` en el entorno `figure` y relajar parámetros de flotantes (ya está en `include/extra.tex`: `\renewcommand{\topfraction}{0.85}`, etc.).
6. Para diagramas TikZ/pgfplots grandes, envolver en `\begin{adjustbox}{max width=\textwidth,max totalheight=0.6\textheight}`.

> Regla 8: Ninguna página con una sola imagen: capturas como mucho a `height=0.42\textheight`; diagramas grandes con `max totalheight`; figuras `[htbp]` con parámetros de flotantes relajados.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

## Ampliación (2026-11-16, memoria-procesos)
Para evitar páginas con una sola imagen y poco texto: 1) Reducir la altura de la imagen a `height=0.42\textheight,keepaspectratio`. 2) Agrupar imágenes relacionadas en una figura con `subfigure` (dos por fila). 3) Añadir texto explicativo antes/después de la figura para que la página no quede solo con la imagen. 4) Usar `[htbp]` y relajar parámetros de flotantes (ya configurados en `include/extra.tex` con `\renewcommand{\topfraction}{0.85}`, etc.) para que LaTeX pueda colocar la figura en la misma página que el texto.

## Ampliación (2026-11-16, memoria-procesos)
Para que las figuras compartan página con texto u otras figuras: (1) reducir altura de capturas a `height=0.42\textheight,keepaspectratio`; (2) agrupar capturas relacionadas en `subfigure` (dos por fila); (3) usar `[htbp]` en todas las figuras; (4) relajar parámetros de flotantes en el preámbulo: `\renewcommand{\topfraction}{0.85}`, `\renewcommand{\bottomfraction}{0.6}`, `\renewcommand{\textfraction}{0.12}`, `\renewcommand{\floatpagefraction}{0.8}`, `\setcounter{topnumber}{3}`, `\setcounter{totalnumber}{4}`. (5) Para diagramas TikZ/pgfplots grandes, envolver en `\begin{adjustbox}{max width=\textwidth,max totalheight=0.6\textheight}`. (6) Si una sección queda muy corta, fusionarla con la anterior o convertirla en lista.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
