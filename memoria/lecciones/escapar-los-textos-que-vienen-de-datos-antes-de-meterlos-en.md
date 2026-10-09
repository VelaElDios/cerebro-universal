---
titulo: "Escapar los textos que vienen de datos antes de meterlos en LaTeX"
temas: ["latex", "lua", "datos"]
claves: ["Misplaced alignment tab", "escapar", "textbackslash", "Missing $ inserted"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]] · [[lua]] · [[datos]]

## Problema
Un `&`, `%`, `$`, `#`, `_`, `{`, `}`, `~`, `^` o `\` en un CSV rompe el documento o desaparece texto. Además, si se cambia `\` por `\textbackslash{}` y DESPUÉS se escapan las llaves, sale `\textbackslash\{\}`.

## Solución
Escapar todos esos caracteres en una función. La barra `\` se trata con un marcador temporal (o al final) para no volver a escapar sus llaves. Probar con datos raros a propósito.

## Ejemplo
```lua
local function escapar_latex(s)
  s = s:gsub("\\", "@@BARRA@@")                 -- 1) la barra, con un marcador
  s = s:gsub("([&%%$#_{}])", "\\%1")             -- 2) & % $ # _ { }
  s = s:gsub("~", "\\textasciitilde{}")
  s = s:gsub("%^", "\\textasciicircum{}")
  s = s:gsub("@@BARRA@@", "\\textbackslash{}")  -- 3) al final, para no escapar sus llaves
  return s
end
```

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
