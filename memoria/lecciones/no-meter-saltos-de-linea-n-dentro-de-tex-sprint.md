---
titulo: "No meter saltos de línea \\n dentro de tex.sprint"
temas: ["latex", "lua"]
claves: ["tex.sprint", "Paragraph ended", "Runaway argument"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]] · [[lua]]

## Problema
Un `\n` dentro de la cadena de `tex.sprint` rompe la compilación (el ejemplo de cálculo de U1 no compilaba).

## Solución
Usar `tex.print` una vez por línea (cada llamada es una línea nueva), o separar párrafos con `\par`.

## Ejemplo
```lua
tex.print("Primera línea")
tex.print("\\par Segunda línea")
```

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
