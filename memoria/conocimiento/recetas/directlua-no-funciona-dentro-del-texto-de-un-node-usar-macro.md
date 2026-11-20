---
tipo: "receta"
titulo: "\\directlua no funciona dentro del texto de un \\node: usar macros"
temas: ["directlua", "latex", "lua", "node", "tikz"]
claves: ["directlua", "node", "tikz", "macro", "edef"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/lecciones.md", "chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-20"
---

Temas: [[directlua]] · [[latex]] · [[lua]] · [[node]] · [[tikz]]

Un \directlua{...} dentro del texto de un \node de TikZ falla. En cambio, dentro de \edef o de \pgfmathsetmacro SÍ funciona. Solución: \edef\media{\directlua{sus.get_stat("media", 1)}}\node at (0,0) {\media};. Esto permite usar valores calculados en Lua dentro de nodos TikZ.

> Calcular el valor antes en una macro y usar la macro en el nodo.
> — `memoria/lecciones.md` (cita sin comprobar)

Relacionado: [[arquitectura-de-calculos-en-lualatex-para-plantilla-sus]] · [[trampas-tecnicas-comprobadas-en-lualatex-evitar-errores-de-c]] · [[dentro-de-cajas-no-se-parten-palabras-ni-rutas-text-width-ma]] · [[diagrama-tikz-ancho-reducir-text-width-y-offsets-para-caber]]

## Ampliación (2026-11-20, memoria-procesos)
Un `\directlua{...}` dentro del texto de un `\node` de TikZ falla. En cambio, dentro de `\edef` o de `\pgfmathsetmacro` SÍ funciona. Calcular el valor antes en una macro y usar la macro en el nodo.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
