---
tipo: "receta"
titulo: "Interpretación del BHR en predictor correlacionado (m,n) (test AC Q12)"
temas: ["ac", "bhr", "correlacion", "prediccion-saltos"]
claves: ["BHR", "branch-history-register", "predictor-correlacionado", "bits-historia"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bhr]] · [[correlacion]] · [[prediccion-saltos]]

En un predictor correlacionado **(m, n)**, `m` = bits de historia global (BHR), `n` = bits del contador de predicción por entrada.
- El **BHR** registra el resultado de los últimos `m` saltos: **1 = tomado (T), 0 = no tomado (NT)**.
- Convención habitual: el bit **menos significativo (LSB) es el salto más reciente**.
- BHR = `01` (binario) → bit 0 (LSB) = 1 → **último salto fue TOMADO (T)**.
- Bit 1 = 0 → penúltimo salto fue NO TOMADO (NT).
Por tanto, la afirmación correcta es: «El último salto ejecutado fue TOMADO (T)».

> El valor del BHR en un predictor de saltos correlacionado (2, 3) en un momento dado es 01. Podemos afirmar que:
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf`

Relacionado: [[interpretacion-del-bhr-en-predictor-correlativo-2-3]] · [[predictor-correlacionado-2-1-bhr-tras-dos-saltos-tomados-des]] · [[predictor-correlacionado-1-2-bhr-11-tras-dos-saltos-tomados]]
