---
titulo: "En un .tex los comentarios son con %, no con --"
temas: ["latex", "lua"]
claves: ["comentario", "texto impreso", "aparece en el pdf"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]] · [[lua]]

## Problema
Las IAs que escriben mucho Lua ponen comentarios `-- ...` en archivos `.tex`: LaTeX los imprime como texto (con guiones).

## Solución
En archivos `.tex` los comentarios empiezan por `%`. `--` solo en archivos `.lua`.

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
