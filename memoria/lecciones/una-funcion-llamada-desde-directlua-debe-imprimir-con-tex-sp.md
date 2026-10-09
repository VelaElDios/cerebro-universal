---
titulo: "Una función llamada desde \\directlua debe imprimir con tex.sprint, no con return"
temas: ["latex", "lua"]
claves: ["tex.sprint", "return ", "no aparece"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]] · [[lua]]

## Problema
Lo que devuelve una función con `return` dentro de `\directlua` se pierde: en el documento no sale nada. El revisor reescribió `get_stat` con `return` y los valores desaparecieron.

## Solución
Para que el valor aparezca en el documento, la función lo escribe con `tex.sprint(...)`.

## Ejemplo
```lua
function M.get_stat(nombre, decimales)
  tex.sprint(string.format("%." .. decimales .. "f", stats[nombre]))
end
```

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
