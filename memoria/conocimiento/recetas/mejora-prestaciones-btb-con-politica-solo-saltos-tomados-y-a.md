---
tipo: "receta"
titulo: "Mejora prestaciones BTB con política solo-saltos-tomados y actualización perezosa"
temas: ["ac", "btb", "prediccion-saltos"]
claves: ["BTB", "miss rate", "solo tomados", "predicción no tomado", "actualización penalización 1 ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Diciembre2010.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[btb]] · [[prediccion-saltos]]

Modelo BTB del enunciado: miss rate 10% (acierto 90%). Solo entradas para saltos tomados. Política: miss en salto tomado → actualiza BTB + 1 ciclo penalización; acierto en salto tomado → 0 penalización; salto no tomado (condicional) → si en BTB, se elimina entrada (0 penalización), si no en BTB, predicción correcta no tomado (0 penalización). CPI_BTB = 1 + penalización_media. Penalización_media = f_cond×tomados×(miss_rate×1) + f_incond×(miss_rate×1) = 0.25×0.75×0.1×1 + 0.08×0.1×1 = 0.01875 + 0.008 = 0.02675. CPI_BTB ≈ 1.02675. Speedup = CPI_base / CPI_BTB ≈ 1.58 / 1.02675 ≈ 1.54.

> Si una dirección no se encuentra en el BTB pero el salto finalmente es tomado (incluye los saltos incondicionales), el BTB es actualizado con un ciclo de penalización.
> — `repo:datos/temarios/AC/examenes/Diciembre2010.pdf`

Relacionado: [[problema-examen-ac-cpi-pipeline-con-btb-que-solo-almacena-sa]] · [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[calculo-de-cpi-con-btb-que-almacena-solo-saltos-tomados-y-pr]] · [[calculo-de-cpi-sin-btb-y-speedup-con-btb-miss-rate-10-solo-s]] · [[evaluacion-de-rendimiento-de-btb-con-politica-de-solo-saltos]]
