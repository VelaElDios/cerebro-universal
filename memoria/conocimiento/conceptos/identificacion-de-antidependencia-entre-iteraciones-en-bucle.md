---
tipo: "concepto"
titulo: "Identificación de antidependencia entre iteraciones en bucle con arrays (A[i+1]=A[i]+B[i]; B[i]=A[i]*2)"
temas: ["ac", "bucles", "dependencias", "pipeline"]
claves: ["antidependencia", "entre iteraciones", "array A", "array B"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[dependencias]] · [[pipeline]]

En el bucle: S1 lee A[i] y escribe A[i+1]; S2 lee A[i] y escribe B[i]. Existe antidependencia (WAR) en A entre iteraciones: S1 escribe A[i+1] en iteración k y S1 lee A[i+1] en iteración k+1. No hay dependencia RAW entre S1 y S2 en la misma iteración porque S1 escribe A[i+1] y S2 lee A[i] (índices distintos).

> c) There is a antidependende, between S1 and S1, through A (between iterations)
> — `repo:datos/temarios/AC/examenes/January2021.pdf`

Relacionado: [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]] · [[definicion-de-dependencia-de-datos-raw-entre-instrucciones]]
