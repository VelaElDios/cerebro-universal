---
tipo: "tema"
titulo: "optimizacion"
notas: 26
---
# optimizacion

Nodo del mapa del Cerebro con todo lo que se sabe de «optimizacion» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/cpi-tras-desenrollado-y-planificacion-de-bucle|CPI tras desenrollado y planificación de bucle]]
- 🧪 [[memoria/conocimiento/recetas/como-forzar-un-salto-condicional-real-en-gcc-para-medir-pred|Cómo forzar un salto condicional real en GCC para medir predicción de ramas]]
- 🧪 [[memoria/conocimiento/recetas/como-fusionar-dos-bucles-en-uno-solo-para-aprovechar-localid|Cómo fusionar dos bucles en uno solo para aprovechar localidad temporal en L1]]
- 🧪 [[memoria/conocimiento/recetas/como-transformar-std-list-a-std-vector-con-reserva-previa-pa|Cómo transformar std::list a std::vector con reserva previa para mejorar localidad de caché]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-de-bucle-4x-con-salto-retardado-para-eliminar-s|Desenrollado de bucle 4x con salto retardado para eliminar stalls en pipeline in-order]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-de-bucle-minimo-para-planificacion-sin-detencio|Desenrollado de bucle mínimo para planificación sin detenciones con salto retardado]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-manual-manual-unrolling-con-4-acumuladores-para|Desenrollado manual (Manual Unrolling) con 4 acumuladores para romper cadena de dependencia y subir IPC]]
- 🧪 [[memoria/conocimiento/recetas/optimizacion-ilp-mediante-desenrollado-de-4-vias-con-acumula|Optimización ILP mediante desenrollado de 4 vías con acumuladores independientes]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/optimizacion-ilp-mediante-desenrollado-de-bucle-con-4-acumul|Optimización ILP mediante desenrollado de bucle con 4 acumuladores independientes]]
- 🧪 [[memoria/conocimiento/recetas/optimizar-std-list-a-std-vector-con-reserva-y-fusion-de-bucl|Optimizar std::list a std::vector con reserva y fusión de bucles (Tarea 3.1 AC)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/patron-branchless-suma-condicional-mediante-multiplicacion-p|Patrón branchless: suma condicional mediante multiplicación por booleano]]
- 🧪 [[memoria/conocimiento/recetas/programacion-branchless-reemplazar-if-condicional-por-aritme|Programación branchless: reemplazar if condicional por aritmética con máscara 0/1]]
- 🧪 [[memoria/conocimiento/recetas/tecnicas-estaticas-basicas-para-reducir-detenciones-en-pipel|Técnicas estáticas básicas para reducir detenciones en pipeline]]

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/cuando-no-usar-branchless-trade-off-latencia-vs-previsibilid|Cuándo NO usar branchless (trade-off: latencia vs. previsibilidad)]]
- ⚖️ [[memoria/conocimiento/decisiones/desenrollado-de-bucles-replicar-mientras-se-reduzcan-detenci|Desenrollado de bucles: replicar mientras se reduzcan detenciones (stalls)]] · ⚠️ propuesto
- ⚖️ [[memoria/conocimiento/decisiones/por-que-fusionar-bucles-de-normalizacion-y-suma-de-cuadrados|Por qué fusionar bucles de normalización y suma de cuadrados en una sola pasada]]
- ⚖️ [[memoria/conocimiento/decisiones/usar-indice-size-t-en-bucle-fusionado-en-lugar-de-iteradores|Usar índice size_t en bucle fusionado en lugar de iteradores]]
- ⚖️ [[memoria/conocimiento/decisiones/uso-de-flag-o1-para-evitar-auto-unrolling-del-compilador-en|Uso de flag -O1 para evitar auto-unrolling del compilador en prácticas ILP]] · ⚠️ propuesto
- ⚖️ [[memoria/conocimiento/decisiones/uso-de-int64-t-y-vector-inicializado-a-1-para-evitar-optimiz|Uso de int64_t y vector inicializado a 1 para evitar optimizaciones muertas]] · ⚠️ propuesto

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/definicion-de-bloque-basico-test-ac-q7|Definición de bloque básico (test AC Q7)]]
- 💡 [[memoria/conocimiento/conceptos/desenrollado-de-bucle-loop-unrolling-3-para-vliw-y-compactac|Desenrollado de bucle (loop unrolling) 3× para VLIW y compactación]]
- 💡 [[memoria/conocimiento/conceptos/desenrollamiento-de-bucles-reduce-dependencias-de-control-me|Desenrollamiento de bucles: reduce dependencias de control mediante planificación estática]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/fusion-de-bucles-loop-fusion-para-localidad-temporal|Fusión de bucles (loop fusion) para localidad temporal]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/objetivo-del-desenrollamiento-de-bucles-loop-unrolling|Objetivo del desenrollamiento de bucles (loop unrolling)]]
- 💡 [[memoria/conocimiento/conceptos/planificacion-de-trazas-trace-scheduling-elimina-saltos-inte|Planificación de trazas (trace scheduling): elimina saltos internos en bucles]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/prevencion-de-dead-code-elimination-dce-forzando-uso-del-res|Prevención de Dead Code Elimination (DCE) forzando uso del resultado]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[pipeline]] · [[ilp]] · [[bucles]] · [[loop-unrolling]] · [[cpp]] · [[branchless]] · [[compiladores]] · [[cache]] · [[compilador]] · [[compilacion]] · [[memoria]]
