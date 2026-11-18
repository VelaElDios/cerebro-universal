---
tipo: "concepto"
titulo: "Diferencia Scoreboard vs Tomasulo en resolución de hazards sin especulación"
temas: ["ac", "hazards", "planificacion-dinamica", "scoreboard", "tomasulo"]
claves: ["RAW", "WAW", "WAR", "scoreboard", "tomasulo", "renombrado", "estaciones reserva"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[hazards]] · [[planificacion-dinamica]] · [[scoreboard]] · [[tomasulo]]

Scoreboard resuelve RAW y WAW (pero no WAR por falta de renombrado). Tomasulo sin especulación resuelve RAW, WAW y WAR gracias al renombrado de registros vía estaciones de reserva. Respuesta correcta: c. The Tomasulo technique without speculation resolves RAW and WAW hazards (también WAR implícito).

> The Tomasulo technique without speculation resolves RAW and WAW hazards
> — `repo:datos/temarios/AC/examenes/June2025.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]]
