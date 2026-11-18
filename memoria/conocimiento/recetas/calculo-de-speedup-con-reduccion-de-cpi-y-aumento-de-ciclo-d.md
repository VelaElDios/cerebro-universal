---
tipo: "receta"
titulo: "Cálculo de speedup con reducción de CPI y aumento de ciclo de reloj (pregunta 5)"
temas: ["ac", "ciclo-reloj", "cpi", "pipeline", "rendimiento", "speedup"]
claves: ["speedup", "CPI punto flotante 35%", "ciclo reloj +20%", "CPI FP = 4 * CPI entero", "6M enteros", "2M FP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ciclo-reloj]] · [[cpi]] · [[pipeline]] · [[rendimiento]] · [[speedup]]

Sea CPI_ent = c, CPI_FP_ant = 4c. CPI_FP_nue = 0.35 * 4c = 1.4c. Ciclo_ant = T, Ciclo_nue = 1.2T. Tiempo_ant = (6M*c + 2M*4c) * T = 14McT. Tiempo_nue = (6M*c + 2M*1.4c) * 1.2T = (6M + 2.8M)c * 1.2T = 8.8Mc * 1.2T = 10.56McT. Speedup = Tiempo_ant / Tiempo_nue = 14 / 10.56 ≈ 1.325 → 32.5% más rápido. Respuesta: b) 33% faster.

> We have improved the floating-point unit of a computer, reducing the CPI for floating-point operations to 35% of its initial value. This improvement has, on the other hand, increased the clock cycle time by 20%. Assuming that, before the improvement was made, the CPI for floating-point operations was 4 times the CPI for integer operations, what is the speedup obtained by considering a test program consisting of 6 million integer instructions and 2 million floating-point instructions?
> — `repo:datos/temarios/AC/examenes/June2021.pdf`

Relacionado: [[calculo-de-speedup-con-ley-de-amdahl-para-mejora-de-unidad-d]]
