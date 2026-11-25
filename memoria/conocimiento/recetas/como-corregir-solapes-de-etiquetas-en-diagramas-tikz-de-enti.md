---
tipo: "receta"
titulo: "Cómo corregir solapes de etiquetas en diagramas TikZ de entidad-relación"
temas: ["latex", "maquetacion", "pgf-umlsd", "tikz"]
claves: ["revisar_maquetacion.py", "fig:modelo-datos", "etiqueta userId", "línea discontinua", "above", "yshift"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-25"
actualizado: "2026-11-25"
---

Temas: [[latex]] · [[maquetacion]] · [[pgf-umlsd]] · [[tikz]]

Cuando `revisar_maquetacion.py` detecta que una etiqueta de relación (p. ej., 'userId') queda sobre la línea en un diagrama entidad-relación TikZ, la solución es aumentar la separación vertical usando `above=<dimensión>` en el nodo de la etiqueta, en lugar de `anchor=south, yshift=<dimensión>`. La sintaxis `above` coloca el nodo por encima de la línea con el espacio indicado y es más robusta. Para líneas horizontales, `above=30pt` suele ser suficiente; para líneas verticales, usar `anchor=east, xshift=-18pt, pos=0.5` (o `left=18pt`). No se debe usar `resizebox`, `adjustbox` ni `scale` sobre el diagrama completo (reglas 16 y 19 de Javier).

> \draw[arrow, dashed] (session.east) -- node[rel, midway, above=30pt] {userId} (users.west);
> — `chapters/04-descripcion.tex` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
