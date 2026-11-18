---
tipo: "concepto"
titulo: "Definición de dependencia de nombre (WAW y WAR)"
temas: ["ac", "dependencia-nombre", "dependencias"]
claves: ["dependencia nombre", "WAW", "WAR", "escritura misma ubicación", "escritura tras lectura"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencia-nombre]] · [[dependencias]]

La dependencia de nombre agrupa tanto la dependencia de salida (WAW: dos escrituras en mismo registro/memoria) como la antidependencia (WAR: escritura en registro que lee instrucción anterior). Ambas se resuelven con renombrado de registros en hardware (Tomasulo, ROB) o en compilador.

> Dadas dos instrucciones i y j (j lógicamente después de i), existe una dependencia de nombre si: a. Las dos instrucciones i y j escriben sobre el mismo registro o posición de memoria. b. La instrucción j escribe sobre un registro o una posición de memoria que lee la instrucción i. c. Las respuestas a y b son ciertas.
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf`

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]]
