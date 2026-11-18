---
tipo: "dato"
titulo: "Vector de entrada y estado inicial para simulación de predictores (Exercise 3)"
temas: ["ac", "examen", "prediccion-saltos"]
claves: ["input vector 10 7 8 4 2 6 9 0", "initial state 11 11", "B1 B2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[prediccion-saltos]]

Vector de entrada de 8 elementos: 10, 7, 8, 4, 2, 6, 9, 0. Se asume que el código del ejercicio 3 (no mostrado en el trozo) contiene dos instrucciones de salto condicional B1 y B2 cuyo comportamiento (T/NT) depende de este vector. Estado inicial de contadores de 2 bits: tanto para B1 como para B2 en predictor one-level = 11 (Strongly Taken). Para predictor two-level (2,1): BHR inicial = 11 (dos T previos), y las 4 entradas de la BHT (índices 00,01,10,11) todas a 11.

> assuming that the input vector is: 10, 7, 8, 4, 2, 6, 9, 0. Use the first and second columns in the table below (and as many rows as you need). ... considering the initial state indicated in the table. ... (Initial state) - 11 11 - - 11 11 11 11 11 - -
> — `repo:datos/temarios/AC/examenes/June2022.pdf` (cita sin comprobar)

Relacionado: [[simulacion-de-predictor-one-level-de-2-bits-para-dos-saltos]] · [[simulacion-de-predictor-de-saltos-de-1-nivel-con-2-bits-cont]] · [[simulacion-de-predictor-two-level-correlacionante-2-1-con-bh]]
