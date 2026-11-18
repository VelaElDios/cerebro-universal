---
tipo: "receta"
titulo: "Cálculo CPI base pipeline 5 etapas con saltos sin predicción"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["CPI", "penalización salto", "frecuencia saltos", "tomado/no tomado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Diciembre2010.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Receta para CPI sin BTB (stall-on-branch): CPI = 1 + Σ(frecuencia_tipo × penalización_tipo). Penalización condicional = ciclos desde fetch hasta resolución sentido (EX) - 1 = 2 ciclos (IF, ID se pierden). Penalización incondicional = ciclos hasta resolución dirección (ID) - 1 = 1 ciclo (IF se pierde). Frecuencias: f_cond=0.25, f_incond=0.08. Tomados cond=0.75. CPI_base = 1 + 0.25×0.75×2 + 0.25×0.25×2 + 0.08×1 = 1 + 0.375 + 0.125 + 0.08 = 1.58.

> para una instrucción de salto condicional la dirección del salto es conocida al final de la etapa ID y el sentido al final de la etapa EX, y para una instrucción de salto incondicional la dirección del salto es conocida al final de la etapa ID
> — `repo:datos/temarios/AC/examenes/Diciembre2010.pdf`

Relacionado: [[problema-examen-ac-cpi-pipeline-con-btb-que-solo-almacena-sa]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[calculo-de-cpi-base-en-pipeline-con-penalizacion-por-saltos]] · [[calculo-de-penalizacion-de-salto-condicional-en-pipeline-de]] · [[cpi-con-prediccion-de-saltos-en-pipeline-de-5-etapas-direcci]]
