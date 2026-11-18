---
tipo: "receta"
titulo: "Cálculo de bits totales en predictor (1,2) con BHT de 4 entradas y BHR"
temas: ["ac", "bhr", "bht", "prediccion-saltos", "predictor-dos-niveles"]
claves: ["predictor (1", "2)", "BHT", "BHR", "bits", "entradas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bhr]] · [[bht]] · [[prediccion-saltos]] · [[predictor-dos-niveles]]

Predictores de dos niveles (m,n): m bits de historia global (BHR), n bits por contador en BHT. Aquí (1,2) → BHR de 1 bit, contadores de 2 bits. BHT con 4 entradas → 4 contadores × 2 bits = 8 bits. BHR = 1 bit. Total = 9 bits. Pero la pregunta dice «en cada BHT», lo que sugiere múltiples BHTs indexados por BHR. Si hay 2^1 = 2 BHTs (porque BHR=1 bit), cada una con 4 entradas de 2 bits: 2 × 4 × 2 = 16 bits para BHTs + 1 bit BHR = 17 bits. Opción a.

> Para implementar un predictor (1,2) con 4 entradas en cada BHT, ¿Cuántos bits se necesitan considerando BHT y BHR?: a) 17 bits b) 18 bits c) 24 bits d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[ancho-y-tamano-en-bits-de-un-btb-implicito-con-1024-entradas]] · [[calculo-de-bits-totales-en-predictor-2-2-con-3-entradas-por]] · [[calculo-de-bits-en-predictor-de-dos-niveles-n-m-con-k-entrad]] · [[calculo-de-bits-en-predictor-correlacionado-de-dos-niveles-p]]
