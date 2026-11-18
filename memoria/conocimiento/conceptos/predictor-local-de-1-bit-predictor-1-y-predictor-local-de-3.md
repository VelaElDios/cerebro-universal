---
tipo: "concepto"
titulo: "Predictor local de 1 bit (Predictor 1) y predictor local de 3 bits (Predictor 2) en esquema híbrido"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor 1 bit", "predictor 3 bits", "predictor local", "estado inicial 0"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Predictor 1: un bit por salto (0=Not Taken, 1=Taken). Se actualiza con el resultado real tras cada ejecución (último resultado). Predictor 2: 3 bits por salto, típicamente un contador de saturación de 3 bits (valores 000 a 111) donde el MSB indica la predicción (0=NT, 1=T). Ambos predictores son locales (indexados por la dirección del salto, aquí B1 y B2 por separado). En el examen, el estado inicial de ambos es 0 para B1 y B2 (Predictor 1: 0; Predictor 2: 000).

> Predictor 1 associates a 1-bit predictor to each branch instruction (B1 and B2) and Predictor 2 associates a 3-bit predictor to each branch.
> — `repo:datos/temarios/AC/examenes/June2017.pdf`

Relacionado: [[predictor-hibrido-con-selector-de-2-bits-entre-predictor-de]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
