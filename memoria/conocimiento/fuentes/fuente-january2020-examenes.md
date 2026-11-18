---
tipo: "fuente"
titulo: "January2020 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/January2020.pdf`.

## Resumen
Este trozo contiene un examen final de Arquitectura de Computadores (enero 2020) con 30 preguntas tipo test y dos ejercicios prácticos. El test cubre conceptos fundamentales: distinción arquitectura/organización/tecnología, VLIW, SISD/ILP, cálculo de MIPS y speedup (ley de Amdahl), coste-efectividad, riesgos de pipeline (RAW/WAR/WAW), forwarding, planificación por software, Scoreboard, predicción de saltos de dos niveles, especulación con poison bits, Reorder Buffer, desambiguación de memoria, VLIW, superscalar, arquitecturas load/store, multicore, GPU/TPU, computación cuántica, multihilo, CUD
Este trozo contiene tres ejercicios de un examen de Arquitectura de Computadores (enero 2020): (1) completar tablas de estado de instrucciones para el algoritmo de Tomasulo sin y con especulación (ROB de 6 entradas) para una secuencia de 10 instrucciones FP; (2) analizar el comportamiento real de dos saltos anidados (B1, B2) con R1=2, R2=4 y simular un predictor híbrido que combina predictores locales de 1 y 2 bits con un contador de selección de 2 bits por salto; (3) planificar código en un superescalar 3-vías (entero/salto, memoria, FP) con latencias ADD.D=2, MUL.D=4, forwarding y ranura de

## Lo que se sacó de él (20)
- [[aplicacion-de-la-ley-de-amdahl-para-speedup-global-mejorando]]
- [[calculo-de-coste-efectividad-rendimiento-precio-entre-dos-co]]
- [[calculo-de-mips-para-comparar-dos-computadores-con-mismo-isa]]
- [[como-rellenar-la-tabla-de-estado-de-instrucciones-en-tomasul]]
- [[como-rellenar-la-tabla-de-estado-en-tomasulo-con-especulacio]]
- [[definicion-de-procesador-vliw]]
- [[dependencia-de-salida-waw-en-pipeline-con-forwarding]]
- [[desenrollado-de-bucles-loop-unrolling-en-superescalar-con-re]]
- [[distincion-entre-arquitectura-organizacion-y-tecnologia-en-p]]
- [[planificacion-en-scoreboard-orden-de-ejecucion]]
- [[planificacion-en-superescalar-3-vias-entero-salto-memoria-fp]]
- [[planificacion-por-software-software-pipelining-y-desenrollad]]
- [[predictor-hibrido-con-selectores-por-salto-1-bit-vs-2-bit-y]]
- [[resultados-reales-de-saltos-b1-y-b2-en-bucles-anidados-con-r]]
- [[riesgo-raw-read-after-write-y-su-causa]]
- [[secuencia-de-instrucciones-fp-del-examen-para-tomasulo-10-in]]
- [[simulacion-paso-a-paso-del-predictor-hibrido-con-contadores]]
- [[superescalar-3-vias-con-tuberias-dedicadas-por-tipo-de-instr]]
- [[tecnica-de-mejora-de-rendimiento-en-sisd]]
- [[uso-de-ranura-de-retardo-de-1-ciclo-en-superescalar-para-ocu]]
