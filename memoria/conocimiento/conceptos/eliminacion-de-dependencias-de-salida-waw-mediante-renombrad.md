---
tipo: "concepto"
titulo: "Eliminación de dependencias de salida (WAW) mediante renombrado de registros"
temas: ["ac", "dependencias", "pipeline", "renombrado-registros"]
claves: ["dependencia salida", "WAW", "renombrado registros", "software pipelining", "trace scheduling"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]] · [[renombrado-registros]]

Las dependencias de salida (WAW) y antidependencias (WAR) son dependencias de nombre, no verdaderas. Se eliminan renombrando los registros destino (registro físico distinto para cada escritura), permitiendo ejecución fuera de orden. El *software pipelining* y el *trace scheduling* reordenan código pero no eliminan la dependencia de nombre por sí solos.

> Output dependences: b) Are removed by register renaming
> — `repo:datos/temarios/AC/examenes/January2021.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[definicion-de-dependencia-de-salida-waw-entre-dos-instruccio]] · [[dependencias-de-nombre-se-eliminan-mediante-renombramiento-d]] · [[el-renombrado-de-registros-evita-dependencias-de-nombre-war]]
