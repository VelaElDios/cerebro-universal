---
tipo: "receta"
titulo: "Diagrama pipeline superscalar: ejecución fuera de orden sin renombramiento, escritura en orden"
temas: ["ac", "in-order-write", "out-of-order", "pipeline", "sin-renombramiento", "superscalar"]
claves: ["out-of-order execution", "no register renaming", "in-order write", "WAR/WAW hazards", "scoreboard"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[in-order-write]] · [[out-of-order]] · [[pipeline]] · [[sin-renombramiento]] · [[superscalar]]

Diferencias vs in-order: Execute puede reordenar instrucciones listas (operandos disponibles, unidad libre). Pero: 1) Sin renombramiento → peligros WAR/WAW reales en registros arquitectónicos frenan emisión/ejecución. 2) Write en orden → instrucción no puede hacer Write hasta que todas las anteriores hayan hecho Write. 3) Decode sigue en orden (4/ciclo). Ejemplo: I3 (DSUB R6,R7,R8) puede ejecutarse antes que I2 (DADD R4,R1,R3) si R1 no listo, pero I3 escribe R6 → si I4 usa R6, hay RAW. WAW: I1 escribe R1, I6 escribe R1 → I6 no puede Write hasta I1 Write.

> b) Ejecución fuera de orden, sin capacidad de renombramiento, y escritura en orden
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[diagrama-pipeline-superscalar-grado-4-ejecucion-en-orden-y-e]]
