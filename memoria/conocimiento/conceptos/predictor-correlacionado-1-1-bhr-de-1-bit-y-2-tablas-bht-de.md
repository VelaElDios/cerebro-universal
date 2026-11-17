---
tipo: "concepto"
titulo: "Predictor correlacionado (1,1): BHR de 1 bit y 2 tablas BHT de 1 bit"
temas: ["1)", "ac", "arquitectura-computadores", "bhr 1 bit", "prediccion-saltos", "predictor (1"]
claves: ["predictor (1", "1)", "BHR 1 bit", "2 tablas BHT", "1 bit entrada", "correlación simple"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[1)]] · [[ac]] · [[arquitectura-computadores]] · [[bhr 1 bit]] · [[prediccion-saltos]] · [[predictor (1]]

El predictor (1,1) es el correlacionado más simple: BHR de 1 bit (resultado del último salto) selecciona entre 2 tablas BHT. Cada BHT tiene entradas de 1 bit (predictor 1-bit) indexadas por PC. Permite capturar correlación de orden 1: "si el salto anterior fue tomado, este salto se toma/no toma". En el ejemplo con d alternando 2 y 0, tras calentamiento logra predecir correctamente la correlación b1→b2.

> c) Predictor correlacionado (1,1) • Implementación más simple: predictor (1,1):  1 bit en la BHR, que selecciona la BHT  2 tablas BHT de 1 bit BHTs • n bits • PC • BHR
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[ejemplo-comparativo-predictores-1-bit-vs-2-bits-vs-correlaci]]
