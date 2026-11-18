---
tipo: "receta"
titulo: "Cálculo de tiempo de ejecución con CPI y frecuencia"
temas: ["ac", "rendimiento"]
claves: ["CPI", "tiempo ejecución", "ciclos reloj", "nanosegundos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[rendimiento]]

Tiempo = (Instrucciones × CPI) × Duración_ciclo. Ejemplo: 5.5e9 × 0.9 × 0.5e-9 = 2.475 segundos. Fórmula útil para estimar rendimiento dada la cuenta de instrucciones, CPI medio y frecuencia de reloj.

> Ejecutamos un programa de 5.5×109 instrucciones en un procesador con un CPI de 0.9 ciclos y con una duración del ciclo de reloj de 0.5 ns. El tiempo de ejecución de dicho programa será de…
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]]
