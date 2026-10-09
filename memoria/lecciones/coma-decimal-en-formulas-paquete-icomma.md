---
titulo: "Coma decimal en fórmulas: paquete icomma"
temas: ["latex"]
claves: ["icomma", "coma decimal", "30, 28", "espacio tras la coma"]
estado: "confirmada"
veces: 1
fecha: "2026-10-05"
proyectos: ["plantilla-sus"]
---

Temas: [[latex]]

## Problema
En modo matemático `30,28` sale como `30, 28` (con espacio), porque la coma se trata como puntuación.

## Solución
Cargar `\usepackage{icomma}`: la coma seguida de un dígito no lleva espacio. Y para escribir decimales desde Lua, usar una función que cambie el punto por coma (en español no vale `38.8`).

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
