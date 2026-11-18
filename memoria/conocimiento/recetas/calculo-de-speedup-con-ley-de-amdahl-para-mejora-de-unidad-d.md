---
tipo: "receta"
titulo: "Cálculo de speedup con ley de Amdahl para mejora de unidad de punto flotante (pregunta 3)"
temas: ["ac", "amdahl", "pipeline", "rendimiento"]
claves: ["speedup", "punto flotante", "4 veces más rápido", "100 segundos", "ley de Amdahl"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[amdahl]] · [[pipeline]] · [[rendimiento]]

Aplicar ley de Amdahl: Speedup_global = 1 / ((1 - f) + f/k), donde f = fracción de tiempo en FP original, k = 4 (mejora FP). Queremos Speedup_global = 5. Despejar f: 5 = 1 / ((1-f) + f/4) → (1-f) + f/4 = 0.2 → 1 - 0.75f = 0.2 → 0.75f = 0.8 → f = 1.066... > 1. Imposible. Respuesta correcta: c) It is not possible. La mejora máxima posible con k=4 es 4x (cuando f=1), no se puede alcanzar 5x.

> We are looking for a benchmark to measure the performance of the new floating-point unit, which is 4 times faster than the old one. We want to get a speedup of 5. If the benchmark we are considering takes 100 seconds using the old floating-point hardware, how much of the initial execution time should the floating-point instructions account for to achieve that speedup?
> — `repo:datos/temarios/AC/examenes/June2021.pdf`
