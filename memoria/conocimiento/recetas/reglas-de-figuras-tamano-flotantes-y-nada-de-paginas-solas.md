---
tipo: "receta"
titulo: "Reglas de figuras: tamaño, flotantes y nada de páginas solas"
temas: ["latex", "memoria", "tfg"]
claves: ["height=0.42\\textheight", "max totalheight", "htbp", "subfigure", "ref"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-21"
actualizado: "2026-11-22"
---

Temas: [[latex]] · [[memoria]] · [[tfg]]

Directrices para evitar páginas con una sola imagen o casi vacías:
- Capturas de pantalla: `height=0.42\textheight` como máximo.
- Diagramas grandes: usar `max totalheight` para limitar altura total.
- Flotantes con `[htbp]` y parámetros relajados (`\setcounter{topnumber}{...}`, `\renewcommand{\topfraction}{...}`, etc.) para que floten y compartan página con texto u otras figuras.
- Si varias capturas van juntas, agruparlas con `subfigure`.
- Si una imagen ya existe en otro lugar, no repetirla: usar `\ref` a la figura original.
- Flechas en captions y texto: `$\rightarrow$` (nunca `->`).

> **Ninguna página con una sola imagen:** - capturas como mucho a `height=0.42\textheight`; - diagramas grandes con `max totalheight`; - figuras `[htbp]` con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[reglas-de-figuras-y-paginas-tamanos-flotantes-duplicados-fle]] · [[figuras-ninguna-pagina-con-una-sola-imagen-limites-de-altura]] · [[como-evitar-paginas-con-una-sola-imagen-regla-8-de-javier]]
