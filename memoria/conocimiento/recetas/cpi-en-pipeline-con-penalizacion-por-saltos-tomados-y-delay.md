---
tipo: "receta"
titulo: "CPI en pipeline con penalización por saltos tomados y delay slots"
temas: ["ac", "cpi", "delay slots", "pipeline", "prediccion-saltos"]
claves: ["CPI", "IPC", "taken branches", "delay slots", "penalty"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[delay slots]] · [[pipeline]] · [[prediccion-saltos]]

Fórmula: CPI = 1 + (fracción_saltos_tomados × slots_retraso_no_rellenables).
- 2 de cada 8 instrucciones son saltos tomados → fracción = 2/8 = 0.25.
- 3 delay slots por salto tomado.
- Si no se rellenan (peor caso): ciclos extra = 0.25 × 3 = 0.75.
- CPI = 1 + 0.75 = 1.75 → IPC = 1/1.75 ≈ 0.57.
Opción correcta: **CPI = 1.75, IPC = 0.57**.

> Given a 5-stage pipeline in which 2 out of every 8 instructions are taken branches and there are 3 delay slots for each taken branch, indicate which of the following options is correct:
> — `repo:datos/temarios/AC/examenes/June2023.pdf`

Relacionado: [[cpi-con-prediccion-de-saltos-en-pipeline-de-5-etapas-direcci]] · [[cpi-con-penalizacion-de-saltos-resueltos-en-id-test-ac-q13]] · [[cpi-con-tecnica-parar-siempre-en-saltos-cpi-1-saltos-tomados]]
