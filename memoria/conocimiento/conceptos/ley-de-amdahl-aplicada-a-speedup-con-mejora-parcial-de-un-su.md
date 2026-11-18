---
tipo: "concepto"
titulo: "Ley de Amdahl aplicada a speedup con mejora parcial de un subsistema"
temas: ["ac", "evaluacion-rendimiento", "ley-amdahl", "mejora-parcial", "speedup"]
claves: ["ley de Amdahl", "speedup", "fracción mejorada", "factor mejora", "tiempo no mejorado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[evaluacion-rendimiento]] · [[ley-amdahl]] · [[mejora-parcial]] · [[speedup]]

Fórmula general: Speedup = T_original / T_mejorado = 1 / ((1 - f) + f/k)
- f = fracción del tiempo original que usa el subsistema mejorado.
- k = factor de mejora de ese subsistema (veces más rápido).
- (1-f) = fracción no mejorada (tiempo invariante).

Ejemplo (Ejercicio 4): f = 0.5 (5s de 10s en FP), k = 5 → T_mejorado = 5s (no FP) + 5s/5 = 6s → Speedup = 10/6 = 1.67.
Ejemplo inverso (Ejercicio 5): Speedup objetivo = 3, k = 5, T_original = 100s → resolver 3 = 100 / ((100-T) + T/5) → T = 83.33s (fracción f = 83.33%).

> Sabemos que la ganancia (aceleración o speedup) es la relación entre el tiempo de ejecución sin utilizar la mejora (10 s en este caso) y el tiempo de ejecución con la mejora.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`

Relacionado: [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]] · [[calculo-de-speedup-con-ley-de-amdahl-mejora-de-una-fraccion]] · [[como-calcular-el-factor-de-mejora-necesario-k-para-un-speedu]] · [[ley-de-amdahl-para-speedup-con-mejora-parcial]]
