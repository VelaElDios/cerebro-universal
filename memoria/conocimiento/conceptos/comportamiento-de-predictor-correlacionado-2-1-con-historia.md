---
tipo: "concepto"
titulo: "Comportamiento de predictor correlacionado (2,1) con historia inicial no tomada y BHT en no tomado fuerte"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor correlacionado (2", "1)", "historia global", "BHT", "no tomado fuerte"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Predictor correlacionado (2,1): historia global de 2 bits (GHR) indexa una BHT con 4 entradas (00,01,10,11). Cada entrada tiene un predictor de 1 bit (2 estados: tomado/no tomado). Inicial: GHR=00 (dos saltos previos no tomados). BHT[00..11] = 0 (no tomado fuerte, i.e., estado NT). Para cada salto (B1 y B2 en orden de ejecución): 1) Usar GHR actual para seleccionar entrada BHT[GHR]. 2) Predecir según esa entrada (NT). 3) Comparar con resultado real. 4) Actualizar entrada BHT[GHR] hacia resultado real (si era NT y real T -> cambiar a T; si era T y real NT -> cambiar a NT). 5) Desplazar GHR: insertar resultado real (1=tomado, 0=no tomado) en bit menos significativo. Repetir para toda la secuencia. Detallar tabla de evolución: ciclo, salto, GHR, índice, predicción, real, nueva BHT[idx], nuevo GHR.

> c) Detalla el comportamiento de un predictor correlacionado (2, 1), considerando que los últimos saltos ejecutados antes de llegar a la instrucción etiquetada como loop: han sido no tomados, y el estado inicial de los predictores en las BHTs es no tomado fuerte.
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[bits-de-prediccion-en-la-i-cache-funcionamiento-y-ventajas]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[predictor-correlacionado-1-2-con-bhr-y-dos-bhts]] · [[simulacion-de-predictor-correlacionante-de-2-niveles-2-1-con]] · [[simulacion-paso-a-paso-de-predictor-correlacionado-2-1-con-b]]
