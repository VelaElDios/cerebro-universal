---
tipo: "receta"
titulo: "Predictor correlacionado (m,n): número de BHTs = 2^m"
temas: ["ac", "bht", "correlating predictor", "predicción saltos", "two-level"]
claves: ["correlating predictor", "two-level", "BHT", "branch history", "m bits history"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bht]] · [[correlating predictor]] · [[predicción saltos]] · [[two-level]]

En un predictor correlacionado de dos niveles (m, n), m es el número de bits de historial global (o local) y n el tamaño del contador saturante por entrada. El número de tablas de predicción (BHTs) es 2^m, ya que cada posible patrón de historial indexa una BHT distinta. Para (3,2): 2^3 = 8 BHTs, cada una con contadores de 2 bits.

> How many BHTs are there in a correlating two-level (3, 2) branch predictor? a) 8
> — `repo:datos/temarios/AC/examenes/June 2024.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-con-predictores-de-4-bits-campos-de-cada-entrada]] · [[bits-de-prediccion-en-la-i-cache-funcionamiento-y-ventajas]]
