---
tipo: "dato"
titulo: "Código MIPS64 de conteo elementos no nulos en vector disperso (examen AC June 2020)"
temas: ["ac", "branch-prediction", "exam-code", "loop", "mips64", "sparse-vector"]
claves: ["count", "isnull", "end", "DADD", "LW", "BEQZ", "DADDUI", "BEQ", "J", "SW", "R1", "R2", "R3", "R4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[branch-prediction]] · [[exam-code]] · [[loop]] · [[mips64]] · [[sparse-vector]]

Bucle de 6 instrucciones que recorre vector [R1..R2] paso 4 bytes. R4=contador no nulos. B1=BEZ R3, isnull (salta si elemento==0). B2=BEQ R1, R2, end (salta si fin vector). Vector prueba: 0,7,0,0,0,0,2,0 (8 elementos). Comportamiento real: B1: NT,T,NT,NT,NT,NT,T,NT (T cuando valor≠0: posiciones 2 y 7). B2: NT,NT,NT,NT,NT,NT,NT,T (T solo en última iteración). Usado para evaluar predictores 1-nivel (2 bits por salto) y 2-niveles (2,1) correlacionante.

> Exercise 3. The next MIPS64 code counts (in R4) the number of not null elements in a disperse vector (a vector in which most of the elements are zero) stored in memory. Assume that R1 and R2 have been initialized with the address of the first and last vector element, respectively: DADD R4, R0, R0 count: LW R3, 0(R1) BEQZ R3, isnull #(B1) DADDUI R4, R4, #1 isnull: BEQ R1, R2, end #(B2) DADDUI R1, R1, #4 J count end: SW R4...
> — `repo:datos/temarios/AC/examenes/June2020.pdf`

Relacionado: [[simulacion-de-predictor-de-saltos-de-1-nivel-con-2-bits-cont]] · [[secuencia-de-datos-y-codigo-mips64-para-ejercicio-2-de-predi]] · [[ejercicio-2-analisis-de-prediccion-de-saltos-en-bucle-contad]] · [[codigo-mips64-y-secuencia-de-entrada-para-problema-2-conteo]]
