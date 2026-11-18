---
tipo: "dato"
titulo: "Código para planificación superescalar con dependencias RAW, WAR, WAW"
temas: ["ac", "pipeline"]
claves: ["LW R1", "DADD R3", "DSUB R6", "LW R2", "DSUB R9", "DADD R4", "DSUB R2", "dependencias registros R1 R2 R3 R4 R5 R6 R7 R9 R10"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]]

Dependencias en el código: RAW: (1->? ninguno usa R1 salvo quizás salto, pero no hay), (4->5 por R2), (5->7 por R2), (2->? R3 no usado), (3->? R6 no usado), (6->? R4 usado en 3? no, 3 antes), (6->7? no). WAR: (5 escribe R9, 5 lee R9 -> RAW en misma instrucción), (7 escribe R2, 5 lee R2 -> RAW 4->5->7), (6 escribe R4, 3 lee R4 -> WAR: 3 antes que 6, pero 3 lee R4, 6 escribe R4 -> antidependencia 3->6). WAW: (4 y 7 escriben R2), (5 y 7? 5 escribe R9, 7 escribe R2). Con renombramiento, WAR/WAW eliminados. Sin renombramiento, emisión fuera de orden debe respetar orden original para WAR/WAW.

> LW   R1, 0(R0) / DADD R3, R5, R2 / DSUB R6, R7, R4 / LW   R2, 0(R10) / DSUB R9, R9, R2 / DADD R4, R4, R5 / DSUB R2, R2, R5
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[banco-de-registros-en-pipeline-mips-se-accede-en-etapas-id-y]]
