---
titulo: "pgfplots: línea horizontal de referencia de lado a lado con \\draw"
temas: ["latex", "tikz", "pgfplots"]
claves: ["línea de referencia", "addplot", "barras punteadas", "rel axis cs"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]] · [[tikz]] · [[pgfplots]]

## Problema
Una línea de referencia (p. ej. el 68 del SUS) hecha con `\addplot` en un gráfico de barras sale como barras punteadas, no como una línea.

## Solución
Dibujarla con `\draw` usando `rel axis cs` para ir de un borde del eje al otro.

## Ejemplo
```latex
\draw[dashed, red] ({rel axis cs:0,0} |- {axis cs:U1,68}) -- ({rel axis cs:1,0} |- {axis cs:U1,68});
```

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
