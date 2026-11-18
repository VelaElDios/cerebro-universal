---
tipo: "concepto"
titulo: "Scoreboard: detiene ejecución ante hazards WAR y WAW"
temas: ["ac", "hazards", "planificacion-dinamica", "scoreboard"]
claves: ["Scoreboard", "WAR", "WAW", "hazard", "parada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[hazards]] · [[planificacion-dinamica]] · [[scoreboard]]

El Scoreboard (marcador) detecta hazards WAR y WAW y detiene (stall) la emisión de instrucciones hasta que se resuelven, garantizando corrección. No los ignora (eso causaría error) ni los evita por hardware. Respuesta correcta: b.

> In the Scoreboard technique… a) Cannot appear WAR and WAW hazards b) Can appear WAR and WAW hazards, which force to stop the execution of the instructions c) Can appear WAR and WAW hazards, but they are not handled by the Scoreboard, leading to incorrect program behavior d) None of the above
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[comparativa-tomasulo-vs-marcador-scoreboard]]
