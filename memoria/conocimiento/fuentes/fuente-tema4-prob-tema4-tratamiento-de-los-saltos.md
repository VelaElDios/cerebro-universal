---
tipo: "fuente"
titulo: "Tema4 Prob (Tema4-Tratamiento de los saltos)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4_Prob.pdf`.

## Resumen
Este trozo contiene una colección de 10 ejercicios del Tema 4 "Tratamiento de los Saltos" de Arquitectura de Computadores (curso 2026-2027). Los ejercicios cubren predictores de 1, 2, 3 y n bits (contadores saturados), predictores correlacionados (m,n), predictores híbridos de torneo y combinados, buffers de destino de salto (BTB) con políticas de actualización y penalizaciones, y cálculos de CPI y speedup. Se usan bucles en C y código RISC-V con secuencias de datos concretas para analizar el comportamiento en estado estable y la evolución de los contadores de predicción.
Este trozo contiene tres ejercicios de predicción de saltos (Ejercicios 10, 11, 12) con código RISC-V y tablas para rellenar. El Ejercicio 10 usa un predictor correlacionado (2,1) sobre un bucle que cuenta letras 'a' en "exam18". El Ejercicio 11 presenta un predictor híbrido que combina un predictor local de 1-bit y otro de 3-bits por salto, con una tabla de contadores de 2-bits saturados que elige entre ellos. El Ejercicio 12 analiza un bucle sobre vector disperso (0,7,0,0,0,0,2,0) con un predictor de 2-bits por instrucción y otro correlacionado (2,1), ambos con estados iniciales dados.

## Lo que se sacó de él (19)
- [[analisis-en-estado-estable-de-predictor-2-bits-vs-correlacio]]
- [[calculo-de-cpi-sin-btb-y-speedup-con-btb-miss-rate-10-solo-s]]
- [[calculo-de-predicciones-correctas-en-bucles-anidados-con-pre]]
- [[calculo-de-speedup-comparando-predictor-con-penalidad-variab]]
- [[codigo-risc-v-ejercicio-10-bucle-conteo-a-en-exam18-con-salt]]
- [[codigo-risc-v-ejercicio-11-bucle-fibonacci-6-elementos-con-s]]
- [[codigo-risc-v-ejercicio-12-bucle-vector-disperso-0-7-0-0-0-0]]
- [[como-disenar-un-bucle-que-haga-fallar-siempre-un-predictor-d]]
- [[comportamiento-real-de-saltos-b1-y-b2-en-bucle-risc-v-que-re]]
- [[estado-inicial-de-predictores-en-ejercicio-12-predictor-2-bi]]
- [[estructura-y-funcionamiento-de-predictor-hibrido-de-torneo-c]]
- [[evaluacion-de-rendimiento-de-btb-con-politica-de-solo-saltos]]
- [[predictor-correlacionado-2-1-para-bucle-de-conteo-de-caracte]]
- [[predictor-de-2-bits-por-instruccion-y-predictor-correlaciona]]
- [[predictor-hibrido-con-predictores-locales-de-1-bit-y-3-bits]]
- [[predictor-hibrido-que-combina-dos-predictores-locales-1-bit]]
- [[simulacion-de-predictores-1-bit-4-bits-saturado-y-correlacio]]
- [[simulacion-paso-a-paso-de-predictor-correlacionado-2-1-con-b]]
- [[tabla-de-actualizacion-de-contadores-de-2-bits-saturados-par]]
