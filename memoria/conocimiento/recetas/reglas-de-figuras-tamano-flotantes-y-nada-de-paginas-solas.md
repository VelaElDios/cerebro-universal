---
tipo: "receta"
titulo: "Reglas de figuras y páginas: tamaños, flotantes, duplicados, flechas y páginas casi vacías"
temas: ["figuras", "latex", "memoria", "tfg"]
claves: ["height=0.42\\textheight", "max totalheight", "htbp", "subfigure", "ref", "max totaltotalheight", "rightarrow"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-21"
actualizado: "2026-11-23"
---

Temas: [[figuras]] · [[latex]] · [[memoria]] · [[tfg]]

Temas: [[figuras]] · [[latex]] · [[memoria]] · [[tfg]]

Directrices para evitar páginas con una sola imagen o casi vacías:

1. **Capturas de pantalla**: altura máxima `height=0.42\textheight`.
2. **Diagramas grandes**: usar `max totalheight` para limitar la altura total.
3. **Flotantes** con `[htbp]` y parámetros relajados (`\setcounter{topnumber}{...}`, `\renewcommand{\topfraction}{...}`, etc.) para que floten y compartan página con texto u otras figuras.
4. **No páginas casi vacías ni secciones de 1–2 líneas**: fusionarlas o convertirlas en lista.
5. **No figuras repetidas**: si una imagen ya existe en otro lugar, usar `\ref` a la figura original.
6. **Flechas reales** en captions y texto: `$\rightarrow$` (nunca `->`).
7. **Agrupar capturas relacionadas** con `subfigure`.

> **Ninguna página con una sola imagen:** capturas como mucho a `height=0.42\textheight`; diagramas grandes con `max totalheight`; figuras `[htbp]` con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[reglas-de-figuras-tamano-flotantes-y-nada-de-paginas-solas]] · [[figuras-ninguna-pagina-con-una-sola-imagen-limites-de-altura]] · [[como-evitar-paginas-con-una-sola-imagen-regla-8-de-javier]] · [[limitar-altura-de-capturas-para-evitar-paginas-con-una-sola]] · [[arreglar-pagina-con-una-sola-imagen-regla-8-agrupando-en-sub]] · [[reglas-de-figuras-tamano-flotantes-y-nada-de-paginas-solas]]

> **Ninguna página con una sola imagen:** - capturas como mucho a `height=0.42\textheight`; - diagramas grandes con `max totalheight`; - figuras `[htbp]` con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
> — `../../memoria/reglas-tfg.md`

Fusionada con: Reglas de figuras y páginas (tamaños, flotantes, duplicados, flechas)
