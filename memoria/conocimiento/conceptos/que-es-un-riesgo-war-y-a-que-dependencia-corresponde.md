---
tipo: "concepto"
titulo: "Qué es un riesgo WAR y a qué dependencia corresponde"
temas: ["ac", "hazards", "pipeline", "war"]
claves: ["WAR", "hazard", "antidependencia", "riesgo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2011.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[hazards]] · [[pipeline]] · [[war]]

WAR = Write After Read = antidependencia. Ocurre cuando una instrucción posterior escribe un registro que una anterior lee. En pipeline in-order genera hazard si la escritura ocurre antes de la lectura. Respuesta correcta: "Ninguna de las anteriores" (debería ser "dependencia de antidependencia" o similar, no está en opciones a-c).

> Un riesgo tipo WAR a) Se corresponde con una dependencia de datos b) Se corresponde con una dependencia de salida c) Se corresponde con una dependencia de control
> — `repo:datos/temarios/AC/examenes/Noviembre2011.pdf`

Relacionado: [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[antidependencia-siempre-genera-hazard-war-en-pipeline-in-ord]] · [[antidependencia-war-siempre-genera-hazard-war]] · [[hazard-war-corresponde-a-antidependencia-dependencia-de-nomb]]
