---
tipo: "concepto"
titulo: "Interpretación del BHR en predictor correlativo (2,3)"
temas: ["ac", "prediccion-saltos"]
claves: ["BHR", "correlating branch predictor", "branch history register"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

En un predictor correlativo (m, n) donde m=2 (bits de historia global) y n=3 (bits de historia local), el BHR (Branch History Register) almacena el resultado de las últimas m ramas ejecutadas (T=1, NT=0). Un valor BHR=01 significa que la rama más antigua fue NT (0) y la más reciente fue T (1). Por tanto, la última rama ejecutada fue TAKEN (T). La opción correcta es (a).

> The value of the BHR in a correlating branch predictor (2, 3) at any given time is 01. We can state that:
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[interpretacion-del-bhr-en-predictor-correlacionado-m-n-test]] · [[predictor-correlacionado-1-2-bhr-11-tras-dos-saltos-tomados]] · [[predictor-correlacionado-2-1-bhr-tras-dos-saltos-tomados-des]]
