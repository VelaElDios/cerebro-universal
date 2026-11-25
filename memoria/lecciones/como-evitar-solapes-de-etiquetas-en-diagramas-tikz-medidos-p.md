---
titulo: "Cómo evitar solapes de etiquetas en diagramas TikZ medidos por revisar_maquetacion.py"
temas: ["latex", "tikz", "pgf-umlsd", "maquetacion"]
claves: ["revisar_maquetacion.py", "solape", "etiqueta", "above", "yshift", "node distance"]
estado: "propuesta"
veces: 1
fecha: "2026-11-25"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[tikz]] · [[pgf-umlsd]] · [[maquetacion]]

## Problema
Las etiquetas colocadas con `above=32pt` sobre líneas horizontales en diagramas TikZ (entity-relationship) seguían siendo detectadas como solapadas por la medición geométrica del PDF (reglas 16-18 de Javier). La medición usa coordenadas reales del PDF y detecta si una línea cruza la caja del texto.

## Solución
Aumentar la separación vertical a `above=50pt` (o más) para garantizar que la línea quede claramente por debajo de la caja del texto. Usar `above` en lugar de `anchor=south, yshift` porque es más robusto y legible. Verificar siempre con `revisar_maquetacion.py` tras cada ajuste.

## Ejemplo
|
  \draw[arrow, dashed] (session.east) -- node[rel, midway, above=50pt] {userId} (users.west);
  \draw[arrow] (users.east) -- node[rel, midway, above=50pt, align=center] {su\\club} (perfiles.west);

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
