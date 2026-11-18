---
tipo: "receta"
titulo: "Simulación de predictor de un nivel con contadores de saturación de 2 bits por instrucción de salto"
temas: ["ac", "prediccion-saltos", "predictor-un-nivel"]
claves: ["2-bit saturating counter", "00 01 10 11", "strongly not taken", "weakly not taken", "weakly taken", "strongly taken"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]] · [[predictor-un-nivel]]

Cada instrucción de salto (B1, B2) tiene su propio contador de 2 bits. Estados: 00=Strongly NT, 01=Weakly NT, 10=Weakly T, 11=Strongly T. Predicción: 00/01 → NT, 10/11 → T. Actualización: si resultado real=T, incrementar (saturando en 11); si NT, decrementar (saturando en 00). Estado inicial: ambos en 00. Para cada salto en orden de ejecución: 1) Leer predicción del contador correspondiente; 2) Comparar con resultado real (T/NT) → Hit/Y o Miss/N; 3) Actualizar contador según resultado real. Calcular hit rate = hits / total predicciones al final.

> Detail the behavior of a one-level branch predictor using 2 bits per branch instruction. Consider the initial state indicated in the table. ... Prediction bits for B1 and B2 00
> — `repo:datos/temarios/AC/examenes/June2023.pdf` (cita sin comprobar)

Relacionado: [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[simulacion-de-predictor-de-saltos-de-1-nivel-con-2-bits-cont]] · [[simulacion-de-predictor-one-level-de-2-bits-para-dos-saltos]] · [[simulacion-de-predictor-two-level-correlacionante-2-1-con-bh]]
