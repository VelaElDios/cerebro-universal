---
tipo: "fuente"
titulo: "June2017 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/June2017.pdf`.

## Resumen
Este trozo contiene el examen final de Arquitectura de Computadores de junio de 2017, compuesto por 30 preguntas tipo test y dos ejercicios prácticos. El test cubre conceptos fundamentales: definición de arquitectura vs organización, tipos de paralelismo (ILP, TLP, DLP), cálculo de rendimiento y ley de Amdahl, pipelining, hazards, planificación estática y dinámica (trace scheduling, software pipelining, loop unrolling), predicción de saltos, especulación, algoritmo de Tomasulo, buffer de reordenación, procesadores superscalar, evolución de Intel (P6/P7, Pentium II/III/IV, Xeon), arquitectura A
Este trozo contiene el Ejercicio 3 de un examen de Arquitectura de Computadores (junio 2017). Presenta un bucle MIPS64 que lee la secuencia 0,1,0,2,0,3,0,4,0,5 y pide: a) determinar los resultados reales (tomado/no tomado) de dos saltos condicionales (B1: BEQZ R2,next y B2: BEQ R1,R3,end); b) simular un predictor híbrido que combina un predictor local de 1 bit (Predictor 1) y otro de 3 bits (Predictor 2) por salto, seleccionados mediante contadores de saturación de 2 bits por salto (MSB=1 → Predictor 1, MSB=0 → Predictor 2). Se incluye una tabla parcialmente resuelta que muestra la evolución d

## Lo que se sacó de él (8)
- [[eleccion-de-predictor-hibrido-con-selector-de-2-bits-frente]]
- [[estado-inicial-de-predictores-y-contadores-en-el-ejercicio-d]]
- [[evolucion-de-predicciones-para-b1-y-b2-con-predictor-hibrido]]
- [[patron-de-prediccion-de-predictor-de-3-bits-ante-alternancia]]
- [[predictor-hibrido-con-selector-de-2-bits-entre-predictor-de]]
- [[predictor-local-de-1-bit-predictor-1-y-predictor-local-de-3]]
- [[reglas-de-actualizacion-del-contador-selector-de-2-bits-en-p]]
- [[resultados-reales-de-saltos-b1-y-b2-en-bucle-mips64-secuenci]]
