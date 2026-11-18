---
tipo: "concepto"
titulo: "Antidependencia (WAR) entre instrucciones consecutivas en RISC-V"
temas: ["ac", "dependencias", "pipeline", "war"]
claves: ["antidependencia", "WAR", "add sub and", "registro destino"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]] · [[war]]

I1 lee x1 (fuente), I2 escribe x1 (destino). Esto es una antidependencia (WAR: Write After Read). I2 escribe x1, I3 lee x1 → dependencia RAW. No hay dependencia de salida (WAW) entre I2 e I3 porque I3 escribe en x6. La opción correcta identifica la antidependencia entre I1 e I2.

> Considera el siguiente código: (I1) add x5, x1, x2 (I2) sub x1, x3, x4 (I3) and x6, x1, x7 ¿Cuál de las siguientes afirmaciones es correcta? ... Existe una antidependencia entre I1 e I2
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf` (cita sin comprobar)

Relacionado: [[dependencia-raw-en-pipeline-risc-v-resuelta-con-adelantamien]] · [[antidependencia-siempre-genera-hazard-war-en-pipeline-in-ord]]
