---
tipo: "receta"
titulo: "Igualar rendimiento de dos máquinas ajustando frecuencia de reloj"
temas: ["ac", "comparacion-maquinas", "cpi", "frecuencia-reloj", "rendimiento"]
claves: ["CPI medio", "frecuencia", "tiempo ejecución", "rendimiento igual"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[comparacion-maquinas]] · [[cpi]] · [[frecuencia-reloj]] · [[rendimiento]]

Para que M1 a frecuencia f tenga mismo tiempo que M2 a 1 GHz con mismo NI: (CPI_M1 / f) = (CPI_M2 / 1GHz) → f = CPI_M1 × 1GHz / CPI_M2. Ejercicio 19: CPI_M1 = (4+3+2+1)/4 = 2.5, CPI_M2 = (2+2+4+4)/4 = 3. f = 2.5/3 × 1GHz = 833.33 MHz.

> Tiempo de ejecución = NI × CPI / Frecuencia
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[igualar-mips-entre-dos-maquinas-despejando-frecuencia-de-rel]] · [[calculo-de-cpi-medio-mips-y-speedup-entre-dos-maquinas]] · [[ejercicios-de-cpi-mips-y-tiempo-de-ejecucion-con-mezcla-de-i]]
