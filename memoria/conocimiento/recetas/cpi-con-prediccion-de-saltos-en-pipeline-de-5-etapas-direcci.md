---
tipo: "receta"
titulo: "CPI con predicción de saltos en pipeline de 5 etapas (dirección en EX, destino en ID)"
temas: ["ac", "cpi", "pipeline", "prediccion-saltos"]
claves: ["CPI", "branch prediction", "taken rate", "branch frequency", "penalty"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cpi]] · [[pipeline]] · [[prediccion-saltos]]

Penalización por salto tomado = ciclos entre IF y resolución de dirección (EX) = 2 ciclos (se anulan IF e ID del camino erróneo). Saltos no tomados no penalizan si se resuelven en ID (secuencial). CPI = 1 (base) + penalización * %tomados * %saltos = 1 + 2 * 0.8 * 0.3 = 1.48. La opción correcta usa 2 ciclos de penalización, 0.8 tomados, 0.3 frecuencia.

> For a 5-stage pipeline, we run a code with 30% of instructions being a conditional branch, from which 80% are taken. In this processor, the branch direction is solved in the EX stage and the target address in the ID stage (the CPI is 1 for the rest of the instructions). Indicate the correct answer: CPI = 1 + 2 x 0,8 x 0,3
> — `repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)` (cita sin comprobar)

Relacionado: [[cpi-con-penalizacion-de-saltos-resueltos-en-id-test-ac-q13]] · [[cpi-en-pipeline-con-penalizacion-por-saltos-tomados-y-delay]] · [[calculo-cpi-base-pipeline-5-etapas-con-saltos-sin-prediccion]]
