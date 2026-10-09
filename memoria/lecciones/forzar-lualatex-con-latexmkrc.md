---
titulo: "Forzar LuaLaTeX con latexmkrc"
temas: ["latex", "overleaf"]
claves: ["latexmkrc", "pdf_mode", "lualatex", "Overleaf", "compilador"]
estado: "confirmada"
veces: 1
fecha: "2026-10-08"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]] · [[overleaf]]

## Problema
Si el proyecto usa `\directlua` y se compila con pdfLaTeX (lo normal por defecto, p. ej. en Overleaf o LaTeX Workshop), falla.

## Solución
Poner un archivo `latexmkrc` junto al `.tex` principal con `$pdf_mode = 4;` (4 = LuaLaTeX). Overleaf gratis da timeout con Biber en documentos pesados: hay que ofrecer una versión sin Biber.

## Ejemplo
```perl
$pdf_mode = 4;
```

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
