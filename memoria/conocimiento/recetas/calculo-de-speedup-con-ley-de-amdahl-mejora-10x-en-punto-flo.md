---
tipo: "receta"
titulo: "Cálculo de speedup con ley de Amdahl: mejora 10x en punto flotante al 50% del tiempo"
temas: ["ac", "amdahl", "pipeline", "rendimiento"]
claves: ["Amdahl", "speedup", "punto flotante", "enhancement", "fracción mejorada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[amdahl]] · [[pipeline]] · [[rendimiento]]

Aplicar la ley de Amdahl: speedup = 1 / ((1 - f) + f/s), donde f es la fracción de tiempo en la parte mejorada (0.5) y s el factor de mejora (10). Speedup = 1 / (0.5 + 0.5/10) = 1 / 0.55 ≈ 1.818. La respuesta correcta es 1.8 (opción b). Esta receta sirve para cualquier mejora parcial donde se conozca la fracción de tiempo afectada y el factor de aceleración.

> Suppose we upgrade a machine making all floating-point instructions execute ten times faster. If the execution time of some test program before the floating-point enhancement is 100 seconds, what will be the speed gain if half of the 100 seconds is spent executing floating-point instructions?
> — `repo:datos/temarios/AC/examenes/June 2024.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]] · [[calculo-de-speedup-con-ley-de-amdahl-para-mejora-de-unidad-d]] · [[calculo-de-speedup-con-ley-de-amdahl-para-instrucciones-de-p]] · [[calculo-de-ganancia-de-velocidad-speedup-con-la-ley-de-amdah]]
