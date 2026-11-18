---
tipo: "concepto"
titulo: "Scoreboard escribe resultados a través del banco de registros (no CDB)"
temas: ["ac", "planificación dinámica", "scoreboard", "tomasulo"]
claves: ["Scoreboard", "CDB", "register bank", "write result", "Tomasulo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[planificación dinámica]] · [[scoreboard]] · [[tomasulo]]

Diferencia clave Scoreboard vs Tomasulo:
- Scoreboard: las unidades funcionales escriben resultados en el **banco de registros**; las instrucciones en espera leen de ahí.
- Tomasulo: usa **Common Data Bus (CDB)** para broadcast directo a estaciones de reserva y ROB.

> In the Scoreboard technique, the results of the functional units: They are sent to the instructions that are waiting for them through the register bank.
> — `repo:datos/temarios/AC/examenes/June2023.pdf` (cita sin comprobar)

Relacionado: [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]] · [[comparativa-tomasulo-vs-marcador-scoreboard]]
