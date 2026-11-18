---
tipo: "concepto"
titulo: "Supuestos de temporización para tablas de planificación en examen AC June 2021"
temas: ["ac", "pipeline", "scoreboard", "tomasulo"]
claves: ["CDB", "Common Data Bus", "stall", "ciclo mismo", "penalización +1"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[scoreboard]] · [[tomasulo]]

Dos reglas clave para rellenar las tablas de ciclos: (1) Forwarding por CDB en el mismo ciclo: si una instrucción espera un resultado y ese resultado se escribe en el CDB en el ciclo N, la instrucción puede reanudar/empezar su ejecución en ese mismo ciclo N (sin esperar al siguiente). (2) Otros stalls (conflictos estructurales, WAW, WAR, disponibilidad de buffers/estaciones): la instrucción detenida solo puede continuar en el ciclo siguiente a la resolución del stall (penalización de +1 ciclo). Estos supuestos son específicos de este enunciado y difieren de otras convenciones (p.ej. algunos modelos exigen +1 ciclo también para CDB).

> An instruction that is waiting for a result can resume its execution in the same cycle in which this result is written to the Common Data Bus. / In the rest of cases where a stall occurs, the stopped instruction cannot continue execution until the next cycle in which the stall has been resolved (+1 cycle).
> — `repo:datos/temarios/AC/examenes/June2021.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]] · [[restriccion-cdb-mismo-ciclo-en-tomasulo-no-iniciar-ejecucion]] · [[restricciones-de-timing-en-tomasulo-con-especulacion-examen]] · [[regla-de-contencion-del-cdb-y-disponibilidad-de-recursos-en]]
