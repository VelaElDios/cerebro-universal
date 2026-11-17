---
tipo: "decision"
titulo: "Figuras: ninguna página con una sola imagen (límites de altura y flotantes relajados)"
temas: ["figuras", "latex", "memoria", "tfg"]
claves: ["height=0.42\\textheight", "max totalheight", "htbp", "flotantes relajados"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[figuras]] · [[latex]] · [[memoria]] · [[tfg]]

1) Capturas de pantalla: `height=0.42\textheight` máximo. 2) Diagramas grandes: usar `max totalheight` (requiere `graphicx` con `keepaspectratio`). 3) Especificador de flotante `[htbp]` y relajar parámetros de flotantes (p. ej., `\setcounter{topnumber}{3}`, `\renewcommand{\topfraction}{0.9}`, etc.) para que LaTeX permita varias figuras + texto en la misma página.

> Ninguna página con una sola imagen: capturas como mucho a `height=0.42\textheight`; diagramas grandes con `max totalheight`; figuras `[htbp]` con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
> — `../../memoria/reglas-tfg.md` (cita sin comprobar)
