---
tipo: "receta"
titulo: "Ejercicio: simulación de predictores de 2 bits vs correlacionado (3,1) para bucles anidados"
temas: ["ac", "bucles anidados", "correlating predictor", "ejercicio", "predicción saltos", "two-bit predictor"]
claves: ["branch prediction", "nested loops", "misprediction rate", "2-bit predictor", "(3", "1) predictor", "BHR", "BHT"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles anidados]] · [[correlating predictor]] · [[ejercicio]] · [[predicción saltos]] · [[two-bit predictor]]

**Comportamiento real**: B1 (bucle interno j<6): se ejecuta 6 veces por iteración externa; tomado 5 veces (j=0..4), no tomado 1 vez (j=5). Total: 60000 ejecuciones, 50000 tomados. B2 (bucle externo i<10000): se ejecuta 10000 veces; tomado 9999, no tomado 1. **Opción A (predictor 2-bit por salto, inicial strongly taken)**: Simular autómata de 2 bits para cada salto con su patrón. B1: patrón TTTTTN repetido. Estado inicial ST (11). Secuencia: T->ST, T->ST, T->ST, T->ST, T->ST, N->WT (10) [fallo], siguiente iteración: T->ST (acierto), T->ST, T->ST, T->ST, T->ST, N->WT [fallo]... Cada iteración externa causa 1 fallo en B1 (en la transición N). 10000 fallos en B1. B2: patrón T...TN (9999 T, 1 N). Inicial ST. Primeros 9999 T: siempre ST, aciertos. Último N: ST->WT [fallo]. 1 fallo en B2. Total fallos A = 10001. Tasa ma = 10001 / 70000 ≈ 0.1429. **Opción B (predictor correlacionado (3,1): 3 bits historial global, 1 bit por entrada (8 BHTs), todos a 1 (taken))**: El historial global de 3 bits indexa una de 8 BHTs. Inicial BHR=000 (asumir 0=not taken? pero bits a 1 significa taken? El enunciado dice "all its bits start with a value of 1" referido a los contadores de las BHTs). Simular requiere traza completa. Esta receta sirve como plantilla para resolver ejercicios de comparación de predictores en bucles anidados.

> We have a pipelined processor with two design options: Option A: Use two-bit predictors for each branch instruction (assuming they are initially strongly taken). Option B: Use a (3,1) predictor (assuming all its bits start with a value of 1). Given the following code for (i=0; i<10000; i++) for (j=0; j<6; j++) ... Complete the following table: Real behaviour of the jumps ... Using predictors Option A ... Option B
> — `repo:datos/temarios/AC/examenes/June 2024.pdf` (cita sin comprobar)

Relacionado: [[contador-saturante-de-3-bits-en-estado-111-indica-tres-tomas]] · [[registro-de-historial-de-saltos-bhr-se-implementa-como-regis]] · [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[simulacion-de-predictores-1-bit-4-bits-saturado-y-correlacio]] · [[calculo-de-predicciones-correctas-en-bucles-anidados-con-pre]] · [[como-analizar-predictores-de-salto-1-bit-4-bit-correlacionad]]
