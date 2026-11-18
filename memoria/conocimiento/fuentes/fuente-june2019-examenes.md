---
tipo: "fuente"
titulo: "June2019 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/June2019.pdf`.

## Resumen
Este trozo contiene el examen final de Arquitectura de Computadores de junio de 2019: 30 preguntas tipo test sobre ley de Amdahl, coste-efectividad, jerarquía de memoria, dependencias de datos, planificación dinámica, predicción de saltos, especulación, Tomasulo, superscalar, arquitecturas (ARM, Itanium), multiprocesadores, MPI y cloud; y dos ejercicios prácticos: (1) desenrollado y planificación de un bucle con división flotante de 6 ciclos en MIPS64, y simulación de Tomasulo especulativo con ROB; (2) traza de un predictor híbrido (local 1-bit + global (2,1)) sobre un bucle que recorre un vec
Este trozo contiene dos partes: primero, la descripción de un selector de 2 bits (contador de saturación) que elige entre dos predictores de salto basándose en sus aciertos/fallos; segundo, el Enunciado del Ejercicio 3 del examen de Arquitectura de Computadores (junio 2019) que pide detallar la ejecución de un código de 10 instrucciones en dos procesadores: A (superscalar 2-vías, in-order, sin renombrado) y B (VLIW 2 operaciones, planificación estática agresiva, con renombrado). Se dan latencias: carga MEM=2 ciclos, multiplicación EX=2 ciclos, resto 1 ciclo; unidades totalmente segmentadas, fo

## Lo que se sacó de él (19)
- [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]]
- [[bht-en-predictor-dinamico-de-3-bits-contadores-de-saturacion]]
- [[calculo-de-speedup-con-ley-de-amdahl-fraccion-mejorada-al-do]]
- [[codigo-de-10-instrucciones-del-exercise-3-ac-june-2019]]
- [[comparativa-de-coste-efectividad-entre-sistemas-rendimiento]]
- [[diferencias-clave-processor-a-superscalar-in-order-vs-proces]]
- [[ejercicio-3-ac-june-2019-comparacion-superscalar-in-order-vs]]
- [[excepcion-terminante-en-instruccion-especulativa-se-pospone]]
- [[inicializacion-del-selector-y-bits-de-prediccion-en-predicto]]
- [[las-dependencias-de-datos-verdaderas-no-se-pueden-eliminar-e]]
- [[latencias-de-instrucciones-y-supuestos-de-pipeline-en-exerci]]
- [[limite-de-la-ley-de-amdahl-mejora-imposible-si-la-fraccion-n]]
- [[pasos-para-resolver-exercise-3-processor-a-superscalar-in-or]]
- [[pasos-para-resolver-exercise-3-processor-b-vliw-con-renombra]]
- [[predictor-correlacionado-1-2-bhr-11-tras-dos-saltos-tomados]]
- [[reglas-de-actualizacion-del-selector-hibrido-de-2-bits]]
- [[scoreboard-detiene-ejecucion-ante-hazards-war-y-waw]]
- [[selector-de-2-bits-para-predictor-hibrido-de-saltos]]
- [[tecnica-poisson-carga-especulativa-con-direccion-invalida-po]]
