---
tipo: "concepto"
titulo: "Selector de 2 bits para predictor híbrido de saltos"
temas: ["ac", "prediccion-saltos"]
claves: ["selector", "contador saturación 2 bits", "predictor híbrido", "Predictor 1", "Predictor 2", "Hit/Miss"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

El selector es un contador de saturación de 2 bits que decide qué predictor usar. Tras cada predicción, ambos predictores se actualizan y el selector se modifica según la tabla:
- Predictor 1 Hit, Predictor 2 Hit → Selector no cambia
- Predictor 1 Hit, Predictor 2 Miss → Selector +1
- Predictor 1 Miss, Predictor 2 Hit → Selector -1
- Predictor 1 Miss, Predictor 2 Miss → Selector no cambia
Si Selector ≥ 2 se usa Predictor 1; en caso contrario Predictor 2. Selector y bits de predicción se inicializan a 1.

> To select the predictor to employ in each case there is a "Selector", which is a 2-bit saturating counter
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-con-predictores-de-4-bits-campos-de-cada-entrada]]
