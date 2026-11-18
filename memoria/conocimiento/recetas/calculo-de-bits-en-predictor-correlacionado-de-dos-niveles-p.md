---
tipo: "receta"
titulo: "Cálculo de bits en predictor correlacionado de dos niveles (pregunta 13 y 15)"
temas: ["ac", "prediccion-saltos", "predictor-correlacionado"]
claves: ["predictor dos niveles", "BHT", "PHT", "bits predicción", "(m", "n) predictor"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[predictor-correlacionado]]

Predictor correlacionado de dos niveles (m,n): m = bits de historia global/local, n = bits de contador por entrada PHT. Número de BHTs = 2^m (cada patrón de historia tiene su propia tabla de predicción). Pregunta 15: (3,2) → 2^3 = 8 BHTs (respuesta c). Pregunta 13: (2,2) con 3 entradas por BHT. Total bits = (número de BHTs) * (entradas por BHT) * (bits por contador) = 2^2 * 3 * 2 = 4 * 3 * 2 = 24 bits. Respuesta b) 24 bits.

> How many BHTs are there in a correlating two-level (3,2) predictor? a) 3 b) 6 c) 8 d) None of the above
> — `repo:datos/temarios/AC/examenes/January2017.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]]
