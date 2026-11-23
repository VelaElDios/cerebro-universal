---
tipo: "receta"
titulo: "Figuras sin páginas solas ni casi vacías: límites de altura y flotantes relajados"
temas: ["latex", "memoria", "tfg"]
claves: ["height", "textheight", "totalheight", "htbp", "subfigure", "ref"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[memoria]] · [[tfg]]

- Capturas de pantalla: `height=0.42\textheight` como máximo.
- Diagramas grandes: usar `max totalheight` (requiere `adjustbox` o `graphicx` con `keepaspectratio`).
- Flotantes `[htbp]` con parámetros relajados (`\setcounter{topnumber}{...}`, `\renewcommand{\topfraction}{...}`, etc.) para que LaTeX mezque figuras y texto.
- Agrupar capturas relacionadas con `subfigure` (una sola figura con sub-figuras).
- Si la misma imagen sirve en otro sitio: `\ref{fig:etiqueta}` en lugar de repetirla.
- Evitar páginas con una sola sección/línea: fusionar secciones cortas o convertirlas en lista.

> Ninguna página con una sola imagen: capturas como mucho a `height=0.42\textheight`; diagramas grandes con `max totalheight`; figuras `[htbp]` con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
> — `../../memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[reglas-de-maquetacion-de-javier-resumen-accionable]] · [[prosa-de-tfg-sin-listas-de-capturas-regla-13-javier]]
