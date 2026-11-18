---
tipo: "concepto"
titulo: "Registro de historial de saltos (BHR) se implementa como registro de desplazamiento"
temas: ["ac", "bhr", "correlating predictor", "predicción saltos", "shift register"]
claves: ["BHR", "branch history register", "shift register", "global history"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bhr]] · [[correlating predictor]] · [[predicción saltos]] · [[shift register]]

El Branch History Register (BHR) almacena el historial global de los últimos saltos (tomados/no tomados) para indexar las BHTs en predictores correlacionados. Se implementa como un registro de desplazamiento (shift register) donde cada nuevo resultado del salto se introduce por un lado (1 para taken, 0 para not taken) y el bit más antiguo sale. No es una XOR, sumador ni contador saturante.

> To implement the BHR of a (2, 1) predictor we use: b) A shift register
> — `repo:datos/temarios/AC/examenes/June 2024.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[implementacion-del-bhr-branch-history-register-en-predictor]] · [[implementacion-predictor-correlacionado-m-n-con-bhr-y-bht]] · [[predictor-correlacionante-de-dos-niveles-1-1-con-bhr-global]]
