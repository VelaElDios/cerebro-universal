---
tipo: "concepto"
titulo: "Predictor híbrido de dos predictores locales con selector por contador saturante"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor híbrido", "predictor 1-bit", "predictor 3-bit", "contador saturante 2-bit", "selector MSB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Esquema de predicción híbrida donde cada instrucción de salto tiene dos predictores locales independientes: Predictor 1 (1 bit, tipo taken/not-taken simple) y Predictor 2 (3 bits, típicamente un contador saturante de 3 bits). Una tabla "Counters" mantiene un contador saturante de 2 bits por salto. El bit más significativo (MSB) del contador decide qué predictor usar: MSB=1 → Predictor 1; MSB=0 → Predictor 2. Tanto los bits de predicción como los contadores se inicializan a 0. Tras cada predicción, se actualizan ambos predictores según el resultado real y se actualiza el contador según la regla: (Hit, Hit) → sin cambio; (Hit, Miss) → incrementar (+1); (Miss, Hit) → decrementar (-1); (Miss, Miss) → sin cambio. Esto permite adaptar dinámicamente la elección al comportamiento local de cada salto.

> Predictor 1 associates a 1-bit predictor to each branch instruction (B1 and B2) and Predictor 2 associates a 3-bit predictor to each branch. To select the predictor to employ in each case there is a table (called “Counters”) storing a 2-bit saturating counter for each branch. If the most-significant bit of the counter is 1, then Predictor 1 is selected; otherwise, Predictor 2 is selected.
> — `repo:datos/temarios/AC/examenes/January2019.pdf` (cita sin comprobar)

Relacionado: [[btb-con-predictores-de-4-bits-campos-de-cada-entrada]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
