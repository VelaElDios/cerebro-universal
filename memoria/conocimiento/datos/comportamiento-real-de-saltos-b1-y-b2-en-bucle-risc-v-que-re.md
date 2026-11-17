---
tipo: "dato"
titulo: "Comportamiento real de saltos B1 y B2 en bucle RISC-V que recorre secuencia 0,1,0,2,0,3,0,4,0,5"
temas: ["ac", "patron-saltos", "prediccion-saltos", "risc-v", "secuencia-datos"]
claves: ["B1 beqz x2", "next", "B2 beq x1", "x3", "fin", "secuencia 0 1 0 2 0 3 0 4 0 5", "x1 puntero inicio", "x3 puntero fin"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[patron-saltos]] · [[prediccion-saltos]] · [[risc-v]] · [[secuencia-datos]]

Secuencia 10 elementos: 0,1,0,2,0,3,0,4,0,5. Bucle: lw x2,0(x1); beqz x2,next (B1); sw x0,0(x1); next: beq x1,x3,fin (B2); addi x1,x1,4; j loop. B1 (beqz x2): salta si x2==0. x2 toma valores de la secuencia. Para valores 0 (posiciones 1,3,5,7,9): B1 TOMADO (5 veces). Para valores no-cero (1,2,3,4,5): B1 NO TOMADO (5 veces). Patrón B1: T, NT, T, NT, T, NT, T, NT, T, NT. B2 (beq x1,x3): salta si x1==x3 (último elemento). Solo en la última iteración (elemento 5) x1 apunta al último. B2: NO TOMADO 9 veces, TOMADO 1 vez (al final). Patrón B2: NT, NT, NT, NT, NT, NT, NT, NT, NT, T.

> El siguiente bucle RISC-V recorre la siguiente secuencia 0, 1, 0, 2, 0, 3, 0, 4, 0, 5. Suponemos que x1 y x3 han sido inicializados con las direcciones del primer y del último elemento de la secuencia, respectivamente.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
