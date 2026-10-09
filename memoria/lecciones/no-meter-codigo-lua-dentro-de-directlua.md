---
titulo: "No meter código Lua dentro de \\directlua"
temas: ["latex", "lua"]
claves: ["directlua", "unexpected symbol", "'=' expected", "malformed number", "unfinished string"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]] · [[lua]]

## Problema
TeX procesa el texto de `\directlua{...}` antes que Lua: convierte `#` en `##`, se come lo que va tras `%`, expande las `\macros` y junta las líneas en una sola (un comentario `--` se traga el resto). Por eso `local`, `function`, `if`, `for` o cadenas con `\` dentro de `\directlua` rompen la compilación. Fue el error más repetido del proyecto (pasos 3 a 6 sin compilar).

## Solución
Todo el código Lua va en un archivo `.lua` aparte. En el `.tex` solo llamadas simples a funciones de ese archivo.

## Ejemplo
```latex
\directlua{sus = dofile("sus-calculos.lua")}
\directlua{sus.get_stat("media", 1)}
```

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
