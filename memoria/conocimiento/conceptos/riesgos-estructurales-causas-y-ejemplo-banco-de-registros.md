---
tipo: "concepto"
titulo: "Riesgos estructurales: causas y ejemplo banco de registros"
temas: ["ac", "hazard estructural", "pipeline"]
claves: ["unidad funcional no segmentada", "recurso no replicado", "banco registros un puerto escritura"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[hazard estructural]] · [[pipeline]]

Ocurren por colisión de recursos. Causas típicas: unidades funcionales no totalmente segmentadas (no aceptan nueva operación cada ciclo) o recursos no replicados (ej. un solo puerto de escritura en el register file). El pipeline debe detener (stall) la instrucción posterior hasta que el recurso quede libre.

> Surgen cuando dos o más instrucciones necesitan usar los mismos recursos hardware • Posibles motivos: • Alguna unidad funcional no está totalmente segmentada • Algún recurso no se ha replicado lo suficiente • Ejemplo: el banco de registros sólo tiene un puerto de escritura, pero dos instrucciones necesitarán escribir un registro
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[tipos-de-riesgos-en-pipeline-estructurales-datos-control]] · [[riesgo-load-use-en-pipeline-mips-con-forwarding]] · [[manejo-de-riesgos-estructurales-en-scoreboard]]
