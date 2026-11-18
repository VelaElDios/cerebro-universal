---
tipo: "receta"
titulo: "Comparativa de rendimiento MIPS entre dos implementaciones con distinto CPI (pregunta 4)"
temas: ["ac", "cpi", "mips", "pipeline", "rendimiento"]
claves: ["MIPS", "CPI", "frecuencia", "M1", "M2", "1000 MHz", "instrucciones A B C D"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[mips]] · [[pipeline]] · [[rendimiento]]

CPI medio = promedio ponderado. Distribución uniforme → cada tipo 25%. CPI_M1 = (1+2+3+4)/4 = 2.5. CPI_M2 = (2+2+3+4)/4 = 2.75. MIPS = Freq / CPI. Igualar MIPS: Freq_M1 / 2.5 = 1000 / 2.75 → Freq_M1 = 1000 * 2.5 / 2.75 = 909.09 MHz. Opción más cercana: a) 900 MHz.

> Let M1 and M2 be two different implementations of the same instruction set, in which there are 4 types of instructions (A, B, C, and D). Next table shows the CPI for each type of instruction (in both computers): Type CPI in M1 CPI in M2 A 1 2 B 2 2 C 3 3 D 4 4 If the number of instructions in a given program is evenly distributed among the four types of instructions, at what clock frequency would M1 have the same performance (using MIPS as a metric) as a 1000 MHz version of M2?
> — `repo:datos/temarios/AC/examenes/June2021.pdf`

Relacionado: [[calculo-de-speedup-con-ley-de-amdahl-para-mejora-de-unidad-d]]
