---
tipo: "concepto"
titulo: "Trace scheduling: traza = secuencia más probable de bloques básicos en código con estructura condicional"
temas: ["ac", "planificacion", "trace-scheduling"]
claves: ["trace scheduling", "traza", "bloques basicos", "estructura condicional"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[planificacion]] · [[trace-scheduling]]

El trace scheduling identifica la traza (trace) como la secuencia de bloques básicos más probable de ejecutarse en una estructura condicional (if-then-else, bucles con salidas), y optimiza esa traza como si fuera código lineal, moviendo instrucciones entre bloques y añadiendo código de compensación (compensation code) en las entradas/salidas laterales.

> In the trace scheduling technique, a trace is the most likely sequence of… d) Basic blocks in a code with a conditional structure
> — `repo:datos/temarios/AC/examenes/January2019.pdf` (cita sin comprobar)
