---
tipo: "dato"
titulo: "Secuencia de datos y código MIPS64 para ejercicio 2 de predicción de saltos"
temas: ["ac", "mips64", "prediccion-saltos"]
claves: ["secuencia 0", "1", "0", "2", "0", "3", "R1=6", "R2 dirección base", "B1 BNEZ R3 nozero", "B2 BNEZ R3 odd", "B3 BNEZ R1 loop"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips64]] · [[prediccion-saltos]]

Datos concretos del ejercicio: array en memoria desde R2: [0,1,0,2,0,3]. R1=6 (contador de elementos). Bucle: LW R3,0(R2); B1: BNEZ R3,nozero; DADDUI R4,R4,#1; nozero: ANDI R3,R3,#1; B2: BNEZ R3,odd; DADDUI R5,R5,#1; odd: DADDUI R2,R2,#4; DADDUI R1,R1,#-1; B3: BNEZ R1,loop. Se ejecutan 6 iteraciones (R1 de 6 a 1). En cada iteración se ejecutan B1, B2, B3 en ese orden.

> assuming that the sequence is 0, 1, 0, 2, 0, 3 and that R1 has been previously initialized with the value 6 (the length of the sequence).
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`

Relacionado: [[ejercicio-2-analisis-de-prediccion-de-saltos-en-bucle-contad]] · [[codigo-mips64-y-secuencia-de-entrada-para-problema-2-conteo]] · [[etiquetado-de-saltos-b1-b2-b3-en-bucle-contador-ceros-pares]]
