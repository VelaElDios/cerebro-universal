---
tipo: "receta"
titulo: "Simulación de predictor one-level de 2 bits para dos saltos (B1/B2)"
temas: ["ac", "examen", "prediccion-saltos"]
claves: ["one-level predictor", "2-bit saturating counter", "B1", "B2", "initial state 11"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[prediccion-saltos]]

Para cada salto (B1 y B2) se mantiene un contador de 2 bits independiente (estados 00=Strongly NT, 01=Weakly NT, 10=Weakly T, 11=Strongly T). Estado inicial: ambos en 11. En cada ejecución del salto: se usa el MSB del contador como predicción (1=T, 0=NT); se compara con resultado real (T/NT); se actualiza el contador: si T y no 11 -> +1; si NT y no 00 -> -1. Se anota Hit (Y/N) si predicción == resultado real. La tabla del examen tiene columnas: Prediction bits for B1 and B2, Predicted outcome (T/NT), Hit (Y/N).

> Detail the behavior of a one-level branch predictor using 2 bits per branch instruction, assuming the same input vector, and considering the initial state indicated in the table.
> — `repo:datos/temarios/AC/examenes/June2022.pdf`

Relacionado: [[simulacion-de-predictor-two-level-correlacionante-2-1-con-bh]] · [[simulacion-de-predictor-de-un-nivel-con-contadores-de-satura]] · [[simulacion-de-predictor-de-saltos-de-1-nivel-con-2-bits-cont]]
