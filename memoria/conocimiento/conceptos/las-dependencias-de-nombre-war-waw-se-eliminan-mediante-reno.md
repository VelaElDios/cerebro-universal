---
tipo: "concepto"
titulo: "Las dependencias de nombre (WAR, WAW) se eliminan mediante renombramiento de registros"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["dependencia de nombre", "renombramiento", "WAR", "WAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2014A.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Las dependencias de nombre (anti-dependencias WAR y dependencias de salida WAW) no son dependencias verdaderas de datos, sino colisiones por uso del mismo registro arquitectónico. El renombramiento de registros (hardware en Tomasulo, software en compilador) asigna registros físicos distintos a cada escritura, eliminando estos hazards.

> Con respecto a las dependencias de nombre… c) Se eliminan mediante renombramiento
> — `repo:datos/temarios/AC/examenes/Noviembre2014A.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[buffer-de-carga-en-tomasulo-especulativo]]
