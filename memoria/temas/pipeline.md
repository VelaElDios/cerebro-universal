---
tipo: "tema"
titulo: "pipeline"
notas: 38
---
# pipeline

Nodo del mapa del Cerebro con todo lo que se sabe de «pipeline» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/adelantamiento-forwarding-para-riesgos-raw|Adelantamiento (forwarding) para riesgos RAW]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/calculo-cpi-base-pipeline-5-etapas-con-saltos-sin-prediccion|Cálculo CPI base pipeline 5 etapas con saltos sin predicción]]
- 🧪 [[memoria/conocimiento/recetas/calculo-de-cpi-en-pipeline-con-stalls-y-tras-optimizacion|Cálculo de CPI en pipeline con stalls y tras optimización]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/calculo-de-detenciones-stalls-y-cpr-en-pipeline-risc-v-con-f|Cálculo de detenciones (stalls) y CPR en pipeline RISC-V con FP segmentado]]
- 🧪 [[memoria/conocimiento/recetas/calculo-de-penalizacion-de-salto-condicional-en-pipeline-de|Cálculo de penalización de salto condicional en pipeline de 5 etapas]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/como-leer-la-tabla-de-estado-de-instrucciones-en-el-marcador|Cómo leer la tabla de estado de instrucciones en el marcador de Tomasulo]]
- 🧪 [[memoria/conocimiento/recetas/como-se-traza-la-ejecucion-ciclo-a-ciclo-en-el-algoritmo-de|Cómo se traza la ejecución ciclo a ciclo en el algoritmo de Tomasulo]]
- 🧪 [[memoria/conocimiento/recetas/desenrollado-manual-manual-unrolling-con-4-acumuladores-para|Desenrollado manual (Manual Unrolling) con 4 acumuladores para romper cadena de dependencia y subir IPC]]
- 🧪 [[memoria/conocimiento/recetas/desenrollamiento-de-bucle-minimo-para-eliminar-detenciones-e|Desenrollamiento de bucle mínimo para eliminar detenciones en RISC-V]]
- 🧪 [[memoria/conocimiento/recetas/parametros-estandar-para-ejercicios-de-segmentacion-software|Parámetros estándar para ejercicios de segmentación software en RISC-V (Tema 3)]]
- 🧪 [[memoria/conocimiento/recetas/pipeline-risc-v-de-5-etapas-if-id-ex-mem-wb|Pipeline RISC-V de 5 etapas: IF, ID, EX, MEM, WB]] · ⚠️ propuesto

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/suposicion-de-cauce-detenido-durante-huecos-de-retardo-para|Suposición de cauce detenido durante huecos de retardo para cálculo de penalización]]

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin|Alternativas de detección de instrucción de salto en pipeline]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/definicion-de-latencia-de-salto-y-huecos-de-retardo|Definición de latencia de salto y huecos de retardo]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/definicion-y-proposito-de-la-segmentacion-pipeline|Definición y propósito de la segmentación (pipeline)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/dependencia-de-datos-en-pipeline-riesgo-solo-si-instruccione|Dependencia de datos en pipeline → riesgo solo si instrucciones están cerca]]
- 💡 [[memoria/conocimiento/conceptos/dependencias-en-bucles-risc-v-clasificacion-intra-iteracion|Dependencias en bucles RISC-V: clasificación intra-iteración vs loop-carried]]
- 💡 [[memoria/conocimiento/conceptos/esquemas-de-pipeline-con-1-2-y-3-huecos-de-retardo-para-beqz|Esquemas de pipeline con 1, 2 y 3 huecos de retardo para beqz]]
- 💡 [[memoria/conocimiento/conceptos/estructura-del-marcador-scoreboard-en-arquitectura-de-comput|Estructura del marcador (scoreboard) en arquitectura de computadores]]
- 💡 [[memoria/conocimiento/conceptos/limitacion-del-adelantamiento-hazard-load-use-load-use-penal|Limitación del adelantamiento: hazard load-use (load-use penalty)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/mecanismos-de-recuperacion-ante-fallos-de-prediccion-de-salt|Mecanismos de recuperación ante fallos de predicción de saltos]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/penalizacion-de-fallo-de-prediccion-de-salto-en-pipeline-sup|Penalización de fallo de predicción de salto en pipeline superscalar]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/penalizacion-de-salto-en-mips-resuelto-en-id-sin-prediccion|Penalización de salto en MIPS resuelto en ID sin predicción]]
- 💡 [[memoria/conocimiento/conceptos/por-que-el-orden-de-los-datos-afecta-al-codigo-con-salto-per|Por qué el orden de los datos afecta al código con salto pero no al branchless]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/predictor-de-saltos-por-que-datos-ordenados-vs-desordenados|Predictor de saltos: por qué datos ordenados vs desordenados cambian rendimiento drásticamente]]
- 💡 [[memoria/conocimiento/conceptos/problema-examen-ac-cpi-pipeline-con-btb-que-solo-almacena-sa|Problema examen AC: CPI pipeline con BTB que solo almacena saltos tomados]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/riesgo-raw-como-dependencia-de-datos-verdadera|Riesgo RAW como dependencia de datos verdadera]]
- 💡 [[memoria/conocimiento/conceptos/riesgos-de-datos-en-risc-v-raw-waw-war|Riesgos de datos en RISC-V: RAW, WAW, WAR]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/riesgos-estructurales-causas-y-ejemplo-banco-de-registros|Riesgos estructurales: causas y ejemplo banco de registros]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/romper-cadena-de-dependencias-para-exponer-ilp-en-pipeline-s|Romper cadena de dependencias para exponer ILP en pipeline superscalar]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/salto-retardado-delayed-branch-en-risc-v-implicaciones-en-pl|Salto retardado (delayed branch) en RISC-V: implicaciones en planificación]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/simulacion-paso-a-paso-de-tomasulo-con-bucle-fp-fld-fmul-d-f|Simulación paso a paso de Tomasulo con bucle FP (fld/fmul.d/fsd)]]
- 💡 [[memoria/conocimiento/conceptos/speedup-ideal-vs-real-en-pipeline-y-formula-con-detenciones|Speedup ideal vs real en pipeline y fórmula con detenciones]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/tipos-de-riesgos-en-pipeline-estructurales-datos-control|Tipos de riesgos en pipeline: estructurales, datos, control]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/ventaja-real-del-pipeline-mayor-throughput-instrucciones-uni|Ventaja real del pipeline: mayor throughput (instrucciones/unidad tiempo)]] · ⚠️ propuesto

## Datos

- 📊 [[memoria/conocimiento/datos/cronograma-de-emision-ejecucion-y-escritura-por-instruccion|Cronograma de emisión, ejecución y escritura por instrucción en ciclos 1-8]]
- 📊 [[memoria/conocimiento/datos/latencias-y-forwarding-en-procesador-de-referencia-para-plan|Latencias y forwarding en procesador de referencia para planificación estática]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/parametros-de-pipeline-risc-v-fp-para-ejercicios-tema-2-mult|Parámetros de pipeline RISC-V FP para ejercicios Tema 2 (multiplicador 3 ciclos, divisor 4/6 ciclos)]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[riscv]] · [[arquitectura]] · [[prediccion-saltos]] · [[tomasulo]] · [[riesgos]] · [[branch-prediction]] · [[cpi]] · [[scoreboard]] · [[microarquitectura]] · [[raw]] · [[ilp]]
