---
tipo: "concepto"
titulo: "Estructura de un predictor correlacionado (2,4): 4 BHR y 2 BHT"
temas: ["ac", "bhr", "bht", "prediccion-saltos", "predictor-correlacionado"]
claves: ["predictor (2", "4)", "4 BHR", "2 BHT", "correlacionado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bhr]] · [[bht]] · [[prediccion-saltos]] · [[predictor-correlacionado]]

Notación (m,n): m = bits de historial (tamaño BHR), n = número de entradas de la BHT (2^n). Un predictor correlacionado (2,4) usa 2 bits de historial → 4 posibles patrones (00,01,10,11) → **4 BHR** (uno por patrón) y **2 BHT** (cada una con 4 entradas de 2 bits). Opción c correcta.

> A (2,4) correlating predictor uses exactly: c) 4 BHRs and 2 BHTs
> — `repo:datos/temarios/AC/examenes/January2021.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]]
