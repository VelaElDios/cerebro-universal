---
tipo: "fuente"
titulo: "January2019 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/January2019.pdf`.

## Resumen
Este trozo contiene un examen final de Arquitectura de Computadores (enero 2019) con 30 preguntas tipo test y un ejercicio de algoritmo de Tomasulo (con y sin especulación). El test cubre: ley de Amdahl, speedup, cálculo de MIPS, clasificación de procesadores (SISD/SIMD/MIMD), VLIW, superscalar, dependencias en pipeline, planificación por software, trace scheduling, planificación dinámica, predicción de saltos de dos niveles, especulación, bits de veneno, ROB, paso de commit, ventana de instrucciones, recuperación tras fallo de predicción, disipación de potencia, microarquitectura Intel P6, SM
Este trozo contiene dos ejercicios de un examen de Arquitectura de Computadores (enero 2019). El ejercicio 2 plantea un predictor de saltos híbrido que combina un predictor local de 1 bit y otro de 3 bits por instrucción de salto, seleccionados mediante un contador saturante de 2 bits por salto; se pide simular su comportamiento para las dos ramas (B1, B2) de un bucle MIPS64 que recorre los seis primeros números de Fibonacci. El ejercicio 3 pide planificar (schedule) un bucle en un procesador VLIW con 6 unidades funcionales (2 enteras, 2 memoria, 1 FP adder, 1 FP multiplier) con latencias dada

## Lo que se sacó de él (17)
- [[calculo-de-bits-en-predictor-de-dos-niveles-n-m-con-k-entrad]]
- [[codigo-del-bucle-vliw-para-planificacion-cargas-fp-mul-s-add]]
- [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]]
- [[desenrollamiento-de-bucle-3x-y-re-planificacion-en-vliw-para]]
- [[especulacion-en-hardware-resultado-definitivo-en-el-paso-de]]
- [[instruccion-especulativa-ejecutada-antes-de-saber-si-realmen]]
- [[paso-de-commit-en-superscalar-actualizacion-de-registros]]
- [[planificacion-dinamica-sin-especulacion-orden-de-ejecucion-d]]
- [[planificacion-scheduling-de-bucle-en-vliw-con-forwarding-y-d]]
- [[predictor-hibrido-de-dos-predictores-locales-con-selector-po]]
- [[procesadores-superscalar-son-maquinas-sisd]]
- [[simulacion-paso-a-paso-del-predictor-hibrido-para-el-bucle-d]]
- [[speedup-no-tiene-unidades-de-medida]]
- [[trace-scheduling-traza-secuencia-mas-probable-de-bloques-bas]]
- [[uso-de-delayed-branch-con-1-delay-slot-en-vliw-para-ocultar]]
- [[ventana-de-instrucciones-en-superscalar-instrucciones-decodi]]
- [[vliw-el-compilador-empaqueta-varias-operaciones-en-una-instr]]
