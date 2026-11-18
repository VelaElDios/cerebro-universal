---
tipo: "concepto"
titulo: "Bucle de cálculo y(i) = A * x(i)^2 en ensamblador MIPS64"
temas: ["ac", "ensamblador", "pipeline"]
claves: ["L.D", "MUL.D", "S.D", "DADDUI", "BNE", "bucle", "FP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ensamblador]] · [[pipeline]]

El bucle consta de 9 instrucciones por iteración: una carga FP (L.D), dos multiplicaciones FP (MUL.D), una almacenamiento FP (S.D), tres instrucciones enteras de incremento de punteros/contador (DADDUI) y una rama condicional (BNE). Los registros usados: F2 (carga x(i)), F4 (x(i)^2), F6 (resultado A*x(i)^2), F8 (constante A), R2 (puntero a x), R4 (puntero a y), R3 (contador), R1 (límite). La dependencia de datos principal: L.D → MUL.D (F2), MUL.D → MUL.D (F4), MUL.D → S.D (F6). Dependencias de control: BNE salta a Loop.

> Loop: L.D F2, 0(R2) // R2 is the address of the element x(i) MUL.D F4, F2, F2 MUL.D F6, F4, F8 // F8 contains the value of A S.D F6, 0(R4) // R4 is the address of the element y(i) DADDUI R2, R2, #4 DADDUI R4, R4, #4 DADDUI R3, R3, #1 BNE R3, R1, Loop // R1 contains the number of elements in x
> — `repo:datos/temarios/AC/examenes/June 2024.pdf`

Relacionado: [[codigo-ensamblador-bucle-y-i-a-x-i-2-para-vliw-examen-ac]] · [[desenrollado-4x-de-bucle-mips64-fp-con-renombrado-de-registr]] · [[analisis-de-dependencias-y-planificacion-de-bucle-mips64-con]]
