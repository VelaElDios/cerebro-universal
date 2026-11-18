---
tipo: "concepto"
titulo: "Planificación dinámica sin especulación: emisión en orden, ejecución y finalización fuera de orden"
temas: ["ac", "especulación", "planificación dinámica", "superscalar"]
claves: ["dynamic scheduling", "in-order issue", "out-of-order execution", "out-of-order completion", "no speculation"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulación]] · [[planificación dinámica]] · [[superscalar]]

Planificación dinámica **sin especulación** (ej. Scoreboard, Tomasulo original):
- Emisión (issue): **en orden** (respeta dependencias WAR/WAW).
- Ejecución: **fuera de orden** (cuando operandos listos).
- Finalización (completion/write-back): **fuera de orden** (cuando termina ejecución).
La especulación añade commit en orden (ROB) para permitir recuperación ante fallos.

> Mark the correct option for dynamic instruction scheduling without speculation: Issue in order, execution out of order and completion out of order.
> — `repo:datos/temarios/AC/examenes/June2023.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[planificacion-dinamica-sin-especulacion-orden-de-ejecucion-d]] · [[planificacion-dinamica-orden-de-ejecucion-por-disponibilidad]] · [[planificacion-dinamica-tomasulo-orden-de-ejecucion-por-dispo]]
