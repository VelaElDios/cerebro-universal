---
tipo: "concepto"
titulo: "Hazard WAR corresponde a antidependencia (dependencia de nombre)"
temas: ["ac", "dependencias", "hazards", "pipeline"]
claves: ["WAR", "antidependencia", "dependencia nombre", "hazard"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[hazards]] · [[pipeline]]

WAR (Write After Read) es una antidependencia: una instrucción escribe un registro/memoria que una instrucción anterior lee. Es una dependencia de nombre (no de datos verdadera) y se elimina mediante renombramiento de registros.

> Un riesgo de tipo WAR: Se corresponde con una antidependencia
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[antidependencia-war-siempre-genera-hazard-war]] · [[que-es-un-riesgo-war-y-a-que-dependencia-corresponde]] · [[antidependencia-siempre-genera-hazard-war-en-pipeline-in-ord]]
