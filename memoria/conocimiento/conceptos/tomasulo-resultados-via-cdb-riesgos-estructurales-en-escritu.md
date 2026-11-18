---
tipo: "concepto"
titulo: "Tomasulo: resultados via CDB, riesgos estructurales en escritura, especulación commit"
temas: ["ac", "cdb", "especulacion-hardware", "riesgo-estructural", "rob", "tomasulo"]
claves: ["Common Data Bus", "riesgo estructural escritura", "commit", "resultado definitivo", "especulación hardware"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2013.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cdb]] · [[especulacion-hardware]] · [[riesgo-estructural]] · [[rob]] · [[tomasulo]]

Tres hechos del test: (8) Resultados via CDB (Common Data Bus), no por buffers de carga ni registros. (9) Riesgos estructurales posibles en fase de escritura (CDB es recurso compartido, 1 puerto). (15) En especulación hardware, resultado se hace definitivo en etapa commit (no al almacenar en ROB ni antes). Instrucciones modifican ROB y registros renombrados; en commit escriben en estado arquitectónico real.

> En la técnica de Tomasulo, los resultados de las unidades funcionales pasan a las instrucciones que están a la espera a través del CDB
> — `repo:datos/temarios/AC/examenes/Enero2013.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[comparativa-tomasulo-vs-marcador-scoreboard]]
