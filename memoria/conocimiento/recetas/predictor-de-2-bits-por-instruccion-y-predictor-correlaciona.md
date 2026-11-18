---
tipo: "receta"
titulo: "Predictor de 2-bits por instrucción y predictor correlacionado (2,1) para bucle de vector disperso (0,7,0,0,0,0,2,0)"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor 2-bits", "predictor correlacionado (2", "1)", "vector disperso", "beqz", "beq", "j", "estado inicial BHR BHT"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

Ejercicio 12: vector disperso de 8 elementos (0,7,0,0,0,0,2,0). Código: count: lw x3,0(x1); B1=beqz x3,isnull (salta si x3==0); addi x4,x4,1; isnull: B2=beq x1,x2,end (salta si x1==x2); addi x1,x1,4; j count; end: sw x4... Parte a) comportamiento real T/NT para B1 y B2 en cada iteración (8 iteraciones). Parte b) predictor de 2-bits por instrucción (B1 y B2 independientes), estado inicial: B1=00, B2=11. Parte c) predictor correlacionado (2,1): BHR de 2 bits, 4 BHTs (índice BHR), estado inicial BHR=10, BHTs: 00=01, 01=10, 10=11, 11=00. Hay que simular paso a paso actualizando BHR y BHTs.

> El siguiente código RISC-V cuenta (en x4) el número de elementos no nulos que hay en un vector disperso almacenado en memoria.
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[analisis-en-estado-estable-de-predictor-2-bits-vs-correlacio]] · [[predictor-correlacionado-2-1-para-bucle-de-conteo-de-caracte]] · [[como-analizar-predictores-de-salto-1-bit-4-bit-correlacionad]]
