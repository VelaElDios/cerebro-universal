---
tipo: "concepto"
titulo: "Riesgo WAR corresponde a antidependencia"
temas: ["ac", "antidependencia", "pipeline", "riesgos", "war"]
claves: ["WAR", "antidependencia", "hazard", "WAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Octubre2010.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[antidependencia]] · [[pipeline]] · [[riesgos]] · [[war]]

WAR (Write After Read) = antidependencia: j escribe un registro que i lee. En pipeline in-order genera hazard porque j podría escribir antes de que i lea. Se elimina con renombramiento.

> Un riesgo tipo WAR a) Se corresponde con una dependencia de datos
> — `repo:datos/temarios/AC/examenes/Octubre2010.pdf`

Relacionado: [[antidependencia-siempre-genera-hazard-war-en-pipeline-in-ord]] · [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]]
