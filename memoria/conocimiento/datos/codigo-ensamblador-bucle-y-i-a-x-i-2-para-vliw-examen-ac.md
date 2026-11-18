---
tipo: "dato"
titulo: "Código ensamblador bucle y(i)=A*x(i)² para VLIW examen AC"
temas: ["ac", "ensamblador", "vliw"]
claves: ["LF F2 0(R2)", "MULTF F4 F2 F2", "MULTF F6 F4 F1", "SF 0(R4) F6", "ADDI R2 R2 #4", "ADDI R4 R4 #4", "ADDI R3 R3 #1", "BNE R3 R1 BUCLE"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Diciembre2010.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ensamblador]] · [[vliw]]

Kernel del bucle (8 instrucciones): 1) LF F2, 0(R2) - carga x(i). 2) MULTF F4, F2, F2 - x². 3) MULTF F6, F4, F1 - A*x² (F1=A). 4) SF 0(R4), F6 - almacena y(i). 5) ADDI R2, R2, #4 - siguiente x. 6) ADDI R4, R4, #4 - siguiente y. 7) ADDI R3, R3, #1 - contador++. 8) BNE R3, R1, BUCLE - salto si R3!=R1 (R1=N elementos).

> LF    F2, 0(R2)                  // R2 es la dirección el elemento x(i)\n                MULTF F4, F2, F2\n                MULTF F6, F4, F1                 // F1 contiene el valor de A\n                SF    0(R4), F6                  // R4 es la dirección el elemento y(i)
> — `repo:datos/temarios/AC/examenes/Diciembre2010.pdf` (cita sin comprobar)

Relacionado: [[problema-examen-ac-planificacion-vliw-para-bucle-y-i-a-x-i-2]] · [[latencias-vliw-examen-ac-para-planificacion-bucle-polinomico]] · [[bucle-de-calculo-y-i-a-x-i-2-en-ensamblador-mips64]] · [[desenrollado-4x-de-bucle-mips64-fp-con-renombrado-de-registr]]
