---
tipo: "dato"
titulo: "Suposiciones del problema: forwarding, ramas retrasadas, unidades totalmente segmentadas, CPI base=1"
temas: ["ac", "pipeline", "suposiciones"]
claves: ["forwarding", "delayed branches", "fully pipelined", "CPI=1", "frecuencia saltos 15%"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[suposiciones]]

Suposiciones clave: 1) Forwarding activo (resultados disponibles tan pronto como se producen). 2) Ramas retrasadas (delayed branches): la instrucción tras BNE se ejecuta siempre. 3) Unidades funcionales totalmente segmentadas (nuevas operaciones cada ciclo). 4) Instrucciones no en tabla de latencias → latencia 0. 5) Para cálculo de speedup en pregunta anterior (no mostrada): penalización 4 ciclos por fallo predicción, frecuencia saltos 15%, CPI = 1 + 4*penalty*mispred_rate.

> It is assumed that there are forwarding and delayed branches. All functional units are fully pipelined. Some instructions have latencies expressed in the following table when executed consecutively (assume that instructions not listed in this table have no latency)
> — `repo:datos/temarios/AC/examenes/June 2024.pdf` (cita sin comprobar)
