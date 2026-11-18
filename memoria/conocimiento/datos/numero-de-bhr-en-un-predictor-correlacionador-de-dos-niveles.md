---
tipo: "dato"
titulo: "Número de BHR en un predictor correlacionador de dos niveles (2, 1)"
temas: ["ac", "bhr", "correlating predictor", "prediccion-saltos"]
claves: ["(2", "1) predictor", "Branch History Register", "BHR", "two-level"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bhr]] · [[correlating predictor]] · [[prediccion-saltos]]

En un predictor correlacionador de dos niveles **(2, 1)**, el primer número (2) indica el **número de bits de historia global** (o por salto) y el segundo (1) el **número de bits del predictor local** (contador saturante). Por tanto, hay **2^2 = 4 entradas en la tabla de historia (BHT)**, cada una con su propio registro de historia de 1 bit (o contador de 1 bit). La pregunta pide "cuántos BHRs": la respuesta correcta es **4** (opción d), uno por cada entrada de la tabla de historia de 2 bits.

> How many BHRs are there in a correlating two-level (2, 1) predictor? a) 1 b) 2 c) 3 d) 4
> — `repo:datos/temarios/AC/examenes/January2018.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
