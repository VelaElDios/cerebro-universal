---
tipo: "dato"
titulo: "Dependencias en la secuencia de instrucciones del examen June 2021"
temas: ["ac", "pipeline", "scoreboard", "tomasulo"]
claves: ["RAW", "WAW", "WAR", "dependencia memoria", "F0 F2 F4 F6 F8"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[scoreboard]] · [[tomasulo]]

Análisis de dependencias de la secuencia: RAW (verdaderas): F0 de instr1→instr4,instr6; F2 de instr2→instr4; F6 de instr4→instr5; F8 de instr5→instr6 (y instr6 lee F8 viejo antes de escribir nuevo F8). WAW (salida): F4 escrito en instr3 (carga) e instr5 (MUL.D) - en Scoreboard/Tomasulo básico requiere espera; en Tomasulo especulativo resuelto por renombrado en ROB. WAR (anti): F8 leído en instr5 (MUL.D) y escrito en instr6 (ADD.D) - en Scoreboard requiere espera en Write result de instr5 hasta que instr6 lea; en Tomasulo resuelto porque instr5 captura valor/etiqueta en Issue. Memoria: instr1-3 cargan de 0(R1),4(R1),8(R1); instr7 almacena en 0(R1) [o 0(R4) en parte1] - posible solapamiento de direcciones (0(R1) vs 0(R1)) que exige orden de memoria en store buffer/ROB.

> L.D    F0, 0(R1) / L.D    F2, 4(R1) / L.D    F4, 8(R1) / MUL.D F6, F0, F2 / MUL.D F4, F8, F6 / ADD.D F8, F0, F8 / S.D    F4, 0(R1)
> — `repo:datos/temarios/AC/examenes/June2021.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-war-siempre-genera-hazard-war]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]]
