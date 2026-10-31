---
titulo: "Números en diagramas de secuencia deben coincidir con la especificación"
temas: ["latex", "pgf-umlsd", "secuencia"]
claves: ["422", "400", "fig:sec-partida"]
estado: "propuesta"
veces: 1
fecha: "2026-10-31"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[pgf-umlsd]] · [[secuencia]]

## Problema
En el diagrama de secuencia fig:sec-partida se usó el código de estado 422 para «resultado imposible», pero la documentación técnica (§7.10) especifica 400. El test de verificación detecta números no presentes en las fuentes.

## Solución
Al escribir diagramas de secuencia, copiar los códigos de estado exactos de la documentación técnica (documentacion-tecnica.md §7.10 y §7.11). Si la fuente dice 400, usar 400; si dice 409, usar 409. No inventar códigos.

## Ejemplo
En el diagrama, la línea \begin{call}{api}{finalizarPartida}{srv}{200 o 400} debe reflejar los códigos reales.

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
