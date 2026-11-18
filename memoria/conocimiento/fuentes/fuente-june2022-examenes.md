---
tipo: "fuente"
titulo: "June2022 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/June2022.pdf`.

## Resumen
Examen final de Arquitectura de Computadores (junio 2022) con 30 preguntas tipo test sobre jerarquía de memoria, ley de Amdahl, coste-efectividad, dependencias en pipeline, bloque básico, Scoreboard, planificación por software, Tomasulo, predicción de saltos (2-bit, correlador, BHR), bits venenosos, especulación, ROB, VLIW, superscalar, P6, multinúcleo, ISA load-store, cloud, TLP, CUDA y SETI; más dos ejercicios: planificación por software de un bucle MIPS64 de coma flotante y análisis de predicción de saltos en un bucle que cuenta pares.
Este trozo contiene dos ejercicios de examen de Arquitectura de Computadores (junio 2022). El primero pide simular predictores de salto (one-level de 2 bits y two-level correlacionante (2,1)) para un vector de entrada dado y estado inicial. El segundo pide desenrollar 4 veces un bucle con instrucciones de punto flotante y enteras, renombrar registros, y planificar el código en un superscalar MIPS64 de 4 vías (2 enteros + 2 FP) y en un VLIW de 4 operaciones sin restricciones, dadas latencias concretas (MEM 2 ciclos, ADD.D 1 ciclo, MUL.D 3 ciclos) y branch delayed de 2 slots, para luego comparar

## Lo que se sacó de él (18)
- [[calculo-de-coste-efectividad-entre-dos-sistemas-pregunta-4]]
- [[calculo-de-factor-de-mejora-en-multiplicacion-segun-ley-de-a]]
- [[comparativa-eficiencia-operations-per-cycle-opc-superscalar]]
- [[definicion-de-bloque-basico-en-paralelismo-a-nivel-de-instru]]
- [[desenrollado-4x-de-bucle-mips64-fp-con-renombrado-de-registr]]
- [[gestion-de-riesgos-war-y-waw-en-tomasulo-pregunta-10]]
- [[informacion-almacenada-en-estaciones-de-reserva-de-tomasulo]]
- [[parametros-de-temporizacion-del-examen-ac-june-2022-exercise]]
- [[planificacion-en-superscalar-mips64-4-vias-2-enteros-2-fp-co]]
- [[planificacion-en-vliw-4-operaciones-sin-restricciones-de-tip]]
- [[proposito-de-la-planificacion-por-software-software-pipelini]]
- [[riesgo-estructural-en-scoreboard-pregunta-7]]
- [[secuencia-h-m-para-predictor-2-bit-debilmente-no-tomado-en-b]]
- [[secuencia-h-m-para-predictor-correlacionado-1-1-en-bucle-de]]
- [[simulacion-de-predictor-one-level-de-2-bits-para-dos-saltos]]
- [[simulacion-de-predictor-two-level-correlacionante-2-1-con-bh]]
- [[valor-de-bhr-de-5-bits-para-bucles-anidados-i-6-j-0-pregunta]]
- [[vector-de-entrada-y-estado-inicial-para-simulacion-de-predic]]
