---
tipo: "concepto"
titulo: "Scoreboard: riesgos estructurales en paso de escritura de resultado (pregunta 12)"
temas: ["ac", "riesgos-estructurales", "scoreboard"]
claves: ["scoreboard", "write result", "common data bus", "riesgo estructural"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[riesgos-estructurales]] · [[scoreboard]]

En Scoreboard (marcador), los riesgos estructurales pueden aparecer en el paso de escritura de resultado (Write Result) si el bus de datos común (CDB) está ocupado (respuesta c). En Issue el riesgo es por falta de unidades funcionales o registros de destino libres; en Read Operands el riesgo es por dependencias de datos (WAW/WAR), no estructural. Scoreboard no usa estaciones de reserva (eso es Tomasulo), así que a) es incorrecto.

> In scoreboard, structural hazards can appear… a) In the issue step, if there is not space at the reservation station b) In the read operands step, if any of the operands is not available c) In the write result step, if the common data bus is busy d) None of the above
> — `repo:datos/temarios/AC/examenes/January2017.pdf`

Relacionado: [[comparativa-tomasulo-vs-marcador-scoreboard]]
