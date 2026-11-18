---
tipo: "concepto"
titulo: "Antidependencia (WAR) siempre genera hazard WAR"
temas: ["ac", "dependencias", "pipeline"]
claves: ["antidependencia", "WAR", "hazard"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]]

Por definición, una antidependencia (escritura después de lectura, WAR) es una dependencia de nombre donde una instrucción posterior escribe un registro que una instrucción anterior lee. En pipeline, esto genera un hazard WAR si la escritura ocurre antes de la lectura. La respuesta correcta es c) A WAR hazard.

> Any antidependence always leads to: a) A WAW hazard b) A RAW hazard c) A WAR hazard d) None of the above
> — `repo:datos/temarios/AC/examenes/June2018.pdf`

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]]
