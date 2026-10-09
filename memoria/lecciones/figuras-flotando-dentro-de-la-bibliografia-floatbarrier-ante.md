---
titulo: "Figuras flotando dentro de la bibliografía: \\FloatBarrier antes"
temas: ["latex"]
claves: ["bibliografía", "printbibliography", "figura", "FloatBarrier", "placeins"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]]

## Problema
Una figura flotante pendiente acaba colocándose en medio de la bibliografía.

## Solución
Cargar `placeins` y poner `\FloatBarrier` justo antes de la bibliografía: obliga a colocar antes todas las figuras pendientes.

## Ejemplo
```latex
\usepackage{placeins}
...
\FloatBarrier
\printbibliography
```

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
