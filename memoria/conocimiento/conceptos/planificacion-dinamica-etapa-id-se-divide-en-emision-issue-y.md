---
tipo: "concepto"
titulo: "Planificación dinámica: etapa ID se divide en emisión (issue) y lectura de operandos"
temas: ["ac", "pipeline", "planificación dinámica", "tomasulo"]
claves: ["dynamic scheduling", "ID stage", "issue", "operand read", "reservation stations"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[planificación dinámica]] · [[tomasulo]]

En planificación dinámica (p.ej. algoritmo Tomasulo), la etapa ID del pipeline in-order se divide en dos sub-etapas: 1) Issue: se decodifica la instrucción, se renombra registros (asignando estaciones de reserva) y se envía a la estación de reserva correspondiente; 2) Operand read: se esperan los operandos (ya sea valores inmediatos o etiquetas Qj/Qk) y cuando están listos se inicia la ejecución. Esto permite emisión in-order pero ejecución out-of-order.

> In dynamic instruction scheduling, which of the following statements is correct? a) The ID stage is divided into two: issue and operand reading.
> — `repo:datos/temarios/AC/examenes/June 2024.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]]
