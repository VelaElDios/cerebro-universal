---
tipo: "tema"
titulo: "bucles"
notas: 22
---
# bucles

Nodo del mapa del Cerebro con todo lo que se sabe de «bucles» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/analisis-de-dependencias-en-bucle-con-indices-de-array-pregu|Análisis de dependencias en bucle con índices de array (pregunta 11)]]
- 🧪 [[memoria/conocimiento/recetas/analisis-de-detenciones-stalls-en-bucle-con-media-ponderada|Análisis de detenciones (stalls) en bucle con media ponderada y cálculo de CPI]]
- 🧪 [[memoria/conocimiento/recetas/condicion-para-solapar-iteraciones-de-un-bucle-desenrollado|Condición para solapar iteraciones de un bucle (desenrollado / software pipelining)]]
- 🧪 [[memoria/conocimiento/recetas/cpi-tras-desenrollado-y-planificacion-de-bucle|CPI tras desenrollado y planificación de bucle]]
- 🧪 [[memoria/conocimiento/recetas/calculo-de-instrucciones-tras-desenrollar-bucle-3-veces-unro|Cálculo de instrucciones tras desenrollar bucle 3 veces (unroll factor 3)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-determinar-la-secuencia-real-de-saltos-y-resultados-en|Cómo determinar la secuencia real de saltos y resultados en un bucle con registro alternante]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-fusionar-dos-bucles-en-uno-solo-para-aprovechar-localid|Cómo fusionar dos bucles en uno solo para aprovechar localidad temporal en L1]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/desenrollado-de-bucle-minimo-para-planificacion-sin-detencio|Desenrollado de bucle mínimo para planificación sin detenciones con salto retardado]]
- 🧪 [[memoria/conocimiento/recetas/identificacion-de-dependencias-loop-carried-en-bucles-c-styl|Identificación de dependencias loop-carried en bucles (C-style y RISC-V)]]

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/por-que-fusionar-bucles-de-normalizacion-y-suma-de-cuadrados|Por qué fusionar bucles de normalización y suma de cuadrados en una sola pasada]] · ⚠️ propuesto

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/antidependencia-entre-iteraciones-en-bucle-con-store-y-actua|Antidependencia entre iteraciones en bucle con store y actualización de puntero]]
- 💡 [[memoria/conocimiento/conceptos/analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter|Análisis de dependencias en bucle con ADD.D y S.D (misma iteración vs entre iteraciones)]]
- 💡 [[memoria/conocimiento/conceptos/criterio-de-desenrollamiento-de-bucles-loop-unrolling|Criterio de desenrollamiento de bucles (loop unrolling)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/desenrollamiento-de-bucles-requiere-ausencia-de-dependencias|Desenrollamiento de bucles requiere ausencia de dependencias entre iteraciones]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/identificacion-de-antidependencia-entre-iteraciones-en-bucle|Identificación de antidependencia entre iteraciones en bucle con arrays (A[i+1]=A[i]+B[i]; B[i]=A[i]*2)]]
- 💡 [[memoria/conocimiento/conceptos/objetivo-del-desenrollamiento-de-bucles-loop-unrolling|Objetivo del desenrollamiento de bucles (loop unrolling)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/proposito-de-la-segmentacion-software-software-pipelining-te|Propósito de la segmentación software (software pipelining) (test AC Q8)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/segmentacion-software-software-pipelining-transforma-bucles|Segmentación software (software pipelining) transforma bucles con iteraciones dependientes en independientes]]
- 💡 [[memoria/conocimiento/conceptos/tipos-de-dependencias-en-bucles-loop-independent-vs-loop-car|Tipos de dependencias en bucles: loop-independent vs loop-carried]]
- 💡 [[memoria/conocimiento/conceptos/transformacion-por-software-pipelining-daddui-mantiene-signo|Transformación por software pipelining: DADDUI mantiene signo de incremento]]
- 💡 [[memoria/conocimiento/conceptos/tecnica-de-segmentacion-software-software-pipelining|Técnica de segmentación software (software pipelining)]]

## Datos

- 📊 [[memoria/conocimiento/datos/valor-inmediato-de-daddui-tras-desenrollar-3-un-bucle-con-da|Valor inmediato de DADDUI tras desenrollar 3× un bucle con DADDUI R1,R1,#-8]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[pipeline]] · [[dependencias]] · [[optimizacion]] · [[ilp]] · [[planificacion]] · [[paralelismo-instruccion]] · [[vectorizacion]] · [[loop-unrolling]] · [[cpi]] · [[optimización]] · [[desenrollamiento]]
