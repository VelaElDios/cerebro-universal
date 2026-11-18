---
tipo: "concepto"
titulo: "Estado inicial de predictores en Ejercicio 12: predictor 2-bits (B1=00, B2=11) y correlacionado (2,1) con BHR=10 y BHTs específicas"
temas: ["ac", "prediccion-saltos"]
claves: ["estado inicial", "predictor 2-bits", "predictor correlacionado (2", "1)", "BHR", "BHT", "00 01 10 11"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[prediccion-saltos]]

Valores iniciales explícitos para la simulación del Ejercicio 12. Predictor de 2-bits por instrucción: B1 empieza en estado 00 (fuertemente no tomado), B2 en 11 (fuertemente tomado). Predictor correlacionado (2,1): BHR inicial = 10. Cuatro entradas BHT indexadas por BHR: BHT[00]=01, BHT[01]=10, BHT[10]=11, BHT[11]=00. Cada entrada BHT es un predictor de 2-bits. Estos valores son la fila "(Estado inicial)" de las tablas del enunciado.

> (Estado inicial)          -       00       11           -           -      10    01    10     11     00          -             -
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`

Relacionado: [[estados-iniciales-de-predictores-en-ejercicio-2-un-nivel-y-d]] · [[estado-inicial-predictores-para-problema-2-1-bit-y-2-niveles]] · [[simulacion-paso-a-paso-de-predictor-correlacionado-2-1-con-b]]
