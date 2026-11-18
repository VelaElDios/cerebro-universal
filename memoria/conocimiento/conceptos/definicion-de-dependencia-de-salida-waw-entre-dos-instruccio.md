---
tipo: "concepto"
titulo: "Definición de dependencia de salida (WAW) entre dos instrucciones"
temas: ["ac", "dependencias", "pipeline"]
claves: ["WAW", "output dependence", "mismo registro", "misma posición memoria"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf", "repo:datos/temarios/AC/examenes/Noviembre2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]]

La dependencia de salida (WAW, Write After Write) ocurre cuando la instrucción i y la instrucción j (i antes que j) escriben en el mismo registro o posición de memoria. Obliga a que j escriba después de i para preservar el valor final correcto. Se resuelve con renombrado de registros o reordenación.

> Given two instructions i and j (i precedes j), there is an output dependence between them if… a) Both instructions update the same register or memory position.
> — `repo:datos/temarios/AC/examenes/January2018.pdf`

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]] · [[definicion-de-dependencia-de-salida-waw]] · [[dependencia-de-salida-waw-dos-instrucciones-escriben-mismo-r]] · [[waw-corresponde-a-dependencia-de-salida]]

## Ampliación (2026-11-18, )
Dependencia de salida (WAW - Write After Write): la instrucción j escribe en un registro que también escribe la instrucción i (predecesora). Es una dependencia de nombre (falsa) que se elimina mediante renombramiento de registros. En pipeline in-order genera hazard WAW si la escritura de j ocurre antes que la de i.
