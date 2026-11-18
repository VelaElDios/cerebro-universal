---
tipo: "receta"
titulo: "Secuencia de instrucciones de referencia para ejercicios de Scoreboard y Tomasulo (examen AC June 2021)"
temas: ["ac", "pipeline", "scoreboard", "tomasulo"]
claves: ["L.D F0 0(R1)", "L.D F2 4(R1)", "L.D F4 8(R1)", "MUL.D F6 F0 F2", "MUL.D F4 F8 F6", "ADD.D F8 F0 F8", "S.D F4 0(R1)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[scoreboard]] · [[tomasulo]]

Secuencia canónica de 7 instrucciones FP usada en el examen June 2021 para comparar Scoreboard, Tomasulo básico y Tomasulo especulativo. Instrucciones: 1) L.D F0,0(R1) 2) L.D F2,4(R1) 3) L.D F4,8(R1) 4) MUL.D F6,F0,F2 5) MUL.D F4,F8,F6 6) ADD.D F8,F0,F8 7) S.D F4,0(R1) [en parte 1 es 0(R4), en partes 2-3 es 0(R1)]. Presenta dependencias RAW (F0,F2,F6,F8), WAW (F4 en instr 3 y 5), WAR (F8 en instr 5 y 6), y dependencia de memoria entre cargas y store.

> L.D    F0, 0(R1) / L.D    F2, 4(R1) / L.D    F4, 8(R1) / MUL.D F6, F0, F2 / MUL.D F4, F8, F6 / ADD.D F8, F0, F8 / S.D    F4, 0(R1)
> — `repo:datos/temarios/AC/examenes/June2021.pdf` (cita sin comprobar)

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[configuracion-de-procesador-tomasulo-con-especulacion-del-ej]] · [[dependencias-en-la-secuencia-de-instrucciones-del-examen-jun]] · [[secuencia-de-instrucciones-para-simulacion-tomasulo-con-div]] · [[secuencia-de-instrucciones-fp-del-examen-para-tomasulo-10-in]]
