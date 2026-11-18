---
tipo: "dato"
titulo: "Predictor de 1 bit en bucle de 3 iteraciones (T, T, NT) produce 2 fallos"
temas: ["ac", "prediccion-saltos", "predictor-1-bit"]
claves: ["predictor 1 bit", "BHT", "fallos predicción", "bucle", "tomado no tomado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[predictor-1-bit]]

Inicializado a NT (0). Iter1: predice NT, real T → fallo, actualiza a T. Iter2: predice T, real T → acierto. Iter3: predice T, real NT → fallo, actualiza a NT. Total: 2 fallos.

> Dado el siguiente fragmento de código de un bucle que se ejecuta 3 veces (las dos primeras el salto es TOMADO y la última NO TOMADO): ... Si se utiliza un predictor dinámico de 1 bit inicializado a 0 (No Tomado), ¿cuántos fallos de predicción se producirán en total tras finalizar las 3 iteraciones? c. 2 fallos.
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[comportamiento-de-la-btb-en-caso-de-acierto-test-ac-q14]] · [[predictor-dinamico-de-un-bit-funcionamiento-y-limitacion-en]] · [[como-analizar-predictores-de-salto-1-bit-4-bit-correlacionad]] · [[patron-de-prediccion-de-predictor-de-3-bits-ante-alternancia]]
