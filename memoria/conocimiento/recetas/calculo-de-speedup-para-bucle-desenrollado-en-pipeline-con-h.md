---
tipo: "receta"
titulo: "Cálculo de Speedup para bucle desenrollado en pipeline con hazards"
temas: ["ac", "loop-unrolling", "pipeline", "rendimiento", "speedup"]
claves: ["ciclos base", "ciclos optimizado", "speedup = base/optimizado", "CPI", "latencias UF"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop-unrolling]] · [[pipeline]] · [[rendimiento]] · [[speedup]]

Speedup = (Ciclos_totales_código_base) / (Ciclos_totales_código_optimizado). Código base: iteraciones N, cada iteración tiene stalls por RAW (fmul.d 5 ciclos -> fadd.d espera 4 ciclos? fadd.d 4 ciclos -> fsd espera?), WAR/WAW, control. Calcular CPI_base * N + overhead. Código optimizado: 4 iteraciones por vuelta, sin stalls (ideal CPI=1 para instrucciones útiles), overhead de prologue/epilogue y salto. Speedup ≈ (N * CPI_base) / (N/4 * CPI_opt + overhead). Explicar stalls eliminados y overhead introducido.

> Calcula el Speedup obtenido respecto al código base. Indica y explica los cálculos realizados.
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf`

Relacionado: [[metodo-para-calcular-speedup-de-bucle-desenrollado-y-planifi]] · [[speedup-teorico-del-desenrollado-4x-frente-a-codigo-original]] · [[calculo-de-speedup-entre-bucle-original-y-desenrollado-en-vl]]
