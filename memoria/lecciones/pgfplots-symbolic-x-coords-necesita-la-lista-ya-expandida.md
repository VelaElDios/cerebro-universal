---
titulo: "pgfplots: symbolic x coords necesita la lista ya expandida"
temas: ["latex", "tikz", "pgfplots"]
claves: ["symbolic x coords", "pgfplots", "expanded", "Package pgfplots Error"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]] · [[tikz]] · [[pgfplots]]

## Problema
Si la lista de coordenadas simbólicas sale de una macro o de Lua, pgfplots la recibe sin expandir y falla.

## Solución
Construir la lista en una macro con `\edef` y pasarla con `/.expanded`.

## Ejemplo
```latex
\edef\usuarios{\directlua{sus.lista_usuarios()}}
\begin{axis}[symbolic x coords/.expanded=\usuarios, xtick=data]
```

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
