---
tipo: "dato"
titulo: "Secuencia de instrucciones para simulación Tomasulo examen enero 2023"
temas: ["ac", "tomasulo"]
claves: ["MUL.D", "SUB.D", "L.D", "DIV.D", "ADD.D", "S.D", "F4", "F6", "F2", "F10", "F0", "F8", "R1", "R2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

Código a simular en el ejercicio 2a. Ocho instrucciones: MUL.D F4,F6,F2; SUB.D F6,F4,F10; L.D F4,0(R1); DIV.D F0,F4,F6; L.D F8,0(R2); SUB.D F2,F8,F0; ADD.D F0,F8,F2; S.D F0,0(R1). Hay dependencias RAW (F4, F6, F0, F8), WAW (F4 escrito por MUL.D y L.D), WAR (F6 leído por SUB.D y luego escrito por SUB.D anterior), y acceso a memoria con misma dirección (R1).

> MUL.D F4,F6,F2 SUB.D F6,F4,F10 L.D F4,0(R1) DIV.D F0,F4,F6 L.D F8,0(R2) SUB.D F2,F8,F0 ADD.D F0,F8,F2 S.D F0,0(R1)
> — `repo:datos/temarios/AC/examenes/January2023.pdf`

Relacionado: [[secuencia-de-instrucciones-para-simulacion-tomasulo-problema]] · [[secuencia-de-instrucciones-fp-del-examen-para-tomasulo-10-in]] · [[secuencia-de-10-instrucciones-mips64-fp-para-ejercicio-3-tom]]
