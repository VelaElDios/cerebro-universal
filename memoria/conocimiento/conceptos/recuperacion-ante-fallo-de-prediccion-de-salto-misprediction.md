---
tipo: "concepto"
titulo: "Recuperación ante fallo de predicción de salto (misprediction)"
temas: ["ac", "misprediction", "prediccion-saltos", "recovery"]
claves: ["mispredicted", "speculative results", "discard", "restart right path"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[misprediction]] · [[prediccion-saltos]] · [[recovery]]

Ante un fallo de predicción (misprediction), los resultados de las instrucciones ejecutadas **especulativamente por el camino erróneo deben descartarse** (flush del pipeline, limpieza de estaciones de reserva, ROB, etc.) y el procesador **reinicia la ejecución en el camino correcto** (fetch desde la dirección correcta). No se hacen permanentes los resultados especulativos ni se termina el programa.

> When a branch instruction is mispredicted… c) The results of the instructions executed speculatively must be discarded, and the program must be restarted along the right path.
> — `repo:datos/temarios/AC/examenes/January2018.pdf` (cita sin comprobar)
