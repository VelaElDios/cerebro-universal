---
tipo: "concepto"
titulo: "Tipos de dependencias en código FP MIPS64 para Tomasulo (RAW, WAR, WAW)"
temas: ["ac", "dependencias", "pipeline", "tomasulo"]
claves: ["RAW", "WAR", "WAW", "dependencia verdadera", "antidependencia", "dependencia de salida", "F2 F4 F6 F8 F10 F0"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[pipeline]] · [[tomasulo]]

En el código dado: I1 L.D F2,0(R1); I2 L.D F4,8(R1); I3 L.D F6,16(R1); I4 ADD.D F8,F2,F4; I5 MUL.D F10,F2,F6; I6 DIV.D F0,F12,F8; I7 S.D F0,32(R1). Dependencias RAW (verdaderas): I1→I4 (F2), I1→I5 (F2), I2→I4 (F4), I3→I5 (F6), I4→I6 (F8), I6→I7 (F0). No hay WAR ni WAW entre estas instrucciones porque cada registro destino es único (F2,F4,F6,F8,F10,F0) y no se reutilizan como fuente tras ser destino en otra instrucción distinta. R1 se usa solo como base en cargas/almacenamiento sin modificarse.

> Identify the dependencies between instructions and indicate their type in the following table: Instruction 1 Instruction 2 Type of dependency
> — `repo:datos/temarios/AC/examenes/June2023.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-war-siempre-genera-hazard-war]]
