---
tipo: "concepto"
titulo: "Clasificación de dependencias en bucle: antidependencia (WAR) entre store e incremento de puntero"
temas: ["ac", "dependencias", "pipeline", "war"]
claves: ["antidependencia", "WAR", "dependencia nombre", "bucle", "store", "addi"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]] · [[war]]

I3 (sw x4, 0(x2)) lee el registro x2; I4 (addi x2, x2, 4) escribe x2. Como I4 escribe un registro que I3 lee y I3 va antes en orden lógico, es una antidependencia (WAR) dentro de la misma iteración. No hay dependencia de datos (RAW) ni de salida (WAW) entre ellas.

> Considera una iteración del siguiente bucle: (I1) Bucle: lw x4, 0(x2) (I2) add x4, x4, x3 (I3) sw x4, 0(x2) (I4) addi x2, x2, 4 ... b. Hay una antidependencia entre I3 e I4
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]]
