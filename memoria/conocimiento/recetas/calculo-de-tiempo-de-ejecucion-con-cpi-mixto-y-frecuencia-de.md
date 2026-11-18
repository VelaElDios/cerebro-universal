---
tipo: "receta"
titulo: "Cálculo de tiempo de ejecución con CPI mixto y frecuencia de reloj"
temas: ["ac", "cpi", "rendimiento"]
claves: ["CPIA=1", "CPIB=2", "CPIC=4", "600 MHz", "miles de millones instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[rendimiento]]

Ciclos totales = Σ (Instrucciones_tipo * CPI_tipo) = (4e9*1) + (2e9*2) + (1e9*4) = 4e9 + 4e9 + 4e9 = 12e9 ciclos. Tiempo = Ciclos / Frecuencia = 12e9 / 600e6 = 20 segundos. Respuesta correcta: b) 20 seconds.

> Assume a computer with three types of instructions (A, B, and C), and the following CPI values: CPIA=1, CPIB=2, and CPIC=4. A compiler produces a program with the following instruction count: Type A: 4, B: 2, C: 1 (in thousands of millions). Assuming a clock frequency of 600 MHz, what would be the execution time for this program?
> — `repo:datos/temarios/AC/examenes/June2018.pdf` (cita sin comprobar)
