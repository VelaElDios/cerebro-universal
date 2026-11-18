---
tipo: "receta"
titulo: "Simulación de predictor correlacionante de 2 niveles (2,1) con BHR global y BHT por entrada"
temas: ["ac", "bhr", "bht", "branch-prediction", "correlating", "gshare", "two-level"]
claves: ["two-level predictor", "correlating", "BHR", "Branch History Register", "BHT", "Branch History Table", "(2", "1) predictor"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2020.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bhr]] · [[bht]] · [[branch-prediction]] · [[correlating]] · [[gshare]] · [[two-level]]

Predictor (2,1) correlacionante: 2 bits de historia global (BHR) + 1 bit para seleccionar entrada en BHT (o 2^1=2 entradas BHT). Enunciado muestra 4 contadores de 2 bits (columnas 6-9: 10, 01, 10, 11) → BHT tiene 4 entradas (2 bits índice). BHR de 2 bits guarda últimos 2 resultados globales (T/NT). Índice BHT = BHR (o BHR XOR PC bits). Flujo por salto: 1) Leer BHR actual. 2) Índice = f(BHR, PC) → selecciona contador 2 bits en BHT. 3) Predecir según MSB contador. 4) Tras resultado real: actualizar contador seleccionado (saturación) y shift BHR << 1 | outcome. Estado inicial: BHR=10 (bits 6-7?), BHT[0]=01, BHT[1]=10, BHT[2]=11, BHT[3]=00 (columna 8-9?). Simular 16 saltos (8 iteraciones × 2 saltos) igual que predictor 1-nivel pero con historia compartida.

> c) Detail the behavior of a two-level (2, 1) correlating branch predictor, assuming the same input vector, and considering the initial state indicated in the table. Use columns 6, 7, and 8. Prediction bits (BHR and BTHs) (Initial state) 10 01 10 11 00
> — `repo:datos/temarios/AC/examenes/June2020.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[bits-de-prediccion-en-la-i-cache-funcionamiento-y-ventajas]] · [[simulacion-de-predictor-two-level-correlacionante-2-1-con-bh]] · [[simulacion-de-predictor-correlacionado-de-dos-niveles-2-2-co]] · [[comportamiento-de-predictor-correlacionado-2-1-con-historia]]
