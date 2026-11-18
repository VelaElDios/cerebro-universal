---
tipo: "concepto"
titulo: "Predictor correlacionado (1,2) con BHR y dos BHTs"
temas: ["ac", "prediccion-saltos"]
claves: ["predictor correlacionado", "BHR", "BHT", "no tomado fuerte", "historia de saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Un predictor correlacionado (1,2) usa un registro de historial de saltos (BHR) de 1 bit y dos tablas de predicción (BHT 0 y BHT 1) de 2 entradas cada una (contadores de saturación de 2 bits). El BHR indica si el último salto fue tomado (1) o no tomado (0). Cada BHT se indexa con el BHR: BHT 0 se usa cuando BHR=0, BHT 1 cuando BHR=1. Estado inicial del ejercicio: BHR=1 (último salto tomado), ambas BHTs en estado 00 (no tomado fuerte). Para cada salto se predice usando la BHT seleccionada por el BHR actual, se compara con el resultado real, se actualiza el contador de esa entrada y se actualiza el BHR con el resultado real.

> Detalla el comportamiento de un predictor correlacionado (1, 2), considerando que el último salto ejecutado antes de llegar a la instrucción etiquetada como loop: ha sido tomado, y el estado inicial de los predictores en las BHTs es no tomado fuerte.
> — `repo:datos/temarios/AC/examenes/Junio2025.pdf`

Relacionado: [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]]
