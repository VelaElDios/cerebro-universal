---
tipo: "receta"
titulo: "Secuencia H/M para predictor correlacionado (1,1) en bucle de 5 iteraciones (pregunta 12)"
temas: ["ac", "historia-global", "prediccion-saltos", "predictor-correlacionado"]
claves: ["(1", "1) correlating predictor", "global history", "BHR", "5 iteraciones", "HMMMM", "MHHHM", "MHHHH", "MMHHM"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[historia-global]] · [[prediccion-saltos]] · [[predictor-correlacionado]]

Predictor (1,1): 1 bit de historia global (GHR), 1 bit por entrada en tabla (contador 1-bit = predicción simple). Inicial GHR=0, tabla[0]=0 (NT). Iter1: índice GHR=0 → pred NT, real T → Miss, tabla[0]=1, GHR=1. Iter2: índice GHR=1 → pred NT (tabla[1]=0), real T → Miss, tabla[1]=1, GHR=1. Iter3: índice GHR=1 → pred T (tabla[1]=1), real T → Hit, GHR=1. Iter4: índice GHR=1 → pred T, real T → Hit, GHR=1. Iter5: índice GHR=1 → pred T, real NT → Miss, tabla[1]=0, GHR=0. Secuencia: MMHHM (opción d).

> Indicate the sequence of Hits (H) and Misses (M) for branch B1 using a (1, 1) correlating predictor whose values are initially all zeros.
> — `repo:datos/temarios/AC/examenes/June2022.pdf`

Relacionado: [[secuencia-h-m-para-predictor-2-bit-debilmente-no-tomado-en-b]] · [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]]
