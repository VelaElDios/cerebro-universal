---
titulo: "Con babel en español, TikZ necesita \\usetikzlibrary{babel}"
temas: ["latex", "tikz"]
claves: ["babel", "stealth", "spanish", "Missing number", "ifdim", "Argument of"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]] · [[tikz]]

## Problema
Babel `spanish` vuelve activos los caracteres `<` y `>`. Entonces fallan `>=stealth`, las flechas `->` y las comparaciones `\ifdim ... >` dentro de figuras TikZ y pgfplots.

## Solución
Cargar la librería `babel` de TikZ en el preámbulo.

## Ejemplo
```latex
\usepackage[spanish]{babel}
\usepackage{tikz}
\usetikzlibrary{babel}
```

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
