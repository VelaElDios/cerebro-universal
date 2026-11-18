---
tipo: "dato"
titulo: "Código del bucle original para planificación (examen AC 2017/18)"
temas: ["ac", "bucle", "pipeline", "planificacion", "vector"]
claves: ["L.D F2 0(R1)", "MUL.D F4 F2 F0", "L.D F6 0(R2)", "ADD.D F6 F4 F6", "S.D F6 0(R2)", "DADDUI R1 R1 #-8", "DADDUI R2 R2 #-8", "SLTI R4 R1 fin", "BEQZ R4 Bucle"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucle]] · [[pipeline]] · [[planificacion]] · [[vector]]

Bucle que recorre vectores A y B (direcciones base en R1, R2, decremento de 8 bytes por elemento double). F0 contiene constante. Operaciones: carga A(i), multiplica por constante, carga B(i), suma, almacena resultado en B(i), actualiza punteros, compara con límite 'fin', salta si no terminado. Dependencias: RAW en F2 (L.D→MUL.D), F4 (MUL.D→ADD.D), F6 (L.D→ADD.D y ADD.D→S.D), R1/R2 (DADDUI→SLTI/BEQZ y DADDUI→siguiente L.D). Antidependencia WAR en F6 (L.D lee antes de que ADD.D escriba) y en R1/R2 (SLTI lee antes de DADDUI escriba).

> Bucle: L.D F2, 0(R1) ; carga A(i) MUL.D F4, F2, F0 ; cte * A(i) L.D F6, 0(R2) ; carga B(i) ADD.D F6, F4, F6 ; cte * A(i) + B(i) S.D F6, 0(R2) ; almacena B(i) DADDUI R1, R1, #-8 ; decrementa índice de A DADDUI R2, R2, #-8 ; decrementa índice de B SLTI R4, R1, fin ; comprobación de fin BEQZ R4, Bucle ; salta si R4 = 0
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]]
