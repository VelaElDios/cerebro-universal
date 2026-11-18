---
tipo: "dato"
titulo: "Código del bucle y valores iniciales de registros para VLIW Problema 3b"
temas: ["ac", "bucle", "desenrollado", "registros-iniciales", "vliw"]
claves: ["L.D F2 0(R1)", "L.D F4 0(R2)", "ADD.D F6 F2 F4", "MUL.D F8 F2 F4", "DIV.D F0 F8 F6", "S.D F0 0(R2)", "DADDUI R1 R1 #8", "DADDUI R2 R2 #8", "DADDUI R10 R10 #-1", "BNEZ R10 Loop", "R1=0x1000", "R2=0x1500", "R10=0x3C"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucle]] · [[desenrollado]] · [[registros-iniciales]] · [[vliw]]

Bucle de 10 instrucciones que procesa arrays de double (8 bytes por elemento, de ahí el incremento #8 en R1 y R2). R10 es contador de iteraciones inicializado a 0x3C (60 decimal). El bucle se ejecuta 60 veces. Se pide desenrollar 4 veces (4 iteraciones por bucle desenrollado, resultando en 15 iteraciones del bucle desenrollado).

> Loop: L.D F2, 0(R1); L.D F4, 0(R2); ADD.D F6, F2, F4; MUL.D F8, F2, F4; DIV.D F0, F8, F6; S.D F0, 0(R2); DADDUI R1, R1, #8; DADDUI R2, R2, #8; DADDUI R10, R10, #-1; BNEZ R10, Loop. Inicialmente el contenido de R1, R2 y R10 es: R1=0x1000, R2=0x1500 y R10=0x3C.
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf` (cita sin comprobar)

Relacionado: [[caracteristicas-del-procesador-vliw-del-examen-enero-2016-pr]]
