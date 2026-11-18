---
tipo: "concepto"
titulo: "Dependencia RAW en pipeline RISC-V resuelta con adelantamiento (forwarding)"
temas: ["ac", "dependencias", "forwarding", "pipeline"]
claves: ["RAW", "load-use", "adelantamiento", "RISC-V", "lw add"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[forwarding]] · [[pipeline]]

La instrucción `lw` escribe en x5 (etapa WB) y `add` lee x5 (etapa ID/EX). Existe dependencia RAW (Read After Write). En pipelines RISC-V estándar con forwarding, el dato cargado se reenvía desde la etapa MEM/WB a la etapa EX de la instrucción siguiente, eliminando la detención (stall). La opción correcta afirma que los efectos pueden eliminarse con adelantamiento.

> Considera que el siguiente fragmento de código se ejecuta en un procesador RISC-V con las características habituales: (I1) lw x5, 0(x1) (I2) add x6, x5, x2 ... Indica cuál de las siguientes afirmaciones es cierta: ... Existe una dependencia de datos entre I1 e I2 cuyos efectos pueden eliminarse con adelantamiento
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf` (cita sin comprobar)

Relacionado: [[banco-de-registros-en-pipeline-mips-se-accede-en-etapas-id-y]]
