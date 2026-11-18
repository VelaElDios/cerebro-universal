---
tipo: "receta"
titulo: "Aplicación de la ley de Amdahl para calcular fracción de tiempo necesaria para un speedup objetivo"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["speedup", "unidad punto flotante", "fracción tiempo", "aceleración"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Speedup_global = 1 / [(1-f) + f/k], donde f = fracción de tiempo en FP, k = aceleración FP (4×). Despejando f para speedup=2: 2 = 1/[(1-f)+f/4] → (1-f)+f/4 = 0,5 → 1 - 0,75f = 0,5 → f = 0,5/0,75 = 2/3 ≈ 66,6 s (opción b).

> We want to get a speedup of 2 for the benchmark we are considering. If the execution time of this benchmark in the old floating-point hardware is 100 seconds, how much of that initial execution time should the floating-point instructions count to get this speedup?
> — `repo:datos/temarios/AC/examenes/January2021.pdf`
