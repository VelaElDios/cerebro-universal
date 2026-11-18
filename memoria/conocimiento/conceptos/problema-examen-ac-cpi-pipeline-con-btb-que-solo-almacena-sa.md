---
tipo: "concepto"
titulo: "Problema examen AC: CPI pipeline con BTB que solo almacena saltos tomados"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["BTB", "CPI", "salto condicional", "salto incondicional", "tasa fallos 10%", "penalización actualización"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Diciembre2010.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Enunciado de problema tipo examen: pipeline 5 etapas (IF, ID, EX, MEM, WB). Dirección salto conocida fin ID, sentido fin EX (condicional) o fin ID (incondicional). Frecuencias: condicionales 25%, incondicionales 8%. De condicionales, 75% tomados. BTB con miss rate 10%, solo guarda saltos tomados, predice no tomado si no está, elimina entrada si predicho tomado pero resulta no tomado (sin penalización), actualiza con 1 ciclo penalización si no está pero es tomado. Preguntas: a) CPI sin BTB, b) mejora con BTB.

> Tiene una tasa de fallos del 10%. Sólo almacena las direcciones de saltos tomados (incluye los saltos incondicionales). Si un salto condicional no está en BTB se predice como no tomado.
> — `repo:datos/temarios/AC/examenes/Diciembre2010.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[calculo-de-cpi-con-btb-que-almacena-solo-saltos-tomados-y-pr]] · [[evaluacion-de-rendimiento-de-btb-con-politica-de-solo-saltos]] · [[calculo-de-cpi-base-en-pipeline-con-penalizacion-por-saltos]]
