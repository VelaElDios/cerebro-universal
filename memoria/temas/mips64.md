---
tipo: "tema"
titulo: "mips64"
notas: 35
---
# mips64

Nodo del mapa del Cerebro con todo lo que se sabe de «mips64» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/analisis-de-dependencias-y-planificacion-de-bucle-mips64-con|Análisis de dependencias y planificación de bucle MIPS64 con unidades FP segmentadas (examen Junio 2013)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/analisis-de-pipeline-fp-para-bucle-media-ponderada-problema|Análisis de pipeline FP para bucle media ponderada (Problema 1) con latencias L.D=1, MUL.D=3, ADD.D=2, DIV.D=5, S.D=1]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/analisis-de-stalls-en-bucle-mips64-con-forwarding-y-ramas-re|Análisis de stalls en bucle MIPS64 con forwarding y ramas resueltas en ID (Ejercicio 1a)]]
- 🧪 [[memoria/conocimiento/recetas/bucle-mips64-para-contar-ocurrencias-de-un-caracter-en-caden|Bucle MIPS64 para contar ocurrencias de un carácter en cadena ASCIIZ]]
- 🧪 [[memoria/conocimiento/recetas/configuracion-de-pipeline-mips64-para-problema-de-examen-lat|Configuración de pipeline MIPS64 para problema de examen (latencias FP, salto retardado, forwarding)]]
- 🧪 [[memoria/conocimiento/recetas/conversion-de-codigo-vliw-compactado-a-bucle-mips64-segmenta|Conversión de código VLIW compactado a bucle MIPS64 segmentado con un resultado por iteración]]
- 🧪 [[memoria/conocimiento/recetas/como-calcular-cycles-per-result-cpr-en-bucles-pipelined-con|Cómo calcular Cycles Per Result (CPR) en bucles pipelined con stalls]]
- 🧪 [[memoria/conocimiento/recetas/como-calcular-stalls-en-pipeline-mips64-con-operand-forwardi|Cómo calcular stalls en pipeline MIPS64 con operand forwarding y latencias FP conocidas]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-desenrollar-8x-y-planificar-en-superescalar-4-issue-2-i|Cómo desenrollar 8x y planificar en superescalar 4-issue (2 int + 2 PF) con sumas PF 2 ciclos]]
- 🧪 [[memoria/conocimiento/recetas/como-resolver-segmentacion-software-software-pipelining-en-m|Cómo resolver segmentación software (software pipelining) en MIPS64 con salto retardado y adelantamiento]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-de-bucle-minimo-para-eliminar-todos-los-stalls|Desenrollado de bucle mínimo para eliminar todos los stalls en pipeline MIPS64 con FP]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-minimo-de-bucle-mips64-para-eliminar-stalls-con|Desenrollado mínimo de bucle MIPS64 para eliminar stalls con FP mul (3 ciclos) y div (4 ciclos)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/desenrollado-y-planificacion-sin-stalls-del-bucle-mips64-eje|Desenrollado y planificación sin stalls del bucle MIPS64 (Ejercicio 1b)]]
- 🧪 [[memoria/conocimiento/recetas/planificacion-de-bucle-jacobsthal-en-pipeline-mips64-con-uni|Planificación de bucle Jacobsthal en pipeline MIPS64 con unidades FP de 2 y 3 ciclos y salto retrasado]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/planificacion-superescalar-mips64-4-vias-con-latencias-pf-pr|Planificación superescalar MIPS64 4 vías con latencias PF (Problema 4 Enero 2015)]]
- 🧪 [[memoria/conocimiento/recetas/simulacion-de-predictor-de-saltos-de-1-nivel-con-2-bits-cont|Simulación de predictor de saltos de 1 nivel con 2 bits (contador saturación) para secuencia dada]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/simulacion-tomasulo-con-especulacion-parametros-clave-y-rest|Simulación Tomasulo con especulación: parámetros clave y restricciones de temporización]] · ⚠️ propuesto

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/desenrollado-6-y-renombrado-de-registros-pf-para-superescala|Desenrollado 6× y renombrado de registros PF para superescalar MIPS64 (examen 2015)]]

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/dependencias-en-codigo-mips64-fp-l-d-mul-s-add-s-s-d|Dependencias en código MIPS64 FP: L.D → MUL.S → ADD.S → S.D]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/ejercicio-2-analisis-de-prediccion-de-saltos-en-bucle-contad|Ejercicio 2 - Análisis de predicción de saltos en bucle contador de ceros y pares]]
- 💡 [[memoria/conocimiento/conceptos/especulacion-estatica-con-poison-bits-en-mips64-lw|Especulación estática con poison bits en MIPS64 (LW*)]]
- 💡 [[memoria/conocimiento/conceptos/etiquetado-de-saltos-b1-b2-b3-en-bucle-contador-ceros-pares|Etiquetado de saltos B1, B2, B3 en bucle contador ceros/pares]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/mips64-usa-caches-separadas-para-instrucciones-y-datos-harva|MIPS64 usa cachés separadas para instrucciones y datos (Harvard modificada)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/tabla-de-estado-de-instrucciones-en-algoritmo-scoreboard-iss|Tabla de estado de instrucciones en algoritmo Scoreboard (Issue, Read operands, Execution Start-End, Write result)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/tipos-de-dependencias-y-hazards-en-codigo-mips64-de-punto-fl|Tipos de dependencias y hazards en código MIPS64 de punto flotante (pregunta 6)]]

