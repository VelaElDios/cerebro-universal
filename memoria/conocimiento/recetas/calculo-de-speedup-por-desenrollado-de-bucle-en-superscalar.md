---
tipo: "receta"
titulo: "Cálculo de speedup por desenrollado de bucle en superscalar"
temas: ["ac", "pipeline", "superscalar"]
claves: ["loop unrolling", "speedup", "superscalar", "CPI", "iteraciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]]

Speedup = (Tiempo original) / (Tiempo nuevo). Original: 5 iteraciones × 15 ciclos/iter = 75 ciclos. Nuevo: 5 iteraciones en 15 ciclos (gracias a desenrollado 5× y superscalar 4-way). Speedup = 75/15 = 5. La opción correcta es c) 5. Fórmula general: Speedup = (iteraciones × CPI_escalar) / (ciclos_superscalar_para_mismas_iteraciones).

> Each iteration of a given loop in a scalar processor requires 15 clock cycles to be issued. We unrolled such a loop 5 times and scheduled it for a 4-way superscalar obtaining that we now perform 5 iterations of the original loop in 15 cycles. What is the speedup obtained?
> — `repo:datos/temarios/AC/examenes/January2024.pdf`

Relacionado: [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]] · [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]] · [[calculo-de-speedup-por-desenrollado-de-bucle-en-superescalar]] · [[calculo-de-speedup-con-desenrollamiento-de-bucle-y-superesca]] · [[calculo-de-speedup-entre-bucle-original-y-desenrollado-en-vl]]
