---
tipo: "receta"
titulo: "Simulación paso a paso del predictor híbrido para el bucle de Fibonacci"
temas: ["ac", "prediccion-saltos"]
claves: ["BEQZ", "BNEZ", "Fibonacci", "resultados reales T/NT", "tabla de simulación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Para simular el predictor híbrido en este bucle: 1) Determinar los resultados reales de B1 (BEQZ R3,next) y B2 (BNEZ R2,loop) en cada iteración. El bucle carga 6 números de Fibonacci (0,1,1,2,3,5). R2 actúa como contador (inicializado a 6). B1 se toma solo en la primera iteración (R3=0 → cero → taken), las 5 siguientes no se toma (R3≠0). B2 se toma las 5 primeras iteraciones (R2>0) y no se toma en la 6ª (R2=0). 2) Inicializar: Predictor1[B1]=0, Predictor1[B2]=0; Predictor2[B1]=0, Predictor2[B2]=0; Counter[B1]=00b, Counter[B2]=00b. 3) Para cada ejecución de salto en orden cronológico: leer MSB del contador correspondiente → elegir predictor; predecir con ese predictor; comparar con resultado real → Hit/Miss; actualizar ambos predictores (Predictor1: último resultado; Predictor2: contador saturante 3 bits); actualizar contador de 2 bits según la tabla de 4 casos. 4) Rellenar la tabla del enunciado con cada fila.

> The following MIPS64 loop reads from memory the first six Fibonacci numbers: 0, 1, 1, 2, 3, 5. Assume that R1, R2, and R5 have been previously initialized. loop: LW R3, 0(R1); BEQZ R3, next (B1); DMUL R3, R3, R5; SW R3, 0(R1); next: DADDUI R1, R1, #4; DADDUI R2, R2, #-1; BNEZ R2, loop (B2)
> — `repo:datos/temarios/AC/examenes/January2019.pdf` (cita sin comprobar)

Relacionado: [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[comportamiento-de-la-btb-en-caso-de-acierto-test-ac-q14]] · [[predictor-hibrido-con-predictores-locales-de-1-bit-y-3-bits]] · [[simulacion-de-predictor-de-saltos-de-1-nivel-con-2-bits-cont]] · [[simulacion-paso-a-paso-del-predictor-hibrido-con-contadores]]
