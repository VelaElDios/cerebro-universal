---
tipo: "concepto"
titulo: "Implementación BHT con contadores saturados de 2 bits"
temas: ["ac", "bht", "prediccion-saltos"]
claves: ["BHT", "Branch History Table", "contador saturado", "2 bits"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bht]] · [[prediccion-saltos]]

La BHT en predictores dinámicos de 2 bits se implementa con contadores saturados de 2 bits por entrada (four-state predictor: strongly taken, weakly taken, weakly not taken, strongly not taken). El contador se incrementa en taken y decrementa en not taken, saturando en los extremos. Respuesta correcta: b) Un Contador saturado de 2-bits.

> La BHT (Branch History Table) en un predictor de saltos dinámico de 2-bits se implementa mediante: a) Una operación XOR de 2-bits b) Un Contador saturado de 2-bits c) Un registro de desplazamiento de 2-bits d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2018.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[bits-de-prediccion-en-la-i-cache-funcionamiento-y-ventajas]]
