---
tipo: "dato"
titulo: "Código del bucle VLIW para planificación (cargas FP, MUL.S, ADD.S, stores, enteros, salto)"
temas: ["ac", "vliw"]
claves: ["L.S", "MUL.S", "ADD.S", "S.S", "DADDUI", "BNEZ", "F1-F5", "R1-R4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[vliw]]

Bucle original de 11 instrucciones: dos cargas FP (L.S) desde R1 y R2 a F1, F2; multiplicación FP (MUL.S) F4=F2*F1 (6 ciclos EX); store FP (S.S) F4 a 0(R1); carga FP (L.S) F3 desde R3; suma FP (ADD.S) F5=F4+F3 (4 ciclos EX, depende de MUL.S); store FP (S.S) F5 a 0(R3); cuatro enteros DADDUI incrementando R1,R2,R3 en 4 y decrementando R4 en 1; salto condicional BNEZ R4,Loop (rama del bucle). Dependencias RAW: F1,F2 → MUL.S; MUL.S → S.S(F4) y ADD.S; F3 → ADD.S; ADD.S → S.S(F5); R1,R2,R3,R4 actualizados por DADDUI para siguiente iteración.

> Loop: L.S F1, 0(R1); L.S F2, 0(R2); MUL.S F4, F2, F1; S.S F4, 0(R1); L.S F3, 0(R3); ADD.S F5, F4, F3; S.S F5, 0(R3); DADDUI R1, R1, #4; DADDUI R2, R2, #4; DADDUI R3, R3, #4; DADDUI R4, R4, #-1; BNEZ R4, Loop
> — `repo:datos/temarios/AC/examenes/January2019.pdf` (cita sin comprobar)

Relacionado: [[planificacion-scheduling-de-bucle-en-vliw-con-forwarding-y-d]] · [[codigo-del-bucle-a-planificar-en-vliw-examen-ac-enero-2017]] · [[planificacion-vliw-de-bucle-con-6-unidades-funcionales-exame]]
