---
tipo: "receta"
titulo: "Cálculo de MIPS para dos procesadores con distinto CPI y frecuencia (pregunta 4)"
temas: ["ac", "mips", "rendimiento"]
claves: ["MIPS", "CPI", "frecuencia", "mezcla instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips]] · [[rendimiento]]

CPI medio = Σ (frecuencia_tipo_i * CPI_i). Comp1: CPI = 0,4*2 + 0,5*8 + 0,1*6 = 0,8 + 4 + 0,6 = 5,4. MIPS = Freq(MHz)/CPI = 1200/5,4 ≈ 222,22 MIPS. Comp2: CPI = 0,4*2 + 0,5*2 + 0,1*10 = 0,8 + 1 + 1 = 2,8. MIPS = 1800/2,8 ≈ 642,86 MIPS. Respuesta correcta: c) Computer 1: 222,2 MIPS; Computer 2: 642,85 MIPS.

> Computer 1 runs at 1,2 GHz, and needs 2, 8, and 6 clock cycles for executing instructions of type A, B, and C, respectively. Computer 2 runs at 1,8 GHz, and needs 2, 2, and 10 cycles for executing instructions of type A, B, and C, respectively. The benchmark applied is composed of instructions of type A (40%), instructions of type B (50%), and instructions of type C (10%).
> — `repo:datos/temarios/AC/examenes/January2017.pdf`

Relacionado: [[calculo-de-mips-para-comparar-dos-computadores-con-mismo-isa]] · [[calculo-de-mips-para-dos-maquinas-con-mismo-isa-y-mezcla-de]] · [[calculo-de-mips-a-partir-de-frecuencia-cpi-por-tipo-y-mezcla]]
