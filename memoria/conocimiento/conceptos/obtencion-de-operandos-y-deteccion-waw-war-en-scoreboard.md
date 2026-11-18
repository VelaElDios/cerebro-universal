---
tipo: "concepto"
titulo: "Obtención de operandos y detección WAW/WAR en Scoreboard"
temas: ["ac", "riesgos", "scoreboard", "tomasulo"]
claves: ["scoreboard", "register file", "WAW", "WAR", "detección"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[riesgos]] · [[scoreboard]] · [[tomasulo]]

En el Scoreboard (planificación dinámica en orden), los operandos se leen del banco de registros (no hay bus común de datos CDB ni reorder buffer). Los riesgos WAW (dependencia de salida) se detectan en el primer paso (emisión) y los WAR (antidependencia) en el último paso (escritura de resultado), lo que limita el paralelismo porque las instrucciones deben esperar a que se resuelvan estos riesgos de nombre.

> In the Scoreboard technique: WAW and WAR hazards are checked in the first and last step, respectively
> — `repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)` (cita sin comprobar)

Relacionado: [[tecnica-de-marcador-scoreboard-riesgos-war-waw-obligan-a-det]] · [[manejo-de-riesgos-estructurales-en-scoreboard]] · [[scoreboard-los-riesgos-estructurales-se-gestionan-en-la-etap]]
