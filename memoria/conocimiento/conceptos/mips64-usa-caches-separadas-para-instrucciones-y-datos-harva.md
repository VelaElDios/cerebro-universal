---
tipo: "concepto"
titulo: "MIPS64 usa cachés separadas para instrucciones y datos (Harvard modificada)"
temas: ["ac", "cache", "mips64", "pipeline"]
claves: ["MIPS64", "I-cache", "D-cache", "Harvard"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cache]] · [[mips64]] · [[pipeline]]

MIPS64 implementa una arquitectura Harvard modificada con cachés de primer nivel separadas: I-cache (instrucciones) y D-cache (datos). El PC se actualiza en la etapa IF (no en WB). El pipelining reduce el CPI ideal a 1, no la latencia de una instrucción individual.

> Mark which of the following statements is correct for MIPS64: It uses one cache memory for instructions and another for data.
> — `repo:datos/temarios/AC/examenes/June2023.pdf` (cita sin comprobar)

Relacionado: [[banco-de-registros-en-pipeline-mips-se-accede-en-etapas-id-y]]
