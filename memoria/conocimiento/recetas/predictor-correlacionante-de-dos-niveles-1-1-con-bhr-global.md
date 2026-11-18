---
tipo: "receta"
titulo: "Predictor correlacionante de dos niveles (1,1) con BHR global y BHT por salto"
temas: ["ac", "prediccion-saltos"]
claves: ["two-level correlating", "BHR 1 bit", "BHT 1 bit", "historia global", "índice combinado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Predictor (1,1): BHR (Branch History Register) de 1 bit que registra el resultado real del último salto ejecutado (global). Cada salto tiene su propia BHT (Branch History Table) de 1 bit (o una tabla compartida indexada por salto). La predicción se hace usando el bit de la BHT correspondiente al salto actual; tras ejecutar, se actualiza ese bit de la BHT con el resultado real y se actualiza el BHR con el resultado real. Estado inicial: BHR=0, entradas BHT (para B1,B2,B3) = 1/1/1. Se rellena tabla con columnas: BHR y BHTs antes de la predicción, predicción hecha, acierto, y nuevo BHR/BHTs.

> Detail the behavior of a two-level correlating branch predictor (1, 1). Consider that the initial state of the predictor is the one shown in the first row of the table.
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`

Relacionado: [[ejercicio-2-analisis-de-prediccion-de-saltos-en-bucle-contad]] · [[predictor-de-un-nivel-con-1-bit-por-instruccion-de-salto-est]] · [[simulacion-de-predictor-two-level-correlacionante-2-1-con-bh]] · [[predictor-correlacionado-1-2-con-bhr-y-dos-bhts]] · [[simulacion-de-predictor-correlacionado-de-dos-niveles-2-2-co]]
