---
tipo: "concepto"
titulo: "Predictor híbrido con selector de 2 bits entre predictor de 1 bit y predictor de 3 bits"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor híbrido", "predictor local 1 bit", "predictor local 3 bits", "contador saturación 2 bits", "MSB selector"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2017.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

El predictor híbrido mantiene dos predictores locales por instrucción de salto: Predictor 1 (1 bit, predice tomado/no tomado simple) y Predictor 2 (3 bits, típicamente un contador de saturación de 3 bits). Un tercer elemento, la tabla "Counters", guarda un contador de saturación de 2 bits por salto. El bit más significativo (MSB) de ese contador decide qué predictor usar: MSB=1 → Predictor 1; MSB=0 → Predictor 2. Tras cada predicción, ambos predictores se actualizan con el resultado real, y el contador selector se actualiza según la tabla de reglas de acierto/fallo de cada predictor.

> Detail the behavior of a hybrid predictor combining two local predictors (called “Predictor 1” and “Predictor 2”). Predictor 1 associates a 1-bit predictor to each branch instruction (B1 and B2) and Predictor 2 associates a 3-bit predictor to each branch. To select the predictor to employ in each case there is a table (called “Counters”) storing a 2-bit saturating counter for each branch. If the most-significant bit of the counter is 1, then Predictor 1 is selected; otherwise, Predictor 2 is selected.
> — `repo:datos/temarios/AC/examenes/June2017.pdf` (cita sin comprobar)

Relacionado: [[btb-con-predictores-de-4-bits-campos-de-cada-entrada]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
