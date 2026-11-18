---
tipo: "concepto"
titulo: "Problema de desambiguación de memoria (memory disambiguation)"
temas: ["ac", "memoria", "pipeline"]
claves: ["memory disambiguation", "RAW", "WAR", "WAW", "hazards memoria"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[memoria]] · [[pipeline]]

La desambiguación de memoria se refiere a determinar si dos accesos a memoria (load/store) se refieren a la misma dirección, para detectar posibles hazards RAW (Read After Write) en memoria. Es crítico en ejecución fuera de orden: un load no puede adelantarse a un store anterior si podrían solaparse. Las opciones WAR/WAW/structural no definen el problema central.

> The problem of memory "disambiguation": a) Refers to the occurrence of potential RAW hazards in memory b) Refers to the occurrence of potential WAR hazards in memory c) Refers to the occurrence of potential in-memory WAW hazards d) Refers to the occurrence of potential structural hazards in memory
> — `repo:datos/temarios/AC/examenes/January2024.pdf`

Relacionado: [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]] · [[definicion-de-riesgo-raw-read-after-write]]
