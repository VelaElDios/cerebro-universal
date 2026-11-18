---
tipo: "dato"
titulo: "Secuencia de instrucciones MIPS64 para simulación Tomasulo Problema 3a"
temas: ["ac", "instrucciones", "mips64", "simulacion", "tomasulo"]
claves: ["DIV.D F0 F2 F4", "ADD.D F2 F6 F8", "ADD.D F0 F4 F8", "S.D F0 0(R1)", "MUL.D F2 F4 F0", "DIV.D F6 F8 F0", "L.D F6 0(R2)", "ADD.D F0 F6 F2", "MUL.D F2 F0 F8", "ADD.D F2 F0 F6"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[instrucciones]] · [[mips64]] · [[simulacion]] · [[tomasulo]]

Las 10 instrucciones a simular en orden de programa: 1) DIV.D F0, F2, F4 2) ADD.D F2, F6, F8 3) ADD.D F0, F4, F8 4) S.D F0, 0(R1) 5) MUL.D F2, F4, F0 6) DIV.D F6, F8, F0 7) L.D F6, 0(R2) 8) ADD.D F0, F6, F2 9) MUL.D F2, F0, F8 10) ADD.D F2, F0, F6. El ROB está inicialmente vacío.

> DIV.D F0, F2, F4; ADD.D F2, F6, F8; ADD.D F0, F4, F8; S.D F0, 0(R1); MUL.D F2, F4, F0; DIV.D F6, F8, F0; L.D F6, 0(R2); ADD.D F0, F6, F2; MUL.D F2, F0, F8; ADD.D F2, F0, F6
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf` (cita sin comprobar)

Relacionado: [[configuracion-hardware-tomasulo-con-especulacion-para-examen]] · [[restricciones-de-uso-del-bus-de-datos-comun-y-recursos-en-to]]
