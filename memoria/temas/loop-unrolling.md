---
tipo: "tema"
titulo: "loop-unrolling"
notas: 26
---
# loop-unrolling

Nodo del mapa del Cerebro con todo lo que se sabe de «loop-unrolling» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/calculo-de-instrucciones-tras-desenrollar-bucle-3-veces-unro|Cálculo de instrucciones tras desenrollar bucle 3 veces (unroll factor 3)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/calculo-de-speedup-entre-bucle-original-y-desenrollado-en-vl|Cálculo de speedup entre bucle original y desenrollado en VLIW]]
- 🧪 [[memoria/conocimiento/recetas/calculo-de-speedup-para-bucle-desenrollado-en-pipeline-con-h|Cálculo de Speedup para bucle desenrollado en pipeline con hazards]]
- 🧪 [[memoria/conocimiento/recetas/como-desenrollar-8x-y-planificar-en-superescalar-4-issue-2-i|Cómo desenrollar 8x y planificar en superescalar 4-issue (2 int + 2 PF) con sumas PF 2 ciclos]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-4x-de-bucle-mips64-fp-con-renombrado-de-registr|Desenrollado 4x de bucle MIPS64 FP con renombrado de registros y latencias dadas]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-4x-y-planificacion-minima-para-bucle-fp-con-lat|Desenrollado 4x y planificación mínima para bucle FP con latencias dadas]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-de-bucle-3x-y-planificacion-vliw-compactada|Desenrollado de bucle 3x y planificación VLIW compactada]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-de-bucle-4x-con-salto-retardado-para-eliminar-s|Desenrollado de bucle 4x con salto retardado para eliminar stalls en pipeline in-order]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-de-bucle-8-veces-para-superscalar-con-latencias|Desenrollado de bucle 8 veces para superscalar con latencias FP]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-de-bucle-minimo-para-eliminar-todos-los-stalls|Desenrollado de bucle mínimo para eliminar todos los stalls en pipeline MIPS64 con FP]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-minimo-de-bucle-mips64-para-eliminar-stalls-con|Desenrollado mínimo de bucle MIPS64 para eliminar stalls con FP mul (3 ciclos) y div (4 ciclos)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/desenrollado-y-planificacion-sin-stalls-del-bucle-mips64-eje|Desenrollado y planificación sin stalls del bucle MIPS64 (Ejercicio 1b)]]
- 🧪 [[memoria/conocimiento/recetas/desenrollamiento-de-bucle-minimo-para-eliminar-detenciones-e|Desenrollamiento de bucle mínimo para eliminar detenciones en RISC-V]]
- 🧪 [[memoria/conocimiento/recetas/desenrollamiento-de-bucles-loop-unrolling-4x-con-renombrado|Desenrollamiento de bucles (loop unrolling) 4x con renombrado de registros en RISC-V]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/desenrollamiento-de-bucles-4x-con-planificacion-para-elimina|Desenrollamiento de bucles 4x con planificación para eliminar detenciones (RISC-V)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/eliminacion-de-dependencias-de-nombre-mediante-renombrado-de|Eliminación de dependencias de nombre mediante renombrado de registros en desenrollamiento]]
- 🧪 [[memoria/conocimiento/recetas/optimizacion-ilp-mediante-desenrollado-de-bucle-con-4-acumul|Optimización ILP mediante desenrollado de bucle con 4 acumuladores independientes]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/preguntas-del-problema-1-detenciones-cpi-y-desenrollamiento|Preguntas del Problema 1: Detenciones, CPI y Desenrollamiento con salto retardado]]

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/efecto-de-intervalo-de-iniciacion-2-en-multiplicador-fp-sobr|Efecto de intervalo de iniciación 2 en multiplicador FP sobre código desenrollado]] · ⚠️ propuesto

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/bucle-vectorial-de-referencia-para-desenrollado-y-planificac|Bucle vectorial de referencia para desenrollado y planificación (examen AC June 2018)]]
- 💡 [[memoria/conocimiento/conceptos/consideraciones-del-desenrollamiento-de-bucles-sobrecarga-ta|Consideraciones del desenrollamiento de bucles: sobrecarga, tamaño de código y presión de registros]]
- 💡 [[memoria/conocimiento/conceptos/desenrollado-de-bucle-loop-unrolling-3-para-vliw-y-compactac|Desenrollado de bucle (loop unrolling) 3× para VLIW y compactación]]
- 💡 [[memoria/conocimiento/conceptos/diferencia-fundamental-desenrollamiento-vs-segmentacion-soft|Diferencia fundamental: desenrollamiento vs segmentación software]]
- 💡 [[memoria/conocimiento/conceptos/objetivo-del-desenrollamiento-de-bucles-loop-unrolling|Objetivo del desenrollamiento de bucles (loop unrolling)]]

## Datos

- 📊 [[memoria/conocimiento/datos/bibliografia-canonica-para-planificacion-de-instrucciones-he|Bibliografía canónica para Planificación de instrucciones (Hennessy & Patterson, Ortega et al.)]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/valor-inmediato-de-daddui-tras-desenrollar-3-un-bucle-con-da|Valor inmediato de DADDUI tras desenrollar 3× un bucle con DADDUI R1,R1,#-8]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[pipeline]] · [[optimizacion]] · [[mips64]] · [[planificacion-estatica]] · [[vliw]] · [[software-pipelining]] · [[bucles]] · [[planificacion]] · [[ilp]] · [[tomasulo]] · [[rendimiento]]
