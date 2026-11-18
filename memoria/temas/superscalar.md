---
tipo: "tema"
titulo: "superscalar"
notas: 29
---
# superscalar

Nodo del mapa del Cerebro con todo lo que se sabe de «superscalar» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/configuracion-superscalar-4-issue-para-diagramas-de-pipeline|Configuración superscalar 4-issue para diagramas de pipeline (examen AC enero 2022)]]
- 🧪 [[memoria/conocimiento/recetas/calculo-de-speedup-por-desenrollado-de-bucle-en-superscalar|Cálculo de speedup por desenrollado de bucle en superscalar]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-de-bucle-8-veces-para-superscalar-con-latencias|Desenrollado de bucle 8 veces para superscalar con latencias FP]]
- 🧪 [[memoria/conocimiento/recetas/diagrama-pipeline-superscalar-grado-4-ejecucion-en-orden-y-e|Diagrama pipeline superscalar grado 4: ejecución en orden y escritura en orden]]
- 🧪 [[memoria/conocimiento/recetas/diagrama-pipeline-superscalar-ejecucion-fuera-de-orden-con-r|Diagrama pipeline superscalar: ejecución fuera de orden con renombramiento y escritura fuera de orden]]
- 🧪 [[memoria/conocimiento/recetas/diagrama-pipeline-superscalar-ejecucion-fuera-de-orden-sin-r|Diagrama pipeline superscalar: ejecución fuera de orden sin renombramiento, escritura en orden]]
- 🧪 [[memoria/conocimiento/recetas/pasos-para-resolver-exercise-3-processor-a-superscalar-in-or|Pasos para resolver Exercise 3 Processor A (superscalar in-order sin renombrado)]]
- 🧪 [[memoria/conocimiento/recetas/planificacion-en-superescalar-3-vias-entero-salto-memoria-fp|Planificación en superescalar 3-vías (entero/salto, memoria, FP) con ranura de retardo]]
- 🧪 [[memoria/conocimiento/recetas/planificacion-en-superscalar-mips64-4-vias-2-enteros-2-fp-co|Planificación en superscalar MIPS64 4 vías (2 enteros + 2 FP) con branch delayed 2 slots]]

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/diferencias-clave-entre-los-tres-modelos-de-ejecucion-supers|Diferencias clave entre los tres modelos de ejecución superscalar (examen AC)]]
- ⚖️ [[memoria/conocimiento/decisiones/uso-de-ranura-de-retardo-de-1-ciclo-en-superescalar-para-ocu|Uso de ranura de retardo de 1 ciclo en superescalar para ocultar latencia de salto]]

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/comparativa-eficiencia-operations-per-cycle-opc-superscalar|Comparativa eficiencia operations per cycle (OPC) superscalar vs VLIW en bucle desenrollado]]
- 💡 [[memoria/conocimiento/conceptos/desenrollado-de-bucles-loop-unrolling-en-superescalar-con-re|Desenrollado de bucles (loop unrolling) en superescalar con renombrado de registros]]
- 💡 [[memoria/conocimiento/conceptos/diferencias-clave-processor-a-superscalar-in-order-vs-proces|Diferencias clave Processor A (superscalar in-order) vs Processor B (VLIW) en Exercise 3]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/ejercicio-3-ac-june-2019-comparacion-superscalar-in-order-vs|Ejercicio 3 AC June 2019: comparación superscalar in-order vs VLIW]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/forwarding-de-resultado-en-ciclo-siguiente-al-write-modelo-s|Forwarding de resultado en ciclo siguiente al Write (modelo superscalar examen)]]
- 💡 [[memoria/conocimiento/conceptos/metrica-de-comparacion-operaciones-por-ciclo-ipc-en-supersca|Métrica de comparación: operaciones por ciclo (IPC) en superscalar vs VLIW]]
- 💡 [[memoria/conocimiento/conceptos/paso-de-commit-en-superscalar-actualizacion-de-registros|Paso de commit en superscalar: actualización de registros]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/planificacion-dinamica-sin-especulacion-emision-en-orden-eje|Planificación dinámica sin especulación: emisión en orden, ejecución y finalización fuera de orden]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/procesador-a-superscalar-mips64-4-issue-2-enteros-2-fp|Procesador A: Superscalar MIPS64 4-issue (2 enteros + 2 FP)]]
- 💡 [[memoria/conocimiento/conceptos/procesadores-superscalar-son-maquinas-sisd|Procesadores superscalar son máquinas SISD]]
- 💡 [[memoria/conocimiento/conceptos/romper-cadena-de-dependencias-para-exponer-ilp-en-pipeline-s|Romper cadena de dependencias para exponer ILP en pipeline superscalar]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/superescalar-3-vias-con-tuberias-dedicadas-por-tipo-de-instr|Superescalar 3-vías con tuberías dedicadas por tipo de instrucción]]
- 💡 [[memoria/conocimiento/conceptos/ventana-de-instrucciones-almacena-instrucciones-activas-deco|Ventana de instrucciones almacena instrucciones activas, decodificadas pero no finalizadas]]
- 💡 [[memoria/conocimiento/conceptos/ventana-de-instrucciones-en-superscalar-instrucciones-decodi|Ventana de instrucciones en superscalar: instrucciones decodificadas y renombradas no emitidas aún]] · ⚠️ propuesto

## Datos

- 📊 [[memoria/conocimiento/datos/cpi-ideal-de-un-superescalar-de-grado-n-es-1-n|CPI ideal de un superescalar de grado N es 1/N]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/codigo-de-10-instrucciones-del-exercise-3-ac-june-2019|Código de 10 instrucciones del Exercise 3 AC June 2019]]
- 📊 [[memoria/conocimiento/datos/codigo-de-instrucciones-para-ejercicio-2-tomasulo-especulati|Código de instrucciones para Ejercicio 2 (Tomasulo especulativo) y Ejercicio 3 (Superscalar)]]
- 📊 [[memoria/conocimiento/datos/latencias-de-instrucciones-y-supuestos-de-pipeline-en-exerci|Latencias de instrucciones y supuestos de pipeline en Exercise 3 AC June 2019]]

## Temas relacionados

[[ac]] · [[pipeline]] · [[vliw]] · [[examen]] · [[loop unrolling]] · [[tomasulo]] · [[out-of-order]] · [[register renaming]] · [[forwarding]] · [[ipc]] · [[rendimiento]] · [[commit]]
