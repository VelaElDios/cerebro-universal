---
tipo: "tema"
titulo: "mips64"
notas: 19
---
# mips64

Nodo del mapa del Cerebro con todo lo que se sabe de «mips64» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/analisis-de-pipeline-fp-para-bucle-media-ponderada-problema|Análisis de pipeline FP para bucle media ponderada (Problema 1) con latencias L.D=1, MUL.D=3, ADD.D=2, DIV.D=5, S.D=1]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/bucle-mips64-para-contar-ocurrencias-de-un-caracter-en-caden|Bucle MIPS64 para contar ocurrencias de un carácter en cadena ASCIIZ]]
- 🧪 [[memoria/conocimiento/recetas/como-desenrollar-8x-y-planificar-en-superescalar-4-issue-2-i|Cómo desenrollar 8x y planificar en superescalar 4-issue (2 int + 2 PF) con sumas PF 2 ciclos]]
- 🧪 [[memoria/conocimiento/recetas/como-resolver-segmentacion-software-software-pipelining-en-m|Cómo resolver segmentación software (software pipelining) en MIPS64 con salto retardado y adelantamiento]]
- 🧪 [[memoria/conocimiento/recetas/planificacion-de-bucle-jacobsthal-en-pipeline-mips64-con-uni|Planificación de bucle Jacobsthal en pipeline MIPS64 con unidades FP de 2 y 3 ciclos y salto retrasado]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/planificacion-superescalar-mips64-4-vias-con-latencias-pf-pr|Planificación superescalar MIPS64 4 vías con latencias PF (Problema 4 Enero 2015)]]
- 🧪 [[memoria/conocimiento/recetas/simulacion-tomasulo-con-especulacion-parametros-clave-y-rest|Simulación Tomasulo con especulación: parámetros clave y restricciones de temporización]] · ⚠️ propuesto

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/desenrollado-6-y-renombrado-de-registros-pf-para-superescala|Desenrollado 6× y renombrado de registros PF para superescalar MIPS64 (examen 2015)]]

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/dependencias-en-codigo-mips64-fp-l-d-mul-s-add-s-s-d|Dependencias en código MIPS64 FP: L.D → MUL.S → ADD.S → S.D]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/ejercicio-2-analisis-de-prediccion-de-saltos-en-bucle-contad|Ejercicio 2 - Análisis de predicción de saltos en bucle contador de ceros y pares]]
- 💡 [[memoria/conocimiento/conceptos/especulacion-estatica-con-poison-bits-en-mips64-lw|Especulación estática con poison bits en MIPS64 (LW*)]]
- 💡 [[memoria/conocimiento/conceptos/etiquetado-de-saltos-b1-b2-b3-en-bucle-contador-ceros-pares|Etiquetado de saltos B1, B2, B3 en bucle contador ceros/pares]] · ⚠️ propuesto

## Datos

- 📊 [[memoria/conocimiento/datos/configuracion-hardware-tomasulo-con-especulacion-para-examen|Configuración hardware Tomasulo con especulación para examen Enero 2016 Problema 3]]
- 📊 [[memoria/conocimiento/datos/codigo-mips64-y-secuencia-de-entrada-para-problema-2-conteo|Código MIPS64 y secuencia de entrada para Problema 2 (Conteo ceros y pares)]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/latencias-de-ejecucion-fp-en-superescalar-mips64-del-examen|Latencias de ejecución FP en superescalar MIPS64 del examen Enero 2015]]
- 📊 [[memoria/conocimiento/datos/secuencia-de-10-instrucciones-mips64-fp-para-ejercicio-3-tom|Secuencia de 10 instrucciones MIPS64 FP para ejercicio 3 Tomasulo]]
- 📊 [[memoria/conocimiento/datos/secuencia-de-10-instrucciones-para-simulacion-tomasulo-probl|Secuencia de 10 instrucciones para simulación Tomasulo Problema 3]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/secuencia-de-datos-y-codigo-mips64-para-ejercicio-2-de-predi|Secuencia de datos y código MIPS64 para ejercicio 2 de predicción de saltos]]
- 📊 [[memoria/conocimiento/datos/secuencia-de-instrucciones-mips64-para-simulacion-tomasulo-p|Secuencia de instrucciones MIPS64 para simulación Tomasulo Problema 3a]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[prediccion-saltos]] · [[tomasulo]] · [[superescalar]] · [[especulacion]] · [[pipeline]] · [[simulacion]] · [[planificacion]] · [[dependencias]] · [[punto-flotante]] · [[raw]] · [[branch-prediction]]
