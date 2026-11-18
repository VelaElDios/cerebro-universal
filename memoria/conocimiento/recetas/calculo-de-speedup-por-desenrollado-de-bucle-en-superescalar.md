---
tipo: "receta"
titulo: "Cálculo de speedup por desenrollado de bucle en superescalar grado 2"
temas: ["ac", "pipeline"]
claves: ["loop unrolling", "superscalar", "speedup", "CPI", "cycles per iteration"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]]

Speedup = (Tiempo original) / (Tiempo nuevo). Original: 1 iteración = 10 ciclos. Desenrollado 3x: el bucle modificado procesa 3 iteraciones originales en 15 ciclos => 5 ciclos por iteración original. Speedup = 10 / 5 = 2. Opción correcta: (d) 2.

> Each iteration of a specific loop requires 10 clock cycles on a scalar processor. We unrolled that loop 3 times and scheduled it for a grade 2 superscalar. Each iteration of the modified loop requires 15 cycles on the superscalar. We have obtained a speedup of:
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`

Relacionado: [[calculo-de-speedup-por-desenrollado-de-bucle-en-superscalar]] · [[calculo-de-speedup-con-desenrollamiento-de-bucle-y-superesca]] · [[metodo-para-calcular-speedup-de-bucle-desenrollado-y-planifi]]
