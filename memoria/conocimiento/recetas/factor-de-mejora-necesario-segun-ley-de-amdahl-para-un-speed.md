---
tipo: "receta"
titulo: "Factor de mejora necesario según ley de Amdahl para un speedup global dado"
temas: ["ac", "ley-amdahl", "rendimiento"]
claves: ["speedup", "enhancement factor", "floating point", "Amdahl"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ley-amdahl]] · [[rendimiento]]

Speedup_global = 1 / [(1 - f) + f/k], donde f = fracción mejorada (0.7), speedup_global = 1.4. Despejar k: 1.4 = 1 / [0.3 + 0.7/k] → 0.3 + 0.7/k = 1/1.4 ≈ 0.7143 → 0.7/k = 0.4143 → k ≈ 1.69. Opción b).

> We want to obtain a speedup of 40% for this test program, by improving the execution of floating point instructions. Then, the factor of enhancement for this part of the computer should be, approximately
> — `repo:datos/temarios/AC/examenes/January2016.pdf`