## Datos

- 📊 [[memoria/conocimiento/datos/configuracion-hardware-tomasulo-con-especulacion-para-examen|Configuración hardware Tomasulo con especulación para examen Enero 2016 Problema 3]]
- 📊 [[memoria/conocimiento/datos/codigo-mips64-de-conteo-elementos-no-nulos-en-vector-dispers|Código MIPS64 de conteo elementos no nulos en vector disperso (examen AC June 2020)]]
- 📊 [[memoria/conocimiento/datos/codigo-mips64-de-conversion-fahrenheitcelsius-usado-en-exame|Código MIPS64 de conversión Fahrenheit→Celsius usado en examen AC June 2020]]
- 📊 [[memoria/conocimiento/datos/codigo-mips64-y-secuencia-de-entrada-para-problema-2-conteo|Código MIPS64 y secuencia de entrada para Problema 2 (Conteo ceros y pares)]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/latencias-de-ejecucion-fp-en-superescalar-mips64-del-examen|Latencias de ejecución FP en superescalar MIPS64 del examen Enero 2015]]
- 📊 [[memoria/conocimiento/datos/latencias-de-unidades-funcionales-fp-en-examen-ac-june-2020|Latencias de unidades funcionales FP en examen AC June 2020 (Adder 2, Multiplier 4, Divider 8)]]
- 📊 [[memoria/conocimiento/datos/secuencia-de-10-instrucciones-mips64-fp-para-ejercicio-3-tom|Secuencia de 10 instrucciones MIPS64 FP para ejercicio 3 Tomasulo]]
- 📊 [[memoria/conocimiento/datos/secuencia-de-10-instrucciones-para-simulacion-tomasulo-probl|Secuencia de 10 instrucciones para simulación Tomasulo Problema 3]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/secuencia-de-datos-y-codigo-mips64-para-ejercicio-2-de-predi|Secuencia de datos y código MIPS64 para ejercicio 2 de predicción de saltos]]
- 📊 [[memoria/conocimiento/datos/secuencia-de-instrucciones-mips64-para-simulacion-tomasulo-p|Secuencia de instrucciones MIPS64 para simulación Tomasulo Problema 3a]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[pipeline]] · [[prediccion-saltos]] · [[tomasulo]] · [[floating-point]] · [[superescalar]] · [[loop-unrolling]] · [[dependencias]] · [[punto-flotante]] · [[branch-prediction]] · [[loop]] · [[especulacion]]
