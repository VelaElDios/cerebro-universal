---
tipo: "concepto"
titulo: "Riesgos resueltos por Marcador y por Tomasulo sin especulación"
temas: ["ac", "marcador", "riesgos", "tomasulo"]
claves: ["marcador", "Tomasulo", "RAW", "WAW", "WAR", "especulación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[marcador]] · [[riesgos]] · [[tomasulo]]

El Marcador (Scoreboard) detecta y espera por riesgos RAW y WAW, pero no resuelve WAR (no renombra). Tomasulo sin especulación usa renombramiento de registros vía estaciones de reserva, resolviendo WAW y WAR, y resuelve RAW mediante bypass (CDB). La opción correcta es d: Tomasulo sin especulación resuelve WAW y WAR.

> Indica la respuesta correcta: a. La técnica de marcador resuelve los riesgos RAW y WAW b. La técnica de marcador resuelve los riesgos WAW y WAR c. La técnica de Tomasulo sin especulación resuelve los riesgos RAW y WAW d. La técnica de Tomasulo sin especulación resuelve los riesgos WAW y WAR
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf`

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[diferencia-scoreboard-vs-tomasulo-en-resolucion-de-hazards-s]] · [[gestion-de-riesgos-war-y-waw-en-tomasulo-pregunta-10]] · [[tecnica-de-marcador-scoreboard-riesgos-war-waw-obligan-a-det]]
