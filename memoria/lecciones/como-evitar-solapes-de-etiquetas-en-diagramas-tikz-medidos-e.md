---
titulo: "Cómo evitar solapes de etiquetas en diagramas TikZ medidos en el PDF"
temas: ["latex", "tikz", "pgf-umlsd", "maquetacion"]
claves: ["revisar_maquetacion.py", "solape", "etiqueta", "línea discontinua", "above", "yshift"]
estado: "propuesta"
veces: 1
fecha: "2026-11-25"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[tikz]] · [[pgf-umlsd]] · [[maquetacion]]

## Problema
En el diagrama entidad-relación (fig:modelo-datos) la etiqueta 'userId' sobre la línea discontinua session→users era detectada como solape por la medición geométrica del PDF (reglas 16-18). Aumentar `yshift` no era suficiente ni robusto.

## Solución
Usar `above=<distancia>` en lugar de `anchor=south, yshift=<distancia>` para las etiquetas horizontales sobre flechas, y aumentar la distancia hasta que la medición del PDF no detecte intersección (p. ej., `above=50pt`). Aplicar la misma separación a etiquetas homólogas por consistencia.

## Ejemplo
|
  \draw[arrow, dashed] (session.east) -- node[rel, midway, above=50pt] {userId} (users.west);
  \draw[arrow] (users.east) -- node[rel, midway, above=50pt, align=center] {su\\club} (perfiles.west);

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
