---
tipo: "dato"
titulo: "Comportamiento real de saltos B1 (BEQZ) y B2 (BEQ) en bucle MIPS64 que recorre secuencia 0,1,0,2,0,3,0,4,0,5"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["BEQZ", "BEQ", "secuencia 0 1 0 2 0 3 0 4 0 5", "salto tomado no tomado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Bucle: loop: LW R2,0(R1); BEQZ R2,next (B1); SW R0,0(R1); next: BEQ R1,R3,fin (B2); DADDUI R1,R1,#4; J loop; fin: ... La secuencia tiene 10 elementos: 0,1,0,2,0,3,0,4,0,5. R1 apunta al primero, R3 al último. B1 (BEQZ R2,next) se toma cuando R2==0 (elementos en posiciones pares: 0,0,0,0,0 → 5 veces tomado, 5 veces no tomado alternando). B2 (BEQ R1,R3,fin) se toma solo en la última iteración cuando R1==R3 (1 vez tomado, 9 veces no tomado). El salto incondicional J loop siempre tomado (9 veces).

> El siguiente bucle MIPS64 recorre la siguiente secuencia 0, 1, 0, 2, 0, 3, 0, 4, 0, 5. Suponemos que R1 y R3 han sido inicializados con las direcciones del primer y del último elemento de la secuencia, respectivamente.
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[resultados-reales-de-saltos-b1-y-b2-en-bucle-mips64-secuenci]] · [[patron-de-saltos-en-bucle-mips64-secuencia-0-1-0-2-examen-en]] · [[comportamiento-real-de-saltos-b1-y-b2-en-bucle-risc-v-que-re]]
