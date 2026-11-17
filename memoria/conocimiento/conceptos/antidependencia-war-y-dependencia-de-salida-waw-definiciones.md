---
tipo: "concepto"
titulo: "Antidependencia (WAR) y dependencia de salida (WAW) definiciones"
temas: ["ac", "dependencias", "riesgos"]
claves: ["antidependencia", "WAR", "dependencia salida", "WAW", "RAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2011.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[dependencias]] · [[riesgos]]

Antidependencia (WAR): j (posterior) escribe un operando que i (anterior) lee. Dependencia de salida (WAW): ambas escriben el mismo operando. Dependencia de datos verdadera (RAW): i produce, j consume.

> La instrucción j escribe sobre un registro o una posición de memoria que lee la instrucción i
> — `repo:datos/temarios/AC/examenes/Enero2011.pdf`
