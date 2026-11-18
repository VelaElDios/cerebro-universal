---
tipo: "dato"
titulo: "Estado inicial predictores para Problema 2 (1-bit y 2-niveles correlacionado (1,1))"
temas: ["ac", "branch-history-table", "correlacionado", "prediccion-saltos"]
claves: ["predictor 1 bit estado inicial 1/1/1", "predictor 2 niveles (1", "1) BHR=0 BTHs=1/1/1"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[branch-history-table]] · [[correlacionado]] · [[prediccion-saltos]]

Tabla de estado inicial para los 3 saltos (B1, B2, B3). Predictor 1 bit: bits de predicción iniciales = 1 (Taken) para los tres. Predictor 2 niveles (1,1): BHR (Branch History Register) inicial = 0. BTHs (Branch History Tables) iniciales = 1 (Taken) para las tres entradas (índice 0 y 1, pero con history 1 bit solo hay 2 entradas por salto? Normalmente (m,n) m=history bits, n=index bits. Aquí (1,1) implica 1 bit history, 1 bit index -> 2 entradas por salto. La tabla muestra "1/1/1" para BTHs, probablemente significando que las 2 entradas de cada salto valen 1, o que el estado mostrado es el relevante). La fila dice "0 1/1/1 1/1/1".

> Considera que el estado inicial del predictor es el mostrado en la primera fila de la tabla. (Estado inicial) - 1/1/1 - - 0 1/1/1 1/1/1 - -
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf` (cita sin comprobar)
