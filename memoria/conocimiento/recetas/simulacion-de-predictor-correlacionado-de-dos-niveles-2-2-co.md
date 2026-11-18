---
tipo: "receta"
titulo: "Simulación de predictor correlacionado de dos niveles (2,2) con BHR de 2 bits y 4 BHTs de 2 bits"
temas: ["ac", "correlacionado", "prediccion-saltos", "predictor-dos-niveles"]
claves: ["BHR", "Branch History Register", "Pattern History Table", "PHT", "(2", "2) correlating", "historia global"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[correlacionado]] · [[prediccion-saltos]] · [[predictor-dos-niveles]]

Predictor (m,n) = m bits de historia global (BHR), n bits por contador en cada PHT. Aquí (2,2): BHR de 2 bits (historia de los 2 últimos saltos globales, T=1, NT=0), 4 entradas en la tabla de patrones (PHTs) indexadas por BHR (00,01,10,11), cada entrada es un contador de 2 bits. Estado inicial: BHR=00, las 4 PHTs en 00. Para cada salto en orden: 1) Índice = BHR actual; 2) Leer contador de esa PHT → predicción (00/01=NT, 10/11=T); 3) Comparar con real → Hit/Miss; 4) Actualizar ese contador según real; 5) Desplazar BHR a la izquierda e insertar resultado real (T=1, NT=0) en LSB. Hit rate final = hits / total.

> Detail the behavior of a two-level (2, 2) correlating branch predictor, assuming the same input vector, and considering the initial state indicated in the table. ... Prediction bits (BHR and BTHs) 00 00 00 00
> — `repo:datos/temarios/AC/examenes/June2023.pdf` (cita sin comprobar)

Relacionado: [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]] · [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[simulacion-de-predictor-two-level-correlacionante-2-1-con-bh]] · [[simulacion-de-predictor-correlacionante-de-2-niveles-2-1-con]] · [[simulacion-paso-a-paso-de-predictor-correlacionado-2-1-con-b]]
