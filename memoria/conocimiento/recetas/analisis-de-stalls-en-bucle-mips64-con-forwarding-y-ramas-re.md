---
tipo: "receta"
titulo: "Análisis de stalls en bucle MIPS64 con forwarding y ramas resueltas en ID (Ejercicio 1a)"
temas: ["ac", "delayed-branch", "forwarding", "hazards", "mips64", "pipeline", "stalls"]
claves: ["LW", "DADD", "SLT", "BNE", "forwarding", "ID stage", "branch resuelto en ID", "delayed branch"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[delayed-branch]] · [[forwarding]] · [[hazards]] · [[mips64]] · [[pipeline]] · [[stalls]]

Código: I1:LW R6,0(R1); I2:DADD R3,R3,R6; I3:LW R7,4(R1); I4:DADD R4,R4,R7; I5:SLT R8,R7,R6; I6:DADD R5,R5,R8; I7:DADDUI R1,R1,#8; I8:BNE R1,R2,read. Con forwarding y resolución en ID: I1→I2 (RAW R6): LW produce en MEM, DADD necesita en EX → 1 stall (EX espera dato de MEM). I2→I5 (RAW R6): DADD produce en WB, SLT necesita en ID → 0 stalls (escritura/lectura mismo ciclo). I3→I4 (RAW R7): igual que I1→I2 → 1 stall. I3→I5 (RAW R7): 0 stalls. I4→I6 (RAW R8): DADD produce WB, SLT consume ID → 0 stalls. I5→I6 (RAW R8): SLT produce WB, DADD consume ID → 0 stalls. I7→I8 (RAW R1): DADDUI produce WB, BNE consume ID → 0 stalls. Rama resuelta en ID con delayed branch → slot de retardo útil. Stalls: I1→I2:1, I2→I3:0, I3→I4:1, I4→I5:0, I5→I6:0, I6→I7:0, I7→I8:0, I8→next:0 (delayed branch).

> Assume that we have a pipelined processor with following characteristics: • Operand forwarding is supported. • A value can be written and read from a register in the same clock cycle. • All the dependences are detected and solved in the ID stage. • Branches are completely solved in the ID stage. • Delayed branch is supported.
> — `repo:datos/temarios/AC/examenes/June2021.pdf`

Relacionado: [[desenrollado-y-planificacion-sin-stalls-del-bucle-mips64-eje]] · [[planificacion-de-bucle-jacobsthal-en-pipeline-mips64-con-uni]] · [[como-calcular-stalls-en-pipeline-mips64-con-operand-forwardi]]
