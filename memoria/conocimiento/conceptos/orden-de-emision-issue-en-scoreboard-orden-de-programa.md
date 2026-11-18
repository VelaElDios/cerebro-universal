---
tipo: "concepto"
titulo: "Orden de emisión (issue) en Scoreboard: orden de programa"
temas: ["ac", "emision", "scoreboard", "tomasulo"]
claves: ["Scoreboard", "paso issue", "orden programa", "unidades funcionales"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[emision]] · [[scoreboard]] · [[tomasulo]]

Scoreboard emite instrucciones **en orden de programa** (in-order issue), comprobando disponibilidad de unidad funcional y riesgos WAW. Tomasulo, en cambio, emite en orden pero renombra registros y permite emisión fuera de orden efectiva gracias a estaciones de reserva.

> In Scoreboard, the order in which the issue step is performed is given by: b) The order of the instructions in the program.
> — `repo:datos/temarios/AC/examenes/January2021.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[scoreboard-los-riesgos-estructurales-se-gestionan-en-la-etap]] · [[manejo-de-riesgos-estructurales-en-scoreboard]] · [[planificacion-en-scoreboard-orden-de-ejecucion]]
