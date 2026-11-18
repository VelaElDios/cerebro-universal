---
tipo: "receta"
titulo: "Cálculo de MIPS para comparar dos computadores con mismo ISA"
temas: ["ac", "benchmark", "mips", "rendimiento"]
claves: ["MIPS", "CPI", "frecuencia", "mix de instrucciones", "ciclos por tipo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[benchmark]] · [[mips]] · [[rendimiento]]

Pasos: 1) Calcular CPI medio ponderado: CPI = Σ (fracción_i × ciclos_i). 2) MIPS = (Frecuencia en MHz) / CPI. Para Computer 1: CPI = 0.2×2 + 0.5×4 + 0.3×6 = 0.4 + 2.0 + 1.8 = 4.2 ciclos/instr. MIPS = 1200 / 4.2 ≈ 285.7. Para Computer 2: CPI = 0.2×2 + 0.5×2 + 0.3×10 = 0.4 + 1.0 + 3.0 = 4.4. MIPS = 1800 / 4.4 ≈ 409.1. Respuesta correcta: b) Computer 1: 285.7 MIPS, Computer 2: 409.1 MIPS.

> Computer 1 needs 2, 4, and 6 cycles for executing type A, B and C instructions, respectively. Computer 2 needs 2, 2, and 10 cycles. Computer 1 works at 1.2 GHz, and Computer 2 works at 1.8 GHz. The benchmark used is composed of 20% type A instructions, 50% type B, and 30% type C. What is the MIPS speed of both computers?
> — `repo:datos/temarios/AC/examenes/January2020.pdf`
