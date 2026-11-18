---
tipo: "concepto"
titulo: "Ejercicio 2 - Análisis de predicción de saltos en bucle contador de ceros y pares"
temas: ["ac", "mips64", "prediccion-saltos"]
claves: ["BNEZ", "predictor un nivel", "predictor dos niveles correlacionante (1", "1)", "BHR", "BHT", "tasa acierto"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips64]] · [[prediccion-saltos]]

El ejercicio presenta un bucle con tres saltos condicionales (B1: BNEZ R3,nozero; B2: BNEZ R3,odd; B3: BNEZ R1,loop) que se ejecutan para la secuencia 0,1,0,2,0,3 con R1=6. Se pide: a) comportamiento real (T/NT) de cada salto; b) simular predictor de un nivel con 1 bit por salto (estado inicial 1/1/1) y calcular tasa de acierto; c) simular predictor correlacionante de dos niveles (1,1) (1 bit de historia global BHR y tablas BHT de 1 bit, estado inicial BHR=0, BHT=1/1/1) y calcular tasa de acierto.

> Exercise 2 (2 points). The following MIPS64 code counts (in R4 and R5) the number of zeros and even numbers (considering that 0 is even) in a sequence stored in memory from the address R2.
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`

Relacionado: [[etiquetado-de-saltos-b1-b2-b3-en-bucle-contador-ceros-pares]] · [[secuencia-de-datos-y-codigo-mips64-para-ejercicio-2-de-predi]] · [[analisis-de-prediccion-de-saltos-en-bucle-con-dos-saltos-con]]
