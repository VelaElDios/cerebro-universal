---
tipo: "receta"
titulo: "Cálculo de bits totales en predictor (2,2) con 3 entradas por BHT"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor correlacionado", "dos niveles", "(m", "n)", "BHT", "bits predicción"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Predictor (m,n): m bits de historia global, n bits de historia local por entrada. Aquí (2,2): 2 bits historia global → 4 patrones globales. Cada BHT tiene 3 entradas (no potencia de 2, inusual). Cada entrada tiene contador de 2 bits. Total BHTs = 2^m = 4. Cada BHT tiene 3 entradas * 2 bits = 6 bits. Total bits = 4 * 6 = 24 bits. Respuesta: b) 24 bits.

> Un predictor (2,2) con 3 entradas en cada BHT a) Se implementa con un total de 16 bits b) Se implementa con un total de 24 bits c) Se implementa con un total de 26 bits d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2017.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[calculo-de-bits-totales-en-predictor-1-2-con-bht-de-4-entrad]] · [[calculo-de-bits-en-predictor-correlacionado-de-dos-niveles-p]] · [[predictor-correlacionante-m-n-tiene-2-n-bhts]]
