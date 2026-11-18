---
tipo: "fuente"
titulo: "January2022 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/January2022.pdf`.

## Resumen
Este trozo contiene el examen final de Arquitectura de Computadores de enero 2022: 30 preguntas tipo test que cubren paralelismo, taxonomía de Flynn, cálculo de MIPS y ley de Amdahl, dependencias en bucles (RAW, WAR, WAW), latencia y forwarding, Scoreboard vs Tomasulo, pipelining software, desenrollado de bucles, predicción de saltos (predictor de 2 bits, BTB implícito, BHT), ejecución multicamino, especulación software, bits venenosos, Tomasulo especulativo, superescalar (CPI ideal, etapa de predicción, inconvenientes), VLIW (afirmación falsa), multicore/NUMA, microarquitectura Netburst, comp
Este trozo contiene dos ejercicios de examen de Arquitectura de Computadores (enero 2022). El Ejercicio 2 pide simular la ejecución de 8 instrucciones FP/load en un MIPS64 con Tomasulo especulativo (ROB de 4 entradas, 2 RS por unidad FP, 2 load buffers, latencias: load/store=1, FP mul=6, FP add=4, DIV no dada) y rellenar el estado del ROB al terminar el primer L.D. El Ejercicio 3 pide diagramas de pipeline ciclo a ciclo para un superscalar 4-issue con 5 unidades funcionales y 3 etapas (decode, execute, write) bajo tres modelos: in-order/in-order, out-of-order sin renombrado/in-order write, y o

## Lo que se sacó de él (19)
- [[analisis-de-paradas-en-bucle-con-unidades-fp-de-latencias-2]]
- [[ancho-y-tamano-en-bits-de-un-btb-implicito-con-1024-entradas]]
- [[aplicacion-de-la-ley-de-amdahl-para-determinar-fraccion-de-u]]
- [[calculo-de-mips-pico-a-partir-de-mezcla-de-instrucciones-y-c]]
- [[codigo-de-instrucciones-para-ejercicio-2-tomasulo-especulati]]
- [[comportamiento-de-bits-venenosos-ante-excepcion-terminante-e]]
- [[configuracion-superscalar-4-issue-para-diagramas-de-pipeline]]
- [[cpi-ideal-de-un-superescalar-de-grado-n-es-1-n]]
- [[definicion-de-ejecucion-multicamino-multipath-execution]]
- [[diferencias-clave-entre-los-tres-modelos-de-ejecucion-supers]]
- [[estructura-de-tabla-rob-de-4-entradas-para-volcado-en-ciclo]]
- [[forwarding-de-resultado-en-ciclo-siguiente-al-write-modelo-s]]
- [[identificacion-de-antidependencia-war-entre-store-e-incremen]]
- [[latencias-de-unidades-funcionales-dadas-en-el-examen-fp-y-me]]
- [[parametros-de-simulacion-tomasulo-especulativo-para-mips64-e]]
- [[paso-de-commit-en-tomasulo-especulativo-usa-rob-para-complet]]
- [[pasos-para-simular-tomasulo-especulativo-con-rob-y-restricci]]
- [[restricciones-de-timing-en-tomasulo-con-especulacion-examen]]
- [[secuencia-de-aciertos-fallos-en-predictor-de-2-bits-iniciali]]
