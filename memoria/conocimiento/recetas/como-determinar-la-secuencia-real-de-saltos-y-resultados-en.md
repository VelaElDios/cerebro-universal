---
tipo: "receta"
titulo: "Cómo determinar la secuencia real de saltos y resultados en un bucle con registro alternante"
temas: ["ac", "bucles", "prediccion-saltos"]
claves: ["BEQZ", "XORI", "alternancia registro", "B1 B2", "T NT"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[prediccion-saltos]]

El bucle inicia con R1=0. XORI R1,R1,#1 invierte el bit menos significativo (0↔1). Cada iteración ejecuta B1 y B2 en orden. B1 (BEQZ R1,L2): si R1=0 salta a L2 (Taken), si R1=1 continúa (Not Taken). B2 (BEQZ R1,L3): mismo registro, misma condición. Como R1 alterna cada iteración, el patrón de 6 iteraciones es: Iter1: R1=0 → B1=T, B2=T; Iter2: R1=1 → B1=NT, B2=NT; Iter3: R1=0 → B1=T, B2=T; Iter4: R1=1 → B1=NT, B2=NT; Iter5: R1=0 → B1=T, B2=T; Iter6: R1=1 → B1=NT, B2=NT. Secuencia: B1,T; B2,T; B1,NT; B2,NT; B1,T; B2,T; B1,NT; B2,NT; B1,T; B2,T; B1,NT; B2,NT.

> DADD R1, R0, R0 ... L1: BEQZ R1, L2 ; (B1) ... L2: BEQZ R1, L3 ; (B2) ... L3: XORI R1, R1, #1 ; (<-> NOT R1) J L1
> — `repo:datos/temarios/AC/examenes/June2023.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[analisis-de-prediccion-de-saltos-en-bucle-con-dos-saltos-con]] · [[comportamiento-real-de-saltos-b1-beqz-y-b2-beq-en-bucle-mips]] · [[comportamiento-real-de-saltos-b1-y-b2-en-bucle-risc-v-que-re]]
