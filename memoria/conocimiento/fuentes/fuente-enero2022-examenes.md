---
tipo: "fuente"
titulo: "Enero2022 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Enero2022.pdf`.

## Resumen
Examen de Arquitectura de Computadores (curso 2021/22) con 30 preguntas tipo test sobre paralelismo, taxonomía de Flynn, cálculo de MIPS pico, ley de Amdahl, dependencias en bucles MIPS, adelantamiento en pipeline, riesgos WAW/WAR/RAW, marcador vs Tomasulo, segmentación software, desenrollamiento de bucles, predicción de saltos (2 bits, BTB, BHT), ejecución multicamino, especulación software, bits de veneno, etapa commit en Tomasulo, CPI ideal superescalar, etapa de predicción en superescalar, inconvenientes superescalar, características VLIW, modelos memoria multicore (UMA/NUMA), microarquite
Este trozo contiene los problemas 1 (continuación), 2 y 3 del examen ordinario de Arquitectura de Computadores (curso 2021/22). El problema 1 pide analizar detenciones en un bucle de media ponderada, desenrollarlo para eliminar stalls y recalcular CPI. El problema 2 es una simulación completa de Tomasulo con especulación en MIPS64 (latencias: LD/ST=1, MUL=6, ADD=4, ROB=4 entradas, 2 RS/unidad, 2 load buffers, restricciones de CDB y recursos). El problema 3 requiere diagramas de pipeline para un superscalar grado 4 con 5 unidades funcionales en tres modalidades: en orden, fuera de orden sin ren

## Lo que se sacó de él (16)
- [[analisis-de-detenciones-stalls-en-bucle-con-media-ponderada]]
- [[analisis-de-pipeline-fp-para-bucle-media-ponderada-problema]]
- [[calculo-de-mips-pico-a-partir-de-mezcla-de-instrucciones-y-f]]
- [[comportamiento-de-bits-de-veneno-poison-bits-ante-excepcion]]
- [[cpi-tras-desenrollado-y-planificacion-de-bucle]]
- [[dependencias-en-bucle-mips-de-carga-modificacion-almacenamie]]
- [[desenrollado-de-bucle-minimo-para-planificacion-sin-detencio]]
- [[diagrama-pipeline-superscalar-ejecucion-fuera-de-orden-con-r]]
- [[diagrama-pipeline-superscalar-ejecucion-fuera-de-orden-sin-r]]
- [[diagrama-pipeline-superscalar-grado-4-ejecucion-en-orden-y-e]]
- [[dimensionado-de-btb-implicita-ancho-y-bits-totales-para-1024]]
- [[ejecucion-multicamino-multi-path-execution-frente-a-predicci]]
- [[ley-de-amdahl-para-mejora-de-subsistema-disco-6x-mas-rapido]]
- [[secuencia-de-aciertos-fallos-en-predictor-2-bits-inicializad]]
- [[simulacion-tomasulo-con-especulacion-parametros-clave-y-rest]]
- [[volcado-de-rob-reorder-buffer-en-ciclo-de-finalizacion-de-pr]]
