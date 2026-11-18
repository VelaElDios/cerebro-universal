---
tipo: "concepto"
titulo: "Planificación en Scoreboard: orden de ejecución"
temas: ["ac", "planificación dinámica", "scoreboard"]
claves: ["Scoreboard", "orden de ejecución", "dependencias", "estaciones de reserva"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[planificación dinámica]] · [[scoreboard]]

Scoreboard (CDC 6600) permite ejecución fuera de orden: una instrucción empieza ejecución cuando sus operandos están listos y la unidad funcional está libre. El orden lo dictan las dependencias de datos (RAW) y la disponibilidad de recursos, no el orden del programa. La opción correcta es c) Dependences that exist in the program.

> In the Scoreboard scheduling technique, the order in which the stage of execution of the instructions is performed is given by: a) The number of hardware reservation stations. b) The order of instructions in the program. c) Dependences that exist in the program. d) None of the above.
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[planificacion-dinamica-orden-de-ejecucion-por-disponibilidad]] · [[orden-de-emision-issue-en-scoreboard-orden-de-programa]] · [[planificacion-dinamica-de-instrucciones-el-hardware-reordena]]
