---
tipo: "receta"
titulo: "Cálculo de bits en predictor de dos niveles (n, m) con k entradas por BHT"
temas: ["ac", "dos-niveles", "prediccion-saltos"]
claves: ["predictor dos niveles", "BHT", "bits", "formula"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dos-niveles]] · [[prediccion-saltos]]

Un predictor de dos niveles (n, m) tiene un registro de historia global de n bits (2^n entradas en la tabla de patrones/PHT) y cada entrada de la PHT contiene un predictor de m bits (típicamente contador saturado de 2 bits). Si además hay una BHT indexada por PC con k entradas, cada una apuntando a una PHT distinta, los bits totales = k * (2^n * m). En el ejemplo (3,4) con 10 entradas BHT: 10 * (2^3 * 2) = 10 * 16 = 160 bits (ninguna opción coincide; la respuesta correcta sería "None of the above" si 160 no está).

> How many bits are required to implement a two-level predictor (3, 4) in which each BHT contains 10 entries?
> — `repo:datos/temarios/AC/examenes/January2019.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[calculo-de-bits-totales-en-predictor-1-2-con-bht-de-4-entrad]] · [[calculo-de-bits-en-predictor-correlacionado-de-dos-niveles-p]] · [[calculo-de-bits-totales-en-predictor-2-2-con-3-entradas-por]]
