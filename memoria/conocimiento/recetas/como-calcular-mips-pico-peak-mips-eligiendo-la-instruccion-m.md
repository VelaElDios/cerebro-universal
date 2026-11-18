---
tipo: "receta"
titulo: "Cómo calcular MIPS pico (peak MIPS) eligiendo la instrucción más rápida"
temas: ["ac", "evaluacion-rendimiento", "mips", "pico"]
claves: ["MIPS pico", "peak MIPS", "CPI mínimo", "frecuencia reloj"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[evaluacion-rendimiento]] · [[mips]] · [[pico]]

Fórmula: MIPS_pico = Frecuencia_Hz / (CPI_mínimo × 10^6).
- Identificar la clase de instrucción con menor CPI (ciclos por instrucción).
- Usar ese CPI_mínimo en la fórmula.
- No se usa CPI medio ni mezcla de instrucciones; solo la mejor instrucción posible.

Ejemplo (Ejercicio 2):
- M1: 500 MHz, CPI mín = 1 (clase A) → MIPS_pico = 500×10^6 / (1×10^6) = 500 MIPS.
- M2: 750 MHz, CPI mín = 2 (clases A y B) → MIPS_pico = 750×10^6 / (2×10^6) = 375 MIPS.

> El rendimiento pico se obtendrá con las instrucciones cuya ejecución sea más rápida.
> — `repo:datos/temarios/AC/Tema1-Introduccion/Tema1_ProbSol.pdf`

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[calculo-de-mips-nativos-y-de-pico-peak-mips-para-maquinas-co]] · [[como-calcular-mips-pico-a-partir-de-frecuencia-y-cpi-minimo]] · [[definicion-de-mips-millones-de-instrucciones-por-segundo]]
