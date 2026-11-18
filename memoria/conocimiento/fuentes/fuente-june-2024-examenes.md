---
tipo: "fuente"
titulo: "June 2024 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/June 2024.pdf`.

## Resumen
Este trozo corresponde a un examen final de Arquitectura de Computadores (junio 2024) que incluye 30 preguntas tipo test y dos ejercicios. Las preguntas abarcan jerarquía ISA/organización/tecnología, benchmarks (Linpack), ley de Amdahl, coste-efectividad, etapas de pipeline (banco de registros), hazards vs dependencias, dependencias de nombre (WAW/WAR), loop unrolling, planificación dinámica (Tomasulo, división de ID, CDB), predicción de saltos (BHTs en predictores correlacionados, contadores saturantes, BHR), ROB, ejecución especulativa (poison bits), superscalar (CPI ideal, emisión, excepcio
Este trozo contiene el Ejercicio 3 de un examen de Arquitectura de Computadores (junio 2024). Se pide comparar el rendimiento en instrucciones por ciclo de dos procesadores (A: superscalar MIPS64 4-issue con 2 enteros + 2 FP; B: VLIW 4-issue sin restricciones de tipo) al ejecutar un bucle que calcula y(i) = A * x(i)^2. Se proporciona una tabla de latencias para instrucciones consecutivas (ALU PF→ALU PF: 3 ciclos, ALU PF→S.D: 2, L.D→ALU PF: 1). Se asume forwarding, ramas retrasadas y unidades funcionales totalmente segmentadas. Las preguntas requieren: a) desenrollar 8 veces y planificar para A

## Lo que se sacó de él (18)
- [[banco-de-registros-en-pipeline-mips-se-accede-en-etapas-id-y]]
- [[bucle-de-calculo-y-i-a-x-i-2-en-ensamblador-mips64]]
- [[calculo-de-cost-effectiveness-entre-dos-sistemas-con-cargas]]
- [[calculo-de-speedup-con-ley-de-amdahl-mejora-10x-en-punto-flo]]
- [[contador-saturante-de-3-bits-en-estado-111-indica-tres-tomas]]
- [[desenrollado-de-bucle-8-veces-para-superscalar-con-latencias]]
- [[desenrollamiento-de-bucles-loop-unrolling-permite-planificar]]
- [[ejercicio-simulacion-de-predictores-de-2-bits-vs-correlacion]]
- [[metrica-de-comparacion-operaciones-por-ciclo-ipc-en-supersca]]
- [[name-dependency-dependencia-de-nombre-incluye-waw-y-war]]
- [[planificacion-dinamica-etapa-id-se-divide-en-emision-issue-y]]
- [[planificacion-estatica-agresiva-para-vliw-4-issue-con-renomb]]
- [[predictor-correlacionado-m-n-numero-de-bhts-2-m]]
- [[procesador-a-superscalar-mips64-4-issue-2-enteros-2-fp]]
- [[procesador-b-vliw-4-issue-sin-restricciones-de-tipo-con-plan]]
- [[registro-de-historial-de-saltos-bhr-se-implementa-como-regis]]
- [[suposiciones-del-problema-forwarding-ramas-retrasadas-unidad]]
- [[tabla-de-latencias-para-instrucciones-consecutivas-en-mips64]]
