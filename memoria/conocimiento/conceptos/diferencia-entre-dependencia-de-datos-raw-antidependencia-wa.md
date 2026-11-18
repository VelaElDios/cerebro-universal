---
tipo: "concepto"
titulo: "Diferencia entre dependencia de datos (RAW), antidependencia (WAR) y dependencia de salida (WAW)"
temas: ["ac", "dependencias", "hazards", "pipeline"]
claves: ["RAW", "WAR", "WAW", "dependencia datos", "antidependencia", "dependencia salida"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2011.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[hazards]] · [[pipeline]]

a) = RAW (dependencia verdadera, flow dependence): i escribe, j lee. b) = WAR (antidependencia): j escribe, i lee (j después de i lógicamente). c) = WAW (dependencia de salida): ambas escriben. La definición correcta de dependencia de datos (RAW) es la a).

> Existe una dependencia de datos entre dos instrucciones i y j (j lógicamente después de i) si a) La instrucción i produce un resultado que usa la instrucción j b) La instrucción j escribe sobre un registro o una posición de memoria que lee la instrucción i c) Las dos instrucciones i y j escriben sobre el mismo registro o posición de memoria
> — `repo:datos/temarios/AC/examenes/Noviembre2011.pdf`

Relacionado: [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[antidependencia-siempre-genera-hazard-war-en-pipeline-in-ord]]
