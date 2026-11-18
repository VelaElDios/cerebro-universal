---
tipo: "concepto"
titulo: "Tomasulo sin especulación: detenciones en escritura por riesgos estructurales en el CDB"
temas: ["ac", "riesgos estructurales", "tomasulo"]
claves: ["Tomasulo", "sin especulación", "escritura", "riesgo estructural", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[riesgos estructurales]] · [[tomasulo]]

En Tomasulo sin especulación, la emisión nunca se detiene por WAW/WAR gracias al renombramiento. Sin embargo, en la fase de escritura (Write Result) puede haber riesgo estructural si varias unidades funcionales intentan usar el Bus de Datos Común (CDB) en el mismo ciclo; entonces se detiene la escritura hasta que el CDB esté libre.

> En la técnica de Tomasulo sin especulación: a) Se pueden producir detenciones en la fase de emisión debido a riesgos WAW b) Se pueden producir detenciones en la fase de escritura debido a riesgos estructurales c) Se pueden producir detenciones en la fase de escritura debido a riesgos WAR d) No se pueden producir nunca detenciones debido a riesgos estructurales
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[comparativa-tomasulo-vs-marcador-scoreboard]]
