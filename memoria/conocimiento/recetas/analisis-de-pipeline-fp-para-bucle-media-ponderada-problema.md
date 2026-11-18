---
tipo: "receta"
titulo: "Análisis de pipeline FP para bucle media ponderada (Problema 1) con latencias L.D=1, MUL.D=3, ADD.D=2, DIV.D=5, S.D=1"
temas: ["ac", "adelantamiento", "coma-flotante", "mips64", "pipeline"]
claves: ["L.D", "MUL.D", "ADD.D", "DIV.D", "S.D", "latencias", "adelantamiento", "riesgos RAW", "bucle"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[adelantamiento]] · [[coma-flotante]] · [[mips64]] · [[pipeline]]

Esquema de dependencias y ciclos de espera con adelantamiento (resultado disponible al final de EX): 1) L.D F1 (EX 1c) → MUL.D F1 necesita F1: MUL.D espera en ID hasta que L.D termine EX → 1 ciclo parada. 2) MUL.D F1 (EX 3c) → ADD.D F3 necesita F1: ADD.D espera 3 ciclos. 3) MUL.D F2 (EX 3c) → ADD.D F3 necesita F2: ADD.D espera 3 ciclos (mismo). 4) ADD.D F3 (EX 2c) → DIV.D F3 necesita F3: DIV.D espera 2 ciclos. 5) DIV.D F3 (EX 5c) → S.D F3 necesita F3: S.D espera 5 ciclos. Enteros (DADDUI, BNEZ) 1 ciclo, saltos resueltos en ID. Iteración solapada: siguiente L.D puede empezar mientras DIV.D/S.D de iteración anterior están en EX/MEM. CPI teórico >1 por paradas RAW en cadena FP.

> Loop: L.D F1, 0(R1) L.D F2, 0(R2) MUL.D F1, F1, F10 MUL.D F2, F2, F20 ADD.D F3, F1, F2 DIV.D F3, F3, F30 S.D F3, 0(R3) DADDUI R1, R1, #8 DADDUI R2, R2, #8 DADDUI R3, R3, #8 DADDUI R4, R4, #-1 BNEZ R4, Loop ... las unidades funcionales de suma, multiplicación y división en coma flotante están totalmente segmentadas y emplean, respectivamente, 2, 3 y 5 ciclos.
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf` (cita sin comprobar)

Relacionado: [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]]
