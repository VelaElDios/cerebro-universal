---
tipo: "receta"
titulo: "Igualar MIPS entre dos máquinas despejando frecuencia de reloj (ejercicio 15)"
temas: ["ac", "arquitectura-computadores", "cpi", "frecuencia-reloj", "mips"]
claves: ["MIPS", "CPI medio", "frecuencia", "mezcla equitativa", "igualar rendimiento"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[cpi]] · [[frecuencia-reloj]] · [[mips]]

Dado MIPS = Freq / (CPI_medio * 1e6). Igualar MIPS_M1 = MIPS_M2 → Freq_M1 / CPI_M1 = Freq_M2 / CPI_M2 → Freq_M1 = Freq_M2 * (CPI_M1 / CPI_M2). Mezcla equitativa (25% cada tipo): CPI_M1 = (1+2+3+4)/4 = 2.5; CPI_M2 = (2+2+4+4)/4 = 3. Freq_M2=750 MHz → Freq_M1 = 750 * (2.5/3) = 625 MHz.

> Como el valor de MIPS debe ser el mismo para ambas máquinas, f / (2.5×10^6) = 750×10^6 / (3×10^6) → f = 625 MHz
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-mips-nativos-y-de-pico-peak-mips-para-maquinas-co]]
