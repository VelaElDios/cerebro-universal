---
tipo: "concepto"
titulo: "Tabla de estado en Tomasulo especulativo con ROB (Issue, Execution Start-End, Write result, Commit)"
temas: ["ac", "dynamic-scheduling", "reorder-buffer", "speculative-execution", "tomasulo"]
claves: ["Tomasulo", "ROB", "Re-Order Buffer", "Issue", "Execution Start", "Execution End", "Write result", "Commit", "reservation stations", "load buffers"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2020.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dynamic-scheduling]] · [[reorder-buffer]] · [[speculative-execution]] · [[tomasulo]]

Tomasulo especulativo con ROB añade fase Commit respecto a Scoreboard. Fases: 1) Issue: asigna estación de reserva (o buffer carga) y entrada ROB; renombra registros (Qj/Qk = tag ROB productor). 2) Execution: espera operandos (CDB o Vj/Vk); Start = ciclo donde FU empieza EX; End = Start + latencia - 1. 3) Write result: resultado en CDB + actualiza ROB (estado=completed); broadcast a estaciones de reserva esperando ese tag. 4) Commit: in-order, cuando instrucción es head of ROB y estado=completed; escribe en registro arquitectónico; libera entrada ROB. Diferencias clave vs Scoreboard: renombrado evita WAR/WAW; ejecución out-of-order; commit in-order para excepciones precisas; ROB bufferiza resultados especulativos. Enunciado: sin hazards estructurales en ROB/estaciones/load buffers; latencias EX iguales que Scoreboard.

> Complete the following instruction status table, indicating the cycle number in which each step is performed, for the code shown and according to the speculative version of the Tomasulo's algorithm. Consider that there are NOT structural hazards affecting the Re-Order Buffer (ROB), the reservation stations or the load buffers. Instruction Issue Execution Start - End Write result Commit
> — `repo:datos/temarios/AC/examenes/June2020.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffer-de-carga-en-tomasulo-especulativo]] · [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[como-rellenar-la-tabla-de-estado-en-tomasulo-con-especulacio]] · [[pasos-para-completar-tabla-de-ejecucion-tomasulo-issue-execu]] · [[como-resolver-tabla-de-estado-en-tomasulo-con-rob-y-especula]]
