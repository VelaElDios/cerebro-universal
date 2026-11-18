---
tipo: "receta"
titulo: "Desenrollado 4x de bucle MIPS64 FP con renombrado de registros y latencias dadas"
temas: ["ac", "examen", "loop-unrolling", "pipeline", "tomasulo"]
claves: ["unroll 4 times", "register renaming", "L.D", "ADD.D", "MUL.D", "S.D", "DADDUI", "BNEZ", "delayed branch 2 slots"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[loop-unrolling]] · [[pipeline]] · [[tomasulo]]

Código original (9 instrucciones/iteración): L.D F2,0(R1); L.D F4,0(R2); ADD.D F6,F2,F2; MUL.D F10,F4,F6; S.D F10,0(R1); DADDUI R1,R1,#8; DADDUI R2,R2,#8; DADDUI R3,R3,#-1; BNEZ R3,Loop. Desenrollar 4 veces => 4 iteraciones. Renombrar registros FP (F2,F4,F6,F10) por iteración para evitar dependencias falsas (WAR/WAW): p.ej. iteración 1: F2_1,F4_1,F6_1,F10_1; iteración 2: F2_2,...; etc. Registros enteros R1,R2,R3 se actualizan secuencialmente; R1 y R2 son punteros base+offset, R3 contador. El BNEZ tiene 2 delay slots: las 2 instrucciones siguientes al salto se ejecutan siempre. Latencias: carga/almacena MEM 2 ciclos (resultado disponible tras 2 ciclos), ADD.D EX 1 ciclo, MUL.D EX 3 ciclos. Todas las unidades totalmente en tubería (pipelined). 32 registros FP de 64 bits disponibles.

> On a separate sheet of paper, unroll the code 4 times (you must deliver that sheet with the scheduling as well). Hint: it is required to rename the registers, since they are limited.
> — `repo:datos/temarios/AC/examenes/June2022.pdf`

Relacionado: [[desenrollado-minimo-de-bucle-mips64-para-eliminar-stalls-con]] · [[desenrollado-4x-y-planificacion-minima-para-bucle-fp-con-lat]] · [[desenrollado-de-bucle-4x-con-salto-retardado-para-eliminar-s]]
