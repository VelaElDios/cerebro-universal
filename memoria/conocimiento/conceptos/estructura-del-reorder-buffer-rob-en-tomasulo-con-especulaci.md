---
tipo: "concepto"
titulo: "Estructura del Reorder Buffer (ROB) en Tomasulo con especulación"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["ROB", "reorder buffer", "entry", "instruction", "stage", "destination register", "value", "commit"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

El ROB en este modelo tiene 4 entradas y cada entrada registra: número de entrada (Entry #), instrucción (Instruction), etapa actual (Stage: Issue, Execution, Write Result, Commit), registro destino (Destination Register) y valor (Value). El ejercicio pide rellenar el contenido del ROB en el ciclo 10, usando solo las entradas necesarias. Las etapas reflejan el flujo con especulación: Issue (emisión), Execution (ejecución), Write Result (escritura en CDB/registro), Commit (confirmación en orden).

> Entry #       Instruction            Stage                         Value" y "Destination Register
> — `repo:datos/temarios/AC/examenes/January2024.pdf` (cita sin comprobar)

Relacionado: [[configuracion-de-procesador-tomasulo-con-especulacion-del-ej]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[estructura-de-tabla-rob-para-tomasulo-especulativo-con-5-ent]] · [[diferencia-escritura-resultado-vs-terminacion-commit-en-toma]]
