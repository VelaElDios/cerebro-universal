---
tipo: "receta"
titulo: "Comparación de rendimiento entre dos máquinas (CPI × ciclo de reloj)"
temas: ["ac", "rendimiento"]
claves: ["CPI", "clock cycle", "tiempo ejecución", "speedup"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[rendimiento]]

Tiempo_ejecución = CPI × ciclo_reloj × N_instrucciones.
Máquina A: 3 × 1 ns = 3 ns por instrucción.
Máquina B: 1.5 × 2 ns = 3 ns por instrucción.
Ambas tardan lo mismo → "A is as fast as B" (opción c).
Speedup = Tiempo_A / Tiempo_B = 1.0 (iguales).

> Machine A has a clock cycle of 1 ns and a CPI of 3 for a particular program, while machine B has a cycle time of 2 ns and a CPI of 1.5 for the same program. Which machine is faster for this program, how much faster?
> — `repo:datos/temarios/AC/examenes/June2023.pdf`

Relacionado: [[calculo-de-cpi-medio-ponderado-por-mezcla-de-instrucciones]] · [[como-comparar-rendimiento-de-dos-maquinas-con-mismo-isa-usan]] · [[comparacion-de-dos-implementaciones-de-la-misma-isa-cpi-y-fr]] · [[calculo-de-mips-para-comparar-dos-computadores-con-mismo-isa]]
