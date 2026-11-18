---
tipo: "concepto"
titulo: "Eliminación de dependencias de nombre mediante renombramiento"
temas: ["ac", "dependencias", "registro", "renombramiento", "pipeline"]
claves: ["dependencia nombre", "WAR", "WAW", "renombramiento", "registros"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf", "repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[registro]] · [[renombramiento]]

Las dependencias de nombre (antidependencia WAR y dependencia de salida WAW) surgen por reutilización de registros. El renombramiento de registros (estático en compilador o dinámico en hardware tipo Tomasulo) asigna registros físicos distintos a cada escritura, eliminando estos falsos conflictos.

> Con respecto a las dependencias de nombre… c) Se eliminan mediante renombramiento
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[dependencias-de-nombre-war-waw-se-eliminan-con-renombramient]] · [[dependencias-de-nombre-se-eliminan-mediante-renombramiento-d]] · [[definicion-de-dependencia-de-nombre-waw-y-war]]

## Ampliación (2026-11-18, )
Las dependencias de nombre (WAW - salida, WAR - antidependencia) no son dependencias reales de datos, sino artefactos por reutilización de registros. Se eliminan asignando registros físicos distintos a cada escritura (renombramiento), permitiendo ejecución fuera de orden.
