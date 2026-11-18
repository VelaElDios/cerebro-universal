---
tipo: "fuente"
titulo: "Enero2014 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2014.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Enero2014.pdf`.

## Resumen
Examen de Arquitectura de Computadores (Enero 2014) con test de 30 preguntas y dos problemas. El test cubre métricas de rendimiento (tiempo de ejecución, MIPS, CPI, speedup), riesgos de pipeline (RAW, WAR, WAW), dependencias y renombramiento, desenrollamiento de bucles, algoritmo de Tomasulo (CDB, ROB, especulación), predicción de saltos (BHT, BTB, gshare, BHR), superescalar (CPI ideal), arquitecturas comerciales (Intel P6/P7, HyperTransport AMD, ARM), GPU (cambio de contexto sin penalización), clústeres, MPI, CC-NUMA y Cloud. El Problema 1 pide analizar dependencias, aplicar segmentación soft
Este trozo contiene el Problema 3 del examen de Arquitectura de Computadores (Enero 2014). Evalúa tres mecanismos de especulación estática en un procesador MIPS64: (a) sin soporte para especulación, (b) cooperación hardware/software sin distinguir instrucciones normales de especulativas, y (c) especulación con poison bits. El código incluye cargas especulativas (LW*) a dirección 0 (prohibida, lanza excepción) y saltos condicionales. Se proporciona estado inicial de registros (R1=10, R2=0, R3=0, R4=4, R5=5, R6=6, R7=7, R8=8, R9=9) y tablas para resolver cada caso indicando qué instrucciones lan

## Lo que se sacó de él (18)
- [[analisis-de-codigo-con-especulacion-estatica-para-examen-ac]]
- [[calculo-de-cpi-en-implementacion-multiciclo-mips-con-mezcla]]
- [[convencion-etiquetas-indefinido-y-sucio-para-poison-bits-en]]
- [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]]
- [[definicion-de-riesgo-raw-read-after-write]]
- [[eliminacion-de-dependencias-de-datos-mediante-renombramiento]]
- [[especulacion-con-poison-bits-propagacion-y-excepcion-diferid]]
- [[especulacion-estatica-con-cargas-especulativas-lw-en-mips64]]
- [[estado-inicial-de-registros-y-restriccion-memoria-direccion]]
- [[interpretacion-de-speedup-del-200]]
- [[mecanismo-cooperacion-hardware-software-sin-distincion-instr]]
- [[mejor-medida-de-rendimiento-de-un-computador]]
- [[objetivo-de-la-segmentacion-software-software-pipelining]]
- [[procesador-sin-soporte-para-especulacion-comportamiento-ante]]
- [[salto-retardado-delayed-branch-como-planificacion-estatica]]
- [[seleccion-de-entrada-en-bht-branch-history-table]]
- [[tomasulo-resultados-via-common-data-bus-cdb]]
- [[tres-mecanismos-de-especulacion-evaluados-en-examen-ac-enero]]
