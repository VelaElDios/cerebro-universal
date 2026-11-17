---
tipo: "tema"
titulo: "prediccion-saltos"
notas: 71
---
# prediccion-saltos

Nodo del mapa del Cerebro con todo lo que se sabe de «prediccion-saltos» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/analisis-en-estado-estable-de-predictor-2-bits-vs-correlacio|Análisis en estado estable de predictor 2 bits vs correlacionado (1,1) para bucle RISC-V con patrón complejo]]
- 🧪 [[memoria/conocimiento/recetas/calculo-cpi-base-pipeline-5-etapas-con-saltos-sin-prediccion|Cálculo CPI base pipeline 5 etapas con saltos sin predicción]]
- 🧪 [[memoria/conocimiento/recetas/calculo-de-cpi-sin-btb-y-speedup-con-btb-miss-rate-10-solo-s|Cálculo de CPI sin BTB y speedup con BTB (miss rate 10%, solo saltos tomados, actualización con penalidad)]]
- 🧪 [[memoria/conocimiento/recetas/calculo-de-predicciones-correctas-en-bucles-anidados-con-pre|Cálculo de predicciones correctas en bucles anidados con predictores de 1, 2 y 3 bits]]
- 🧪 [[memoria/conocimiento/recetas/calculo-de-speedup-comparando-predictor-con-penalidad-variab|Cálculo de speedup comparando predictor con penalidad variable vs penalidad fija]]
- 🧪 [[memoria/conocimiento/recetas/como-disenar-un-bucle-que-haga-fallar-siempre-un-predictor-d|Cómo diseñar un bucle que haga fallar siempre un predictor de 1 bit]]
- 🧪 [[memoria/conocimiento/recetas/como-el-predictor-de-2-bits-resuelve-el-problema-de-bucles-a|Cómo el predictor de 2 bits resuelve el problema de bucles anidados]]
- 🧪 [[memoria/conocimiento/recetas/ejemplo-comparativo-predictores-1-bit-vs-2-bits-vs-correlaci|Ejemplo comparativo predictores 1 bit vs 2 bits vs correlacionado (1,1) con código if(d==0)/if(d==1)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/ejemplo-de-transformacion-de-salto-a-instrucciones-predicada|Ejemplo de transformación de salto a instrucciones predicadas (código ensamblador)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/ejemplo-gas-4-22-predictor-dos-niveles|Ejemplo Gas(4,22) predictor dos niveles]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/evaluacion-de-rendimiento-de-btb-con-politica-de-solo-saltos|Evaluación de rendimiento de BTB con política de solo saltos tomados, hit rate 90%, actualización en fallo con penalidad]]
- 🧪 [[memoria/conocimiento/recetas/funcionamiento-y-actualizacion-de-la-btac-branch-target-addr|Funcionamiento y actualización de la BTAC (Branch Target Address Cache)]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/implementacion-predictor-correlacionado-m-n-con-bhr-y-bht|Implementación predictor correlacionado (m,n) con BHR y BHT]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/mejora-prestaciones-btb-con-politica-solo-saltos-tomados-y-a|Mejora prestaciones BTB con política solo-saltos-tomados y actualización perezosa]]
- 🧪 [[memoria/conocimiento/recetas/predictor-correlacionado-2-1-para-bucle-de-conteo-de-caracte|Predictor correlacionado (2,1) para bucle de conteo de caracteres en cadena "exam18]]
- 🧪 [[memoria/conocimiento/recetas/predictor-de-2-bits-por-instruccion-y-predictor-correlaciona|Predictor de 2-bits por instrucción y predictor correlacionado (2,1) para bucle de vector disperso (0,7,0,0,0,0,2,0)]]
- 🧪 [[memoria/conocimiento/recetas/predictor-dinamico-de-un-bit-funcionamiento-y-limitacion-en|Predictor dinámico de un bit: funcionamiento y limitación en bucles anidados]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/predictor-hibrido-con-predictores-locales-de-1-bit-y-3-bits|Predictor híbrido con predictores locales de 1-bit y 3-bits más selector de 2-bits saturado]]
- 🧪 [[memoria/conocimiento/recetas/predictor-hibrido-mcfarling-con-contador-saturado-de-2-bits|Predictor híbrido McFarling con contador saturado de 2 bits]]
- 🧪 [[memoria/conocimiento/recetas/simulacion-de-predictores-1-bit-4-bits-saturado-y-correlacio|Simulación de predictores 1 bit, 4 bits saturado y correlacionado (2,1) para dos bucles anidados con conteos fijos]] · ⚠️ propuesto
- 🧪 [[memoria/conocimiento/recetas/simulacion-paso-a-paso-de-predictor-correlacionado-2-1-con-b|Simulación paso a paso de predictor correlacionado (2,1) con BHR y 4 BHTs de 2-bits]] · ⚠️ propuesto

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/diseno-de-btac-cache-asociativa-por-conjuntos-como-opcion-ma|Diseño de BTAC: caché asociativa por conjuntos como opción más usada]] · ⚠️ propuesto
- ⚖️ [[memoria/conocimiento/decisiones/predictor-correlacionado-1-1-en-bucle-secuencia-0-1-0-2|Predictor correlacionado (1,1) en bucle secuencia 0,1,0,2]]
- ⚖️ [[memoria/conocimiento/decisiones/predictor-de-1-bit-inicializado-a-no-tomado-en-bucle-secuenc|Predictor de 1 bit inicializado a no tomado en bucle secuencia 0,1,0,2]]
- ⚖️ [[memoria/conocimiento/decisiones/yeh-y-patt-recomiendan-g-g-para-enteros-y-s-s-para-coma-flot|Yeh y Patt recomiendan G/g para enteros y S/s para coma flotante]] · ⚠️ propuesto

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/actualizacion-de-la-btb-tras-ejecutar-el-salto|Actualización de la BTB tras ejecutar el salto]]
- 💡 [[memoria/conocimiento/conceptos/bht-branch-history-table-tabla-separada-para-bits-de-predicc|BHT (Branch History Table): tabla separada para bits de predicción]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/bits-de-prediccion-en-la-i-cache-funcionamiento-y-ventajas|Bits de predicción en la I-caché: funcionamiento y ventajas]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion|BTB (Branch Target Buffer): fusión de BTAC y bits de predicción en una sola estructura]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/btb-con-predictores-de-4-bits-campos-de-cada-entrada|BTB con predictores de 4 bits: campos de cada entrada]]
- 💡 [[memoria/conocimiento/conceptos/ejecucion-multicamino-multi-path-execution-como-alternativa|Ejecución multicamino (multi-path execution) como alternativa a la predicción]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/estado-inicial-de-predictores-en-ejercicio-12-predictor-2-bi|Estado inicial de predictores en Ejercicio 12: predictor 2-bits (B1=00, B2=11) y correlacionado (2,1) con BHR=10 y BHTs específicas]]
- 💡 [[memoria/conocimiento/conceptos/estructura-y-funcionamiento-de-predictor-hibrido-de-torneo-c|Estructura y funcionamiento de predictor híbrido de torneo con predictor local 2-bit y global (1,2)]]
- 💡 [[memoria/conocimiento/conceptos/estructuras-hardware-para-prediccion-de-saltos-btac-bht-btb|Estructuras hardware para predicción de saltos (BTAC, BHT, BTB, I-caché con índice sucesor)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/implementacion-bht-para-predictor-de-2-bits-4k-entradas-80-9|Implementación BHT para predictor de 2 bits: 4K entradas, ~80-90% acierto]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/instrucciones-predicadas-convertir-dependencias-de-control-e|Instrucciones predicadas: convertir dependencias de control en dependencias de datos]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/mecanismos-de-recuperacion-ante-fallos-de-prediccion-de-salt|Mecanismos de recuperación ante fallos de predicción de saltos]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/multiples-caminos-como-tecnica-de-prediccion-de-saltos|Múltiples caminos como técnica de predicción de saltos]]
- 💡 [[memoria/conocimiento/conceptos/notacion-xax-m-2n-para-predictores-adaptativos-de-dos-nivele|Notación XAx(m,2n) para predictores adaptativos de dos niveles (Yeh y Patt 1992)]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/patron-de-saltos-en-bucle-mips64-secuencia-0-1-0-2-examen-en|Patrón de saltos en bucle MIPS64 secuencia 0,1,0,2 (examen Enero 2012)]]
- 💡 [[memoria/conocimiento/conceptos/penalizacion-de-salto-en-mips-resuelto-en-id-sin-prediccion|Penalización de salto en MIPS resuelto en ID sin predicción]]
- 💡 [[memoria/conocimiento/conceptos/planteamiento-general-de-prediccion-de-saltos-con-ejecucion|Planteamiento general de predicción de saltos con ejecución especulativa]]
- 💡 [[memoria/conocimiento/conceptos/prediccion-dinamica-basada-en-correlacion-temporal-y-espacia|Predicción dinámica basada en correlación temporal y espacial]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/prediccion-implicita-sin-bits-de-prediccion-en-btb|Predicción implícita sin bits de predicción en BTB]]
- 💡 [[memoria/conocimiento/conceptos/predictor-alpha-21264-tournament-branch-prediction-combina-l|Predictor Alpha 21264 (Tournament Branch Prediction) combina local y global]]
- 💡 [[memoria/conocimiento/conceptos/predictor-correlacionado-1-1-bhr-de-1-bit-y-2-tablas-bht-de|Predictor correlacionado (1,1): BHR de 1 bit y 2 tablas BHT de 1 bit]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/predictor-correlacionado-general-mejora-a-predictores-no-cor|Predictor correlacionado general mejora a predictores no correlacionados]]
- 💡 [[memoria/conocimiento/conceptos/predictor-correlacionado-o-de-dos-niveles-m-n-correlacion-es|Predictor correlacionado o de dos niveles (m,n): correlación espacial e historia global]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/predictor-dinamico-de-2-bits-jim-smith-1981-maquina-de-4-est|Predictor dinámico de 2 bits (Jim Smith, 1981): máquina de 4 estados y inercia]]
- 💡 [[memoria/conocimiento/conceptos/predictor-gselect-concatenacion-vs-gshare-xor-para-indexar-b|Predictor gselect (concatenación) vs gshare (XOR) para indexar BHT]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/predictor-hibrido-que-combina-dos-predictores-locales-1-bit|Predictor híbrido que combina dos predictores locales (1 bit y 3 bits) con selector de 2 bits y reglas de actualización específicas]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/predictores-n-bits-y-optimalidad-de-n-2-en-la-practica|Predictores n bits y optimalidad de n=2 en la práctica]]
- 💡 [[memoria/conocimiento/conceptos/problema-examen-ac-cpi-pipeline-con-btb-que-solo-almacena-sa|Problema examen AC: CPI pipeline con BTB que solo almacena saltos tomados]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/recuperacion-de-fallos-de-prediccion-con-registros-temporale|Recuperación de fallos de predicción con registros temporales]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/salto-retardado-con-instruccion-de-bloque-destino-riesgo-si|Salto retardado con instrucción de bloque destino: riesgo si salto no tomado]]
- 💡 [[memoria/conocimiento/conceptos/salto-retardado-y-instrucciones-predicadas-como-alternativas|Salto retardado y instrucciones predicadas como alternativas a predicción]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/tabla-de-actualizacion-de-contadores-de-2-bits-saturados-par|Tabla de actualización de contadores de 2-bits saturados para selector de predictor híbrido]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/taxonomia-de-tecnicas-de-prediccion-de-saltos|Taxonomía de técnicas de predicción de saltos]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/ventajas-e-inconvenientes-de-las-instrucciones-predicadas|Ventajas e inconvenientes de las instrucciones predicadas]] · ⚠️ propuesto
- 💡 [[memoria/conocimiento/conceptos/indice-sucesor-en-la-i-cache-para-prediccion-de-saltos-alter|Índice sucesor en la I-caché para predicción de saltos (alternativa a BTAC)]] · ⚠️ propuesto

