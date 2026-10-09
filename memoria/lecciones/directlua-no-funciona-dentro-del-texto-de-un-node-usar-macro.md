---
titulo: "\\directlua no funciona dentro del texto de un \\node: usar macros"
temas: ["latex", "lua", "tikz"]
claves: ["\\node", "directlua", "pgfmathsetmacro", "edef"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]] · [[lua]] · [[tikz]]

## Problema
Un `\directlua{...}` dentro del texto de un `\node` de TikZ falla. En cambio, dentro de `\edef` o de `\pgfmathsetmacro` SÍ funciona.

## Solución
Calcular el valor antes en una macro y usar la macro en el nodo.

## Ejemplo
```latex
\edef\media{\directlua{sus.get_stat("media", 1)}}
\node at (0,0) {\media};
```

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
