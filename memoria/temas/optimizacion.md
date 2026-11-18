---
tipo: "tema"
titulo: "optimizacion"
notas: 15
---
# optimizacion

Nodo del mapa del Cerebro con todo lo que se sabe de «optimizacion» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/cpi-tras-desenrollado-y-planificacion-de-bucle|CPI tras desenrollado y planificación de bucle]]
- 🧪 [[memoria/conocimiento/recetas/como-forzar-un-salto-condicional-real-en-gcc-para-medir-pred|Cómo forzar un salto condicional real en GCC para medir predicción de ramas]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-fusionar-dos-bucles-en-uno-solo-para-aprovechar-localid|Cómo fusionar dos bucles en uno solo para aprovechar localidad temporal en L1]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-transformar-std-list-a-std-vector-con-reserva-previa-pa|Cómo transformar std::list a std::vector con reserva previa para mejorar localidad de caché]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/desenrollado-de-bucle-minimo-para-planificacion-sin-detencio|Desenrollado de bucle mínimo para planificación sin detenciones con salto retardado]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-manual-manual-unrolling-con-4-acumuladores-para|Desenrollado manual (Manual Unrolling) con 4 acumuladores para romper cadena de dependencia y subir IPC]]
- 🧪 [[memoria/conocimiento/recetas/optimizacion-ilp-mediante-desenrollado-de-bucle-con-4-acumul|Optimización ILP mediante desenrollado de bucle con 4 acumuladores independientes]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/patron-branchless-suma-condicional-mediante-multiplicacion-p|Patrón branchless: suma condicional mediante multiplicación por booleano]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/programacion-branchless-reemplazar-if-condicional-por-aritme|Programación branchless: reemplazar if condicional por aritmética con máscara 0/1]]
- 🧪 [[memoria/conocimiento/recetas/tecnicas-estaticas-basicas-para-reducir-detenciones-en-pipel|Técnicas estáticas básicas para reducir detenciones en pipeline]]

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/cuando-no-usar-branchless-trade-off-latencia-vs-previsibilid|Cuándo NO usar branchless (trade-off: latencia vs. previsibilidad)]]
- ⚖️ [[memoria/conocimiento/decisiones/por-que-fusionar-bucles-de-normalizacion-y-suma-de-cuadrados|Por qué fusionar bucles de normalización y suma de cuadrados en una sola pasada]] · ⚠️ propuesto

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/definicion-de-bloque-basico-test-ac-q7|Definición de bloque básico (test AC Q7)]]
- 💡 [[memoria/conocimiento/conceptos/desenrollado-de-bucle-loop-unrolling-3-para-vliw-y-compactac|Desenrollado de bucle (loop unrolling) 3× para VLIW y compactación]]
- 💡 [[memoria/conocimiento/conceptos/objetivo-del-desenrollamiento-de-bucles-loop-unrolling|Objetivo del desenrollamiento de bucles (loop unrolling)]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[bucles]] · [[pipeline]] · [[ilp]] · [[branchless]] · [[compiladores]] · [[loop-unrolling]] · [[cpp]] · [[vliw]] · [[tradeoff]] · [[temporal-locality]] · [[memoria]]
