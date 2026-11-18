---
tipo: "concepto"
titulo: "Dependencia de salida (WAW): dos instrucciones escriben mismo registro/memoria"
temas: ["ac", "dependencias", "riesgos", "waw"]
claves: ["dependencia salida", "WAW", "escritura mismo registro", "escritura misma memoria"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencias]] · [[riesgos]] · [[waw]]

WAW (Write After Write): i escribe, luego j escribe en la misma ubicación. En pipeline in-order no hay riesgo WAW porque i escribe antes que j; en out-of-order o con especulación puede haber riesgo si j escribe antes que i. Se resuelve con renombrado de registros o ROB.

> Dadas dos instrucciones i y j (j lógicamente después de i) existe una dependencia de salida entre ellas si: c) Las dos instrucciones i y j escriben sobre el mismo registro o posición de memoria
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[definicion-de-dependencia-de-salida-waw-entre-dos-instruccio]] · [[definicion-de-dependencia-de-salida-waw]] · [[waw-corresponde-a-dependencia-de-salida]]
