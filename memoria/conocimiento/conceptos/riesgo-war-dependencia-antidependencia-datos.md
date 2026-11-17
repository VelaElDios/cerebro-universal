---
tipo: "concepto"
titulo: "Riesgo WAR = dependencia antidependencia (datos)"
temas: ["ac", "antidependencia", "riesgos", "war"]
claves: ["riesgo WAR", "antidependencia", "dependencia datos", "WAR"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[antidependencia]] · [[riesgos]] · [[war]]

WAR (Write After Read): j escribe en una ubicación que i lee (i antes que j lógicamente). Es una dependencia de datos (antidependencia). En pipeline in-order no hay riesgo WAR porque i lee en ID antes de que j escriba en WB; en out-of-order puede haber riesgo si j escribe antes de que i lea. Renombrado de registros lo elimina.

> Un riesgo de tipo WAR: c) Se corresponde con una dependencia de datos
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]]
