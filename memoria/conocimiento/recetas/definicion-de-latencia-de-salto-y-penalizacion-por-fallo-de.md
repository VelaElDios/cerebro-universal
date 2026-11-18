---
tipo: "receta"
titulo: "Definición de latencia de salto y penalización por fallo de predicción"
temas: ["ac", "latencia", "pipeline", "prediccion-saltos"]
claves: ["branch latency", "miss penalty", "branch direction", "target address"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[latencia]] · [[pipeline]] · [[prediccion-saltos]]

La latencia de un salto es el número de ciclos extra entre la etapa IF (fetch) y el ciclo en que el salto se resuelve (se conoce dirección y destino). La penalización por fallo de predicción depende tanto de la etapa donde se conoce la dirección del salto (tomado/no tomado) como de la etapa donde se conoce la dirección destino (target address). Si se resuelven en etapas distintas, la penalización es el máximo de ambas distancias desde IF.

> Assuming a conditional branch, the miss penalty in the prediction depends on a) y b) are true.
> — `repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)` (cita sin comprobar)
