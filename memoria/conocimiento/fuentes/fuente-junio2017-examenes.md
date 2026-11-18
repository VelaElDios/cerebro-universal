---
tipo: "fuente"
titulo: "Junio2017 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Junio2017.pdf`.

## Resumen
Este trozo contiene un examen de Arquitectura de Computadores (curso 2016/17) con 30 preguntas tipo test y dos problemas. El test cubre conceptos fundamentales: definición de arquitectura/organización, leyes de rendimiento (Amdahl, CPI, ciclo de reloj), segmentación, riesgos, planificación estática/dinámica, predicción de saltos, especulación, algoritmo Tomasulo, superescalares, microarquitecturas Intel (P6/P7), GPUs, taxonomía de Flynn, multicomputadores y SMP. Los problemas plantean análisis de dependencias y CPI en un bucle MIPS64 con FP, y simulación de Tomasulo con configuración concreta 
Este trozo contiene dos problemas de un examen de Arquitectura de Computadores (2016/17). El Problema 2 pide simular la ejecución de 7 instrucciones (3 cargas, MUL, ADD, DIV, store) con el algoritmo de Tomasulo básico (sin especulación) y con versión especulativa usando un ROB de 5 entradas, incluyendo el estado del ROB al ciclo 8. El Problema 3 analiza un bucle MIPS64 que recorre la secuencia 0,1,0,2,0,3,0,4,0,5 y pide determinar el comportamiento real de dos saltos (B1: BEQZ, B2: BEQ) y simular un predictor híbrido que combina un predictor local de 1 bit y otro de 3 bits por salto, seleccion

## Lo que se sacó de él (16)
- [[analisis-de-dependencias-en-codigo-fp-con-registro-f1-raw-y]]
- [[aplicacion-de-la-ley-de-amdahl-para-encontrar-fraccion-de-co]]
- [[calculo-de-bits-totales-en-predictor-1-2-con-bht-de-4-entrad]]
- [[como-comparar-rendimiento-de-dos-maquinas-con-mismo-isa-usan]]
- [[comportamiento-real-de-saltos-b1-beqz-y-b2-beq-en-bucle-mips]]
- [[configuracion-y-parametros-para-simular-tomasulo-en-problema]]
- [[definicion-y-objetivo-de-la-planificacion-de-trazas-trace-sc]]
- [[efectos-de-la-especulacion-en-flujo-de-datos-ilp-y-excepcion]]
- [[estado-inicial-de-predictores-y-contadores-en-problema-de-pr]]
- [[estructura-de-tabla-rob-para-tomasulo-especulativo-con-5-ent]]
- [[grado-de-un-superescalar-a-partir-de-su-cpi-ideal]]
- [[predictor-hibrido-de-saltos-con-selectores-de-2-bits-entre-p]]
- [[que-busca-conseguir-la-segmentacion-software-software-pipeli]]
- [[reglas-de-actualizacion-de-contadores-de-seleccion-en-predic]]
- [[simulacion-de-algoritmo-tomasulo-basico-y-especulativo-con-r]]
- [[tasa-de-aciertos-de-predictor-1-bit-inicializado-a-0-con-sal]]
