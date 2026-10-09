---
titulo: "Al reescribir un archivo, conservar todo lo que ya funcionaba"
temas: ["general"]
claves: ["attempt to call a nil value", "nil value", "undefined", "is not defined", "NameError", "AttributeError"]
estado: "confirmada"
veces: 1
fecha: "2026-10-08"
proyectos: ["plantilla-sus"]
---

Temas: [[general]]

## Problema
Las IAs escriben archivos COMPLETOS y, al rehacer uno grande, a veces se dejan funciones que ya existían (pasó dos veces con `get_stat_raw` en `sus-calculos.lua`): luego todo lo que las usaba deja de compilar.

## Solución
Antes de reescribir un archivo, mirar qué funciones/secciones tiene y mantenerlas todas. Si un error dice que algo no existe, comprobar primero si se borró en un paso anterior.

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
