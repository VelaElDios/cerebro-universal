---
tipo: "concepto"
titulo: "Implementación del BHR (Branch History Register) en predictor correlacionado (2,2)"
temas: ["ac", "bhr", "prediccion-saltos", "predictor-correlacionado"]
claves: ["BHR", "predictor (2", "2)", "registro desplazamiento", "saturating counter", "sumador binario"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bhr]] · [[prediccion-saltos]] · [[predictor-correlacionado]]

El BHR guarda el historial global/locale de saltos tomados/no tomados. Para un predictor (m,n) se necesitan m bits de historial → registro de desplazamiento (shift register) de m bits. Los contadores de saturación (saturating counters) se usan en la BHT para los bits de predicción, no para el BHR.

> To implement the BHR of a (2,2) predictor we use: c) A shift register
> — `repo:datos/temarios/AC/examenes/January2021.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]]