## Datos

- 📊 [[memoria/conocimiento/datos/comportamiento-real-de-saltos-b1-y-b2-en-bucle-risc-v-que-re|Comportamiento real de saltos B1 y B2 en bucle RISC-V que recorre secuencia 0,1,0,2,0,3,0,4,0,5]]
- 📊 [[memoria/conocimiento/datos/costes-de-recuperacion-de-fallos-de-prediccion-por-procesado|Costes de recuperación de fallos de predicción por procesador]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/codigo-risc-v-ejercicio-10-bucle-conteo-a-en-exam18-con-salt|Código RISC-V Ejercicio 10: bucle conteo 'a' en "exam18" con saltos B1 (bne) y B2 (bnez)]]
- 📊 [[memoria/conocimiento/datos/codigo-risc-v-ejercicio-11-bucle-fibonacci-6-elementos-con-s|Código RISC-V Ejercicio 11: bucle Fibonacci 6 elementos con saltos B1 (beqz) y B2 (bnez)]]
- 📊 [[memoria/conocimiento/datos/codigo-risc-v-ejercicio-12-bucle-vector-disperso-0-7-0-0-0-0|Código RISC-V Ejercicio 12: bucle vector disperso (0,7,0,0,0,0,2,0) con saltos B1 (beqz), B2 (beq), j incondicional]]
- 📊 [[memoria/conocimiento/datos/ejemplo-pentium-pro-predictor-2-2-con-historia-global-de-2-b|Ejemplo Pentium Pro: predictor (2,2) con historia global de 2 bits y ~95% precisión]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/ejemplos-reales-de-predictores-de-salto-en-procesadores-come|Ejemplos reales de predictores de salto en procesadores comerciales (PowerPC, UltraSPARC, Pentium, Pentium Pro)]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/limitacion-de-la-btb-solo-predice-saltos-ya-conocidos|Limitación de la BTB: solo predice saltos ya conocidos]]
- 📊 [[memoria/conocimiento/datos/predictores-de-un-nivel-de-historia-1-2-y-3-bits-con-procesa|Predictores de un nivel de historia: 1, 2 y 3 bits con procesadores y años]] · ⚠️ propuesto
- 📊 [[memoria/conocimiento/datos/tabla-historica-de-predictores-en-procesadores-1989-1998|Tabla histórica de predictores en procesadores 1989-1998]]
- 📊 [[memoria/conocimiento/datos/vulnerabilidades-de-seguridad-por-prediccion-especulativa-me|Vulnerabilidades de seguridad por predicción especulativa: Meltdown, Spectre, Branch Privilege Injection]] · ⚠️ propuesto

## Temas relacionados

[[ac]] · [[arquitectura]] · [[arquitectura-computadores]] · [[btb]] · [[instrucciones-predicadas]] · [[pipeline]] · [[bht]] · [[yeh-patt]] · [[compilador]] · [[cpi]] · [[i-cache]] · [[predictor-hibrido]]
