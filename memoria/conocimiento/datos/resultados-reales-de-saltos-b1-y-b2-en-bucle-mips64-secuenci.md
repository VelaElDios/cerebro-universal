---
tipo: "dato"
titulo: "Resultados reales de saltos B1 y B2 en bucle MIPS64 secuencia 0,1,0,2,0,3,0,4,0,5"
temas: ["ac", "pipeline", "prediccion-saltos"]
claves: ["B1 BEQZ R2 next", "B2 BEQ R1 R3 end", "secuencia 0 1 0 2 0 3 0 4 0 5", "taken not taken"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]]

Para la secuencia 0,1,0,2,0,3,0,4,0,5 (10 elementos, 5 ceros y 5 no-ceros):
- B1 (BEQZ R2, next): salta cuando R2==0 → Taken en los 5 ceros (posiciones 1,3,5,7,9), Not Taken en los 5 no-ceros (posiciones 2,4,6,8,10). Patrón: T,N,T,N,T,N,T,N,T,N.
- B2 (BEQ R1, R3, end): compara puntero actual (R1) con dirección del último elemento (R3). R1 avanza de 4 en 4 (DADDUI R1,R1,#4). Solo en la última iteración (tras leer el 5) R1==R3 → Taken una sola vez al final; Not Taken en las 9 iteraciones previas. Patrón: N,N,N,N,N,N,N,N,N,T.

> The following MIPS64 code loop reads the sequence 0, 1, 0, 2, 0, 3, 0, 4, 0, 5. We assume that R1 and R3 contain the addresses of the first and last sequence elements, respectively. loop: LW R2, 0(R1) BEQZ R2, next #(B1) SW R0, 0(R1) next: BEQ R1, R3, end #(B2) DADDUI R1, R1, #4 J loop end: ...
> — `repo:datos/temarios/AC/examenes/June2017.pdf`

Relacionado: [[bucle-de-calculo-y-i-a-x-i-2-en-ensamblador-mips64]] · [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]]
