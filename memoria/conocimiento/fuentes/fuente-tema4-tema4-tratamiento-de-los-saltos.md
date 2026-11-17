---
tipo: "fuente"
titulo: "Tema4 (Tema4-Tratamiento de los saltos)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`.

## Resumen
Este trozo introduce el tema "Tratamiento de los saltos" en Arquitectura de Computadores. Define la latencia de salto y los huecos de retardo, presenta estadísticas sobre frecuencia y tipos de saltos (1 de cada 6 instrucciones es salto tomado, 85% de saltos hacia atrás tomados, 60% hacia delante), y calcula penalizaciones en un pipeline de 5 etapas según en qué etapa se resuelva el sentido y la dirección del salto (1, 2 o 3 ciclos de penalización).
Este trozo del Tema 4 de Arquitectura de Computadores cubre la predicción de saltos condicionales: planteamiento general (ejecución especulativa y recuperación), detección de instrucciones de salto (tres alternativas con ejemplos de procesadores), taxonomía de técnicas de predicción (fija, estática, dinámica con subclasificaciones), recuperación de fallos de predicción (costes en ciclos y mecanismos con registros temporales), predicción dinámica basada en correlación temporal y espacial, predictores de un nivel de historia (1, 2 y 3 bits con procesadores y años), y el funcionamiento detallado 
Este trozo explica los predictores dinámicos de salto de 2 bits (Jim Smith, 1981) y los predictores correlacionados o de dos niveles. Detalla la máquina de 4 estados del predictor de 2 bits, su implementación mediante Branch History Table (BHT), cómo resuelve el problema de bucles anidados, y la generalización a predictores (m,n) que usan historia global (BHR) para seleccionar entre múltiples BHTs. Incluye un ejemplo comparativo exhaustivo con código que muestra tasas de fallo: predictor de 1 bit (100% fallos), de 2 bits (50% fallos) y correlacionado (1,1) con mejor rendimiento. Menciona que e
Este trozo cubre predictores de salto correlacionados y adaptativos de dos niveles (Yeh y Patt), su notación XAx(m,2n), variantes gselect/gshare para combinar BHR y PC, predictores híbridos (McFarling, Alpha 21264) y una tabla histórica de predictores en procesadores de 1989 a 1998.
Este trozo describe las estructuras hardware para implementar predicción de saltos: BTAC (caché de direcciones destino), BHT (tabla de historial de predicción), bits de predicción en la I-caché y BTB (combinación de BTAC y bits). Incluye ejemplos reales de procesadores (PowerPC, UltraSPARC, Pentium, Pentium Pro) y mecanismos de recuperación ante fallos de predicción.
Este trozo final del tema 4 cubre la actualización de la BTB tras ejecutar el salto, la predicción implícita sin bits de predicción, el diagrama de flujo de la BTB, las vulnerabilidades de seguridad derivadas de la predicción especulativa (Meltdown, Spectre, Branch Privilege Injection), las instrucciones predicadas como alternativa para eliminar saltos (con ejemplo de código y ventajas/inconvenientes), y la ejecución multicamino como técnica poco usada.

## Lo que se sacó de él (51)
- [[actualizacion-de-la-btb-tras-ejecutar-el-salto]]
- [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
- [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]]
- [[bibliografia-de-referencia-para-el-tema-de-prediccion-de-sal]]
- [[bits-de-prediccion-en-la-i-cache-funcionamiento-y-ventajas]]
- [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]]
- [[calculo-de-penalizacion-de-salto-condicional-en-pipeline-de]]
- [[como-el-predictor-de-2-bits-resuelve-el-problema-de-bucles-a]]
- [[costes-de-recuperacion-de-fallos-de-prediccion-por-procesado]]
- [[definicion-de-latencia-de-salto-y-huecos-de-retardo]]
- [[diseno-de-btac-cache-asociativa-por-conjuntos-como-opcion-ma]]
- [[ejecucion-multicamino-multi-path-execution-como-alternativa]]
- [[ejemplo-comparativo-predictores-1-bit-vs-2-bits-vs-correlaci]]
- [[ejemplo-de-transformacion-de-salto-a-instrucciones-predicada]]
- [[ejemplo-gas-4-22-predictor-dos-niveles]]
- [[ejemplo-pentium-pro-predictor-2-2-con-historia-global-de-2-b]]
- [[ejemplos-reales-de-predictores-de-salto-en-procesadores-come]]
- [[esquemas-de-pipeline-con-1-2-y-3-huecos-de-retardo-para-beqz]]
- [[estadisticas-de-frecuencia-y-tipos-de-saltos-en-programas-ti]]
- [[estructuras-hardware-para-prediccion-de-saltos-btac-bht-btb]]
- [[funcionamiento-y-actualizacion-de-la-btac-branch-target-addr]]
- [[impacto-de-la-frecuencia-de-saltos-en-el-ilp-y-tamano-de-blo]]
- [[implementacion-bht-para-predictor-de-2-bits-4k-entradas-80-9]]
- [[implementacion-predictor-correlacionado-m-n-con-bhr-y-bht]]
- [[indice-sucesor-en-la-i-cache-para-prediccion-de-saltos-alter]]
- [[instrucciones-predicadas-convertir-dependencias-de-control-e]]
- [[limitacion-de-la-btb-solo-predice-saltos-ya-conocidos]]
- [[mecanismos-de-recuperacion-ante-fallos-de-prediccion-de-salt]]
- [[multiples-caminos-como-tecnica-de-prediccion-de-saltos]]
- [[notacion-xax-m-2n-para-predictores-adaptativos-de-dos-nivele]]
- [[planteamiento-general-de-prediccion-de-saltos-con-ejecucion]]
- [[prediccion-dinamica-basada-en-correlacion-temporal-y-espacia]]
- [[prediccion-implicita-sin-bits-de-prediccion-en-btb]]
- [[predictor-alpha-21264-tournament-branch-prediction-combina-l]]
- [[predictor-correlacionado-1-1-bhr-de-1-bit-y-2-tablas-bht-de]]
- [[predictor-correlacionado-general-mejora-a-predictores-no-cor]]
- [[predictor-correlacionado-o-de-dos-niveles-m-n-correlacion-es]]
- [[predictor-dinamico-de-2-bits-jim-smith-1981-maquina-de-4-est]]
- [[predictor-dinamico-de-un-bit-funcionamiento-y-limitacion-en]]
- [[predictor-gselect-concatenacion-vs-gshare-xor-para-indexar-b]]
- [[predictor-hibrido-mcfarling-con-contador-saturado-de-2-bits]]
- [[predictores-de-un-nivel-de-historia-1-2-y-3-bits-con-procesa]]
- [[predictores-n-bits-y-optimalidad-de-n-2-en-la-practica]]
- [[recuperacion-de-fallos-de-prediccion-con-registros-temporale]]
- [[salto-retardado-y-instrucciones-predicadas-como-alternativas]]
- [[suposicion-de-cauce-detenido-durante-huecos-de-retardo-para]]
- [[tabla-historica-de-predictores-en-procesadores-1989-1998]]
- [[taxonomia-de-tecnicas-de-prediccion-de-saltos]]
- [[ventajas-e-inconvenientes-de-las-instrucciones-predicadas]]
- [[vulnerabilidades-de-seguridad-por-prediccion-especulativa-me]]
- [[yeh-y-patt-recomiendan-g-g-para-enteros-y-s-s-para-coma-flot]]
