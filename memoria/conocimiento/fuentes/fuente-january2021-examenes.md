---
tipo: "fuente"
titulo: "January2021 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/January2021.pdf`.

## Resumen
Este trozo contiene un examen final de Arquitectura de Computadores (enero 2021) con 30 preguntas tipo test sobre organización vs arquitectura, métricas de rendimiento (MIPS, coste-efectividad, ley de Amdahl), dependencias de datos y control, predicción de saltos, algoritmo Scoreboard, Tomasulo con bits de veneno, superescalar, VLIW, consumo, multinúcleo, multi-hilo, GRID, SIMD/GPU y modelos cloud. Incluye dos ejercicios: uno de análisis de riesgos en pipeline y *software pipelining* para un bucle de monitor CO₂, y otro (incompleto) sobre especulación por hardware con Tomasulo.
Este trozo contiene dos ejercicios de un examen final de Arquitectura de Computadores (enero 2021). El primero pide simular la ejecución de 10 instrucciones FP en un algoritmo Tomasulo con ROB de 8 entradas, buffers de carga y estaciones de reserva específicas, unidades funcionales con latencias dadas (FP Adder 2 ciclos, FP Multiplier 4, FP Divider 8 no segmentado, LOAD/STORE 2, INT ALU 1) y reglas de CDB y liberación de recursos. El segundo ejercicio compara un procesador superscalar MIPS64 de 4 emisiones/ciclo (2 enteros + 2 FP) frente a un VLIW de 4 operaciones/ciclo sin restricciones de ti

## Lo que se sacó de él (19)
- [[aplicacion-de-la-ley-de-amdahl-para-calcular-fraccion-de-tie]]
- [[calculo-de-instrucciones-tras-desenrollar-bucle-3-veces-unro]]
- [[calculo-de-mips-nativo-a-partir-de-mezcla-de-instrucciones-y]]
- [[codigo-de-bucle-base-para-desenrollado-l-d-add-d-s-d-daddui]]
- [[comparativa-eficiencia-operaciones-ciclo-superscalar-con-res]]
- [[configuracion-tomasulo-con-rob-para-simulacion-de-examen-ene]]
- [[definicion-de-dependencia-de-datos-raw-entre-instrucciones]]
- [[desenrollado-8-del-bucle-l-d-add-d-s-d-daddui-bne-para-sched]]
- [[eliminacion-de-dependencias-de-salida-waw-mediante-renombrad]]
- [[estructura-de-un-predictor-correlacionado-2-4-4-bhr-y-2-bht]]
- [[identificacion-de-antidependencia-entre-iteraciones-en-bucle]]
- [[implementacion-del-bhr-branch-history-register-en-predictor]]
- [[orden-de-emision-issue-en-scoreboard-orden-de-programa]]
- [[procesador-a-mips64-superscalar-5-etapas-4-emisiones-ciclo-2]]
- [[procesador-b-vliw-4-operaciones-ciclo-sin-restricciones-de-t]]
- [[reglas-de-cdb-y-liberacion-de-recursos-en-tomasulo-con-rob]]
- [[salto-retardado-delayed-branch-en-bucle-con-bne-y-daddui]]
- [[tabla-de-latencias-fp-para-desenrollado-de-bucle-examen-ener]]
- [[valor-inmediato-de-daddui-tras-desenrollar-3-un-bucle-con-da]]
