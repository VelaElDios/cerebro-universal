---
tipo: "receta"
titulo: "Cálculo de CPI medio ponderado por mezcla de instrucciones"
temas: ["ac", "pipeline", "rendimiento"]
claves: ["CPI", "mezcla instrucciones", "ciclos por tipo", "frecuencia"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[rendimiento]]

CPI_medio = Σ (fracción_tipo_i × ciclos_tipo_i)
Ejemplo: 0.4×2 + 0.5×6 + 0.1×4 = 0.8 + 3.0 + 0.4 = 4.2 ciclos/instrucción.
Luego MIPS = (frecuencia_MHz) / CPI_medio = 800 / 4.2 ≈ 190.5 MIPS.
El peak MIPS se calcula con la instrucción más rápida (tipo A, 2 ciclos): 800/2 = 400 MIPS.

> In its instruction set there are three types of instructions, A, B, and C. and it needs 2, 6, and 4 clock cycles to execute instructions of type A, B, and C. The machine has a clock frequency of 800 MHz. The test program we are going to use has the following mix of instructions: 40% type A, 50% type B, and 10% type C.
> — `repo:datos/temarios/AC/examenes/June2023.pdf`
