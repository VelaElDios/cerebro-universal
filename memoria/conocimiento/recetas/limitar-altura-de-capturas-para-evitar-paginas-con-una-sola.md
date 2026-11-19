---
tipo: "receta"
titulo: "Limitar altura de capturas para evitar páginas con una sola imagen"
temas: ["figuras", "latex", "maquetacion"]
claves: ["adjustbox", "max totalheight", "0.42\\textheight", "regla 8"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[figuras]] · [[latex]] · [[maquetacion]]

Para capturas altas (gráficas de DoneTonic, capturas de CI/CD), envolver en `adjustbox{max totalheight=0.42\textheight,width=...}` en lugar de solo `height=0.42\textheight,keepaspectratio`. Esto permite que la figura comparta página con texto. Para diagramas TikZ/pgfplots grandes, usar `\begin{adjustbox}{max width=\linewidth,max totalheight=0.6\textheight}...\end{adjustbox}`. Relajar parámetros de flotantes: `\renewcommand{\topfraction}{0.85}`, `\renewcommand{\textfraction}{0.12}`, `\setcounter{totalnumber}{4}`.

> capturas como mucho a `height=0.42\textheight`; diagramas grandes con `max totalheight`; figuras `[htbp]` con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
