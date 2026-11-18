---
tipo: "concepto"
titulo: "Definición de dependencia de salida (WAW)"
temas: ["ac", "dependencias", "salida", "waw"]
claves: ["dependencia de salida", "WAW", "mismo registro", "escritura"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2011.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[salida]] · [[waw]]

Una dependencia de salida (Write After Write, WAW) ocurre cuando dos instrucciones escriben en el mismo registro o posición de memoria, y la segunda (j) debe escribir después de la primera (i) para mantener la semántica correcta. Se resuelve con renombramiento.

> Dadas dos instrucciones i y j (j lógicamente después de i) existe una dependencia de salida entre ellas si: a) La instrucción i produce un resultado que usa la instrucción j b) La instrucción j escribe sobre un registro que lee la instrucción i c) Las dos instrucciones i y j escriben sobre el mismo registro d) Ninguna de las anteriores
> — `repo:datos/temarios/AC/examenes/Junio2011.pdf`

Relacionado: [[antidependencia-war-siempre-genera-hazard-war]] · [[definicion-de-dependencia-de-salida-waw-entre-dos-instruccio]] · [[dependencia-de-salida-waw-dos-instrucciones-escriben-mismo-r]] · [[waw-corresponde-a-dependencia-de-salida]]
