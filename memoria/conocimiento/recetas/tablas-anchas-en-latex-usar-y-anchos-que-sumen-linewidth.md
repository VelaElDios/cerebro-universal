---
tipo: "receta"
titulo: "Tablas anchas en LaTeX: usar @{} y anchos que sumen ≤ \\linewidth"
temas: ["latex", "longtable", "tablas"]
claves: ["overfull", "\\linewidth", "@{}", "L{}", "p{}", "longtable"]
proyectos: ["memoria-procesos"]
fuentes: ["lecciones del cerebro (memoria-procesos)"]
confianza: "propuesto"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[latex]] · [[longtable]] · [[tablas]]

Usar @{}L{...}@{} en la definición de la tabla (o @{} al inicio y final del preámbulo tabular) para eliminar el padding lateral, y reducir anchos de columna para que la suma sea ≤ \linewidth (p.ej., 13–14cm). Alternativamente, envolver en \begin{adjustwidth}{-1cm}{-1cm} o usar \small/\footnotesize. Ejemplo: \begin{tabular}{@{}L{1.5cm} L{8.0cm} L{3.5cm}@{}} ... \end{tabular}

> Las tablas con columnas L{...} sumaban más de \linewidth (≈15.5cm en esta plantilla), causando desbordamiento horizontal. El paquete array con L{...} añade padding lateral que suma al ancho total.
> — `lecciones del cerebro (memoria-procesos)` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
