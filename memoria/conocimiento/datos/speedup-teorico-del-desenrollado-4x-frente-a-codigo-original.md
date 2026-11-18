---
tipo: "dato"
titulo: "Speedup teórico del desenrollado 4x frente a código original (fórmula)"
temas: ["ac", "performance-analysis", "pipeline", "speedup"]
claves: ["speedup", "unrolled", "original", "cycles per iteration"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[performance-analysis]] · [[pipeline]] · [[speedup]]

Speedup = (Ciclos_totales_original_4_iteraciones) / (Ciclos_totales_desenrollado_planificado_4_iteraciones). Ciclos_totales_original_4_iteraciones = 4 × CPI_original (p.ej. 4 × 7 = 28 ciclos). Ciclos_totales_desenrollado_planificado = número de filas de la tabla de planificación (ciclos desde primera emisión hasta última emisión útil). El speedup mide la mejora por ocultación de latencias y mayor paralelismo a nivel de instrucción.

> Compute the speedup for the unrolled and scheduled version with respect the original code.
> — `repo:datos/temarios/AC/examenes/June2018.pdf`

Relacionado: [[como-calcular-ciclos-por-iteracion-del-codigo-original-con-l]] · [[desenrollado-4x-y-planificacion-minima-para-bucle-fp-con-lat]] · [[metodo-para-calcular-speedup-de-bucle-desenrollado-y-planifi]] · [[calculo-de-speedup-para-bucle-desenrollado-en-pipeline-con-h]] · [[calculo-de-speedup-entre-bucle-original-y-desenrollado-en-vl]]
