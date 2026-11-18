---
tipo: "concepto"
titulo: "Definición de dependencia de datos (RAW) entre instrucciones"
temas: ["ac", "dependencias", "pipeline"]
claves: ["dependencia datos", "RAW", "produce resultado", "usa resultado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf", "repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]]

Dependencia verdadera (RAW): i escribe un registro/memoria que j lee después. Es la única dependencia real de flujo de datos; las demás (WAR, WAW) son dependencias de nombre eliminables con renombramiento.

> Existe una dependencia de datos entre dos instrucciones i y j (j lógicamente después de i) si : c) La instrucción i produce un resultado que usa la instrucción j
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]]

## Ampliación (2026-11-18, )
Dependencia de datos verdadera (RAW): i produce un resultado que j puede usar. i precede a j en orden de programa. Opción a). WAW = dependencia de salida (ambas escriben mismo registro). WAR = antidependencia (j escribe lo que i lee).
