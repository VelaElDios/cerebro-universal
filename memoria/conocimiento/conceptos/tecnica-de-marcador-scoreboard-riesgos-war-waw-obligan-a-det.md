---
tipo: "concepto"
titulo: "Técnica de Marcador (Scoreboard): riesgos WAR/WAW obligan a detener"
temas: ["ac", "riesgos", "scoreboard", "war", "waw"]
claves: ["Scoreboard", "marcador", "WAR", "WAW", "stall", "detencion"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2011.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[riesgos]] · [[scoreboard]] · [[war]] · [[waw]]

El Scoreboard detecta riesgos WAR y WAW (por falta de renombramiento) y resuelve deteniendo (stall) la instrucción posterior hasta que el riesgo desaparece, no produciendo comportamiento erróneo.

> Pueden aparecer riesgos WAR y WAW, que obligan a detener la ejecución de instrucciones
> — `repo:datos/temarios/AC/examenes/Enero2011.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[planificacion-dinamica-orden-de-ejecucion-por-disponibilidad]]
