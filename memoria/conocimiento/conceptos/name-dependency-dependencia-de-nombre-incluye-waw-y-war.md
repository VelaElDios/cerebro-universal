---
tipo: "concepto"
titulo: "Name dependency (dependencia de nombre) incluye WAW y WAR"
temas: ["ac", "dependencias", "ilp", "pipeline"]
claves: ["name dependency", "WAW", "WAR", "output dependence", "antidependence"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[ilp]] · [[pipeline]]

Una dependencia de nombre (name dependency) ocurre cuando dos instrucciones usan el mismo registro o posición de memoria pero no hay flujo de datos real entre ellas. Incluye dos casos: (a) WAW (output dependence): ambas escriben en el mismo registro; (b) WAR (antidependence): la segunda escribe en un registro que la primera lee. Ambas se resuelven con renombrado de registros en planificación dinámica o fuera de orden.

> Given two instructions i and j (j logically after i), there is a name dependency if: c) Both a and b are true.
> — `repo:datos/temarios/AC/examenes/June 2024.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]] · [[definicion-de-dependencia-de-salida-waw-entre-dos-instruccio]] · [[definicion-de-dependencia-de-nombre-waw-y-war]] · [[definicion-de-dependencia-de-nombre-anti-y-salida]] · [[dependencias-de-nombre-se-eliminan-mediante-renombramiento-d]]
