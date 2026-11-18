---
tipo: "receta"
titulo: "Desenrollado y planificación sin stalls del bucle MIPS64 (Ejercicio 1b)"
temas: ["ac", "loop-unrolling", "mips64", "pipeline", "scheduling", "stalls"]
claves: ["desenrollado", "unrolling", "planificación", "stalls", "MIPS64", "forwarding", "delayed branch"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop-unrolling]] · [[mips64]] · [[pipeline]] · [[scheduling]] · [[stalls]]

Stalls críticos: LW→DADD (1 ciclo). Para eliminarlos, separar LW y DADD dependiente con otras instrucciones. Desenrollar 2 veces da 2 cargas (I1,I3) y 2 DADDs (I2,I4) que pueden intercalarse. Versión desenrollada 2x: read: LW R6,0(R1); LW R7,4(R1); DADD R3,R3,R6; DADD R4,R4,R7; SLT R8,R7,R6; DADD R5,R5,R8; LW R6,8(R1); LW R7,12(R1); DADD R3,R3,R6; DADD R4,R4,R7; SLT R8,R7,R6; DADD R5,R5,R8; DADDUI R1,R1,#16; BNE R1,R2,read. Planificación sin stalls (reordenando): read: LW R6,0(R1); LW R7,4(R1); DADDUI R1,R1,#16; DADD R3,R3,R6; DADD R4,R4,R7; SLT R8,R7,R6; DADD R5,R5,R8; LW R6,0(R1); LW R7,4(R1); DADD R3,R3,R6; DADD R4,R4,R7; SLT R8,R7,R6; DADD R5,R5,R8; BNE R1,R2,read. (Ajustar offsets y registro base según desenrollado).

> b) Unroll the loop the minimum number of times to schedule it without stalls, and keep in mind that the program behavior must be preserved. Show the unrolled version: read: Show the scheduled version (without stalls): read:
> — `repo:datos/temarios/AC/examenes/June2021.pdf`

Relacionado: [[analisis-de-stalls-en-bucle-mips64-con-forwarding-y-ramas-re]]
