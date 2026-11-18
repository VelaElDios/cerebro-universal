---
tipo: "concepto"
titulo: "Manejo de riesgos estructurales en Scoreboard"
temas: ["ac", "riesgos estructurales", "scoreboard"]
claves: ["scoreboard", "structural hazards", "issue step", "functional units"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[riesgos estructurales]] · [[scoreboard]]

En el Scoreboard (marcador), los riesgos estructurales (conflictos por unidades funcionales ocupadas) se detectan y resuelven en la etapa de **emisión (issue)**: la instrucción no se emite hasta que haya una unidad funcional libre del tipo requerido. No hay renombrado de registros; los riesgos de datos (RAW, WAR, WAW) se gestionan en etapas posteriores (read operands, execution, write result).

> In Scoreboard... b) Structural hazards are handled in the issue step.
> — `repo:datos/temarios/AC/examenes/January2018.pdf` (cita sin comprobar)

Relacionado: [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[scoreboard-los-riesgos-estructurales-se-gestionan-en-la-etap]] · [[riesgos-estructurales-en-marcador-scoreboard-fase-de-emision]] · [[tecnica-de-marcador-scoreboard-riesgos-war-waw-obligan-a-det]]
