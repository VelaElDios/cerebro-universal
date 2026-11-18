---
tipo: "fuente"
titulo: "January2023 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/January2023.pdf`.

## Resumen
Este trozo contiene el examen final de Arquitectura de Computadores (enero 2023) con 30 preguntas tipo test y el inicio de dos ejercicios. El test cubre: benchmarks sintéticos, organización vs arquitectura, leyes de rendimiento (Amdahl), riesgos en pipeline MIPS con forwarding, dependencias en bucles (RAW, WAR, WAW), desenrollamiento de bucles, Scoreboard vs Tomasulo, latencia y penalización de saltos, CPI con predicción, BTB, especulación software/hardware, bits de veneno, superscalar (renombrado, emisión, CPI ideal), predecodificación, speedup por desenrollamiento, tendencias 2004-2020 (tran
Este trozo contiene dos ejercicios de un examen de Arquitectura de Computadores (enero 2023). El Ejercicio 2 pide simular la ejecución de una secuencia de instrucciones FP en un procesador con algoritmo Tomasulo, detallando ciclos de issue, ejecución, escritura de resultado y commit, junto con causas de parada (RAW, estructural, orden de programa). Se dan parámetros concretos: latencias de unidades FP (adder 4, multiplier 6, divider 12), ROB de 4 entradas, 2 reservation stations por unidad FP, 1 load buffer y 1 store buffer, carga/almacenamiento en 2 ciclos, y restricciones de uso del CDB y li

## Lo que se sacó de él (16)
- [[calculo-de-efectividad-de-programa-vliw-original-vs-desenrol]]
- [[calculo-de-mejora-necesaria-con-ley-de-amdahl-ejemplo-multip]]
- [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]]
- [[codigo-vliw-bucle-original-examen-enero-2023-4-slots-7-instr]]
- [[como-desenrollar-4-veces-y-planificar-bucle-vliw-para-maximo]]
- [[configuracion-tomasulo-examen-enero-2023-unidades-fp-rob-buf]]
- [[cpi-con-prediccion-de-saltos-en-pipeline-de-5-etapas-direcci]]
- [[definicion-de-benchmarks-sinteticos]]
- [[definicion-de-latencia-de-salto-y-penalizacion-por-fallo-de]]
- [[diferencia-entre-especulacion-software-y-hardware-falso-en-s]]
- [[latencias-de-unidades-funcionales-vliw-examen-enero-2023-int]]
- [[objetivo-del-desenrollamiento-de-bucles-loop-unrolling]]
- [[obtencion-de-operandos-y-deteccion-waw-war-en-scoreboard]]
- [[proposito-del-branch-target-buffer-btb-ademas-de-bits-de-pre]]
- [[riesgo-load-use-en-pipeline-mips-con-forwarding]]
- [[secuencia-de-instrucciones-para-simulacion-tomasulo-examen-e]]
