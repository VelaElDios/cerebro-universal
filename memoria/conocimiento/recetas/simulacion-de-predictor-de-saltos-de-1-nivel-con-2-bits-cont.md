---
tipo: "receta"
titulo: "Simulación de predictor de saltos de 1 nivel con 2 bits (contador saturación) para secuencia dada"
temas: ["2-bit-saturating-counter", "ac", "branch-prediction", "mips64", "one-level"]
claves: ["2-bit predictor", "saturating counter", "state machine", "00=strongly NT", "01=weakly NT", "10=weakly T", "11=strongly T"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2020.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[2-bit-saturating-counter]] · [[ac]] · [[branch-prediction]] · [[mips64]] · [[one-level]]

Predictor 1-nivel 2 bits: cada instrucción de salto tiene su contador de 2 bits independiente. Estados: 00=Strongly NT, 01=Weakly NT, 10=Weakly T, 11=Strongly T. Predicción: MSB=1 → Taken, MSB=0 → Not Taken. Actualización tras resultado real: Taken → incrementa (saturando en 11); Not Taken → decrementa (saturando en 00). En ejercicio: B1 (BEQZ R3, isnull) estado inicial 00; B2 (BEQ R1, R2, end) estado inicial 11. Vector entrada: 0,7,0,0,0,0,2,0 → 8 iteraciones. B1: T cuando R3≠0 (valores 7,2), NT cuando R3=0 (6 veces). B2: NT mientras R1≠R2 (7 primeras iteraciones), T en última (R1=R2). Simular ciclo a ciclo actualizando contadores y anotando Hit/Miss.

> b) Detail the behavior of a one-level branch predictor using 2 bits per branch instruction, assuming the same input vector, and considering the initial state indicated in the table. Use columns 3, 4, and 5. Prediction bits for B1 and B2 (Initial state) 00 11
> — `repo:datos/temarios/AC/examenes/June2020.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]] · [[btb-con-predictores-de-4-bits-campos-de-cada-entrada]]
