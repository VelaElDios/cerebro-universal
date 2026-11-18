---
tipo: "receta"
titulo: "Traza de predictor correlacionado (1,1) con historia global de 1 bit"
temas: ["ac", "bhr", "bht", "prediccion-saltos", "predictor-correlacionado"]
claves: ["predictor correlacionado", "(1", "1)", "BHR", "BHT", "historia global", "aciertos fallos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bhr]] · [[bht]] · [[prediccion-saltos]] · [[predictor-correlacionado]]

Predictor (1,1): 1 bit de historia global (BHR), BHT indexada por BHR con contadores de 1 bit. Inicio: BHR=0, BHT[0]=0(NT), BHT[1]=0(NT). 1) Salto T: índice BHR=0 → pred NT (fallo). Actualiza BHT[0]=1(T), BHR=1. 2) Salto NT: índice BHR=1 → pred NT (acierto). Actualiza BHT[1]=0(NT), BHR=0. 3) Salto T: índice BHR=0 → pred T (acierto). Resultado: 1 fallo, 2 aciertos.

> Analiza la evolución de un predictor correlacionado (1,1) ante la siguiente secuencia de saltos: Tomado, No Tomado, Tomado. Supón que el estado inicial es BHR=0 y todos los bits de la BHT=0. d. Se produce 1 fallo y 2 aciertos
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[bits-de-prediccion-en-la-i-cache-funcionamiento-y-ventajas]]
