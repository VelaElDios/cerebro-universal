---
tipo: "receta"
titulo: "Simulación de predictor two-level correlacionante (2,1) con BHR de 2 bits y 4 entradas BHT"
temas: ["ac", "examen", "prediccion-saltos"]
claves: ["two-level predictor", "correlating", "(2", "1)", "BHR", "BHT", "Pattern History Table", "initial state 11"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[prediccion-saltos]]

Predictor two-level (2,1): Global Branch History Register (BHR) de 2 bits que registra los 2 últimos resultados reales (T/NT) de cualquier salto. BHT (Pattern History Table) con 4 entradas (2^2), cada una un contador de 2 bits (inicial 11). Para cada salto ejecutado (B1 o B2): el índice en la BHT = valor actual del BHR; se lee el contador de esa entrada; predicción = MSB del contador; se compara con resultado real; se actualiza ese contador (saturando); se actualiza el BHR desplazando e insertando el resultado real (T=1, NT=0). Columnas de la tabla: Prediction bits (BHR and BHTs) — muestra los 4 contadores de la BHT en orden 00,01,10,11; Predicted outcome (T/NT); Hit (Y/N).

> Detail the behavior of a two-level (2, 1) correlating branch predictor, assuming the same input vector, and considering the initial state indicated in the table.
> — `repo:datos/temarios/AC/examenes/June2022.pdf`
