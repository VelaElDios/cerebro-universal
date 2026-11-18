---
tipo: "receta"
titulo: "Cálculo de MIPS pico a partir de mezcla de instrucciones y CPI por tipo"
temas: ["ac", "pipeline", "rendimiento"]
claves: ["MIPS", "CPI promedio", "frecuencia reloj", "mezcla instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[rendimiento]]

Para obtener el MIPS pico de cada máquina: 1) Calcular CPI promedio ponderado por la mezcla (CPI_avg = Σ %tipo_i × CPI_i). 2) MIPS = Frecuencia (MHz) / CPI_avg. Ejemplo: M1 CPI_avg = 0.4×3 + 0.5×6 + 0.1×4 = 4.6 → MIPS = 400/4.6 ≈ 87. M2 CPI_avg = 4 → MIPS = 750/4 = 187.5.

> M1 needs 3, 6, and 4 clock cycles to execute instructions of type A, B, and C, respectively. M2 needs 4 cycles for all types. M1 runs at 400 MHz and M2 runs at 750 MHz. The test program we will use has the following mix of instructions: 40% of type A, 50% of type B, and 10% of type C.
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]] · [[definicion-de-latencia-de-salto-y-huecos-de-retardo]] · [[calculo-de-mips-pico-a-partir-de-mezcla-de-instrucciones-y-f]] · [[calculo-de-cpi-medio-ponderado-por-mezcla-de-instrucciones]] · [[calculo-de-mips-pico-para-comparar-maquinas-test-ac-q4]]
