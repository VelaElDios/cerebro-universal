---
tipo: "concepto"
titulo: "Contenido de una estación de reserva en Tomasulo"
temas: ["ac", "arquitectura", "estacion-reserva", "planificacion-dinamica", "tomasulo"]
claves: ["instrucción emitida", "operandos", "etiquetas", "control ejecución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[estacion-reserva]] · [[planificacion-dinamica]] · [[tomasulo]]

Cada estación de reserva almacena: (1) la operación a realizar; (2) los operandos fuente ya disponibles (valores) o, si no lo están, la etiqueta (tag) de la estación que los producirá; (3) bits de control para saber si la operación está lista para ejecutar; (4) etiquetas para la gestión de riesgos (RAW vía CDB, WAR/WAW vía renombrado).

> Las estaciones de reserva contienen: Las instrucciones que han sido emitidas y esperan su ejecución; Operandos para esas instrucciones (si ya han sido calculados), o el origen de los operandos (la estación de reserva que los obtendrá); Información necesaria para controlar la ejecución; Etiquetas para el control de los riesgos
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[estaciones-de-reserva-almacenan-etiquetas-para-control-de-ri]] · [[estructura-de-una-estacion-de-reserva-en-tomasulo]] · [[idea-central-de-tomasulo-control-distribuido-con-estaciones]]
