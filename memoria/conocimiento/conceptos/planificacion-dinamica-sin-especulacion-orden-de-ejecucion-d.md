---
tipo: "concepto"
titulo: "Planificación dinámica sin especulación: orden de ejecución dado por dependencias de datos del programa"
temas: ["ac", "planificacion-dinamica", "tomasulo"]
claves: ["planificacion dinamica", "dependencias datos", "orden ejecucion"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[planificacion-dinamica]] · [[tomasulo]]

En planificación dinámica (p. ej., algoritmo de Tomasulo o Scoreboard), las instrucciones se emiten en orden pero se ejecutan fuera de orden tan pronto como sus operandos están listos; el orden real de ejecución lo dictan las dependencias de datos (RAW) reales, no el orden del programa ni el flujo de control.

> In dynamic scheduling techniques (without speculation), the order in which the execution step of different instruction is performed… c) is given by program data dependences
> — `repo:datos/temarios/AC/examenes/January2019.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[planificacion-dinamica-orden-de-ejecucion-por-disponibilidad]] · [[planificacion-dinamica-tomasulo-orden-de-ejecucion-por-dispo]] · [[planificacion-dinamica-sin-especulacion-emision-en-orden-eje]]
