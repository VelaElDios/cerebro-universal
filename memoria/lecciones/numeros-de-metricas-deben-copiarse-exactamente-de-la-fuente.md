---
titulo: "Números de métricas deben copiarse exactamente de la fuente única"
temas: ["latex", "verificacion", "metricas"]
claves: ["11.100", "4.350", "14.800", "5.050"]
estado: "propuesta"
veces: 1
fecha: "2026-11-03"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[verificacion]] · [[metricas]]

## Problema
En chapters/05-evaluacion.tex la tabla de métricas usaba valores ~11.100 (líneas juego) y ~4.350 (líneas pruebas) que no aparecen en documentacion-tecnica.md §14, donde dice ~14.800 y ~5.050. El test verificar.py rechaza cualquier número >20 que no esté en las fuentes.

## Solución
Antes de escribir cualquier cifra en la memoria, buscarla en las fuentes (documentacion-tecnica.md, gestion.md, revision-entrega.md) y copiarla tal cual. Si la fuente da un rango o aproximación, usar esa aproximación exacta.

## Ejemplo
"Líneas del motor del juego ... & ~14.800 \\\\" (fuente: documentacion-tecnica.md §14: "Líneas del motor del juego ... ~14.800")

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
