---
titulo: "Nombres de archivo normales: sin espacios y con extensión"
temas: ["general"]
claves: ["Nombre de archivo no válido", "borrado de archivos temporales"]
estado: "confirmada"
veces: 1
fecha: "2026-10-08"
proyectos: ["plantilla-sus"]
---

Temas: [[general]]

## Problema
Un constructor creó un archivo llamado «- borrado de archivos temporales» en vez de borrar archivos.

## Solución
Para borrar se usa `<<<BORRAR ruta>>>`. Los archivos nuevos llevan nombres sin espacios, que empiezan por letra o número y tienen extensión (`.tex`, `.py`...). El orquestador rechaza los demás.

Origen: [[proyectos/plantilla-sus/bitacora|plantilla-sus]]
