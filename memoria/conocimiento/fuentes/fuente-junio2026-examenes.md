---
tipo: "fuente"
titulo: "Junio2026 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Junio2026.pdf`.

## Resumen
Este trozo contiene un examen de Arquitectura de Computadores (convocatoria extraordinaria 2025/26) con 30 preguntas tipo test que cubren: ley de Amdahl, cálculo de MIPS y speedup, dependencias en pipeline RISC-V (RAW, WAR, WAW), riesgos en bucles, ILP, planificación estática, desenrollamiento de bucles, algoritmo de Tomasulo, predictores de salto correlacionados y de 2 bits, BTB, bits de veneno en especulación, ejecución especulativa, CPI en superescalar, diferencias VLIW/superescalar, ROB, grado de emisión, compiladores VLIW, compatibilidad binaria, sectores de mercado, consumo de potencia, 
El trozo contiene tres problemas de un examen de Arquitectura de Computadores (curso 2025/26). Problema 1: calibración lineal de IMU en bucle RISC-V, análisis de hazards en pipeline in-order 5 etapas con UF FP de 5 y 4 ciclos, desenrollado 4x con salto retardado, speedup y efecto de intervalo de iniciación 2 en multiplicador FP. Problema 2: simulación de Tomasulo con especulación (ROB 6 entradas, 2 RS por UF FP, buffer carga 1, latencias fld/fsd=2, fmul=6, fadd=2, regla CDB y recurso libre en ciclo siguiente) para una secuencia de 7 instrucciones, y estado del ROB tras emitir el segundo fadd.d

## Lo que se sacó de él (20)
- [[antidependencia-war-entre-instrucciones-consecutivas-en-risc]]
- [[bits-de-veneno-poison-bits-en-carga-especulativa-marcan-regi]]
- [[bucle-risc-v-para-calibracion-imu-con-puntero-descendente]]
- [[calculo-de-ganancia-de-velocidad-speedup-con-la-ley-de-amdah]]
- [[calculo-de-mips-pico-a-partir-de-mezcla-de-instrucciones-y-f]]
- [[calculo-de-speedup-para-bucle-desenrollado-en-pipeline-con-h]]
- [[calibracion-lineal-de-giroscopio-imu-para-compensar-desvio-t]]
- [[dependencia-de-datos-entre-iteraciones-en-bucle-con-actualiz]]
- [[dependencia-raw-en-pipeline-risc-v-resuelta-con-adelantamien]]
- [[desenrollado-de-bucle-4x-con-salto-retardado-para-eliminar-s]]
- [[diferencia-fundamental-vliw-vs-superescalar-compilador-vs-ha]]
- [[efecto-de-intervalo-de-iniciacion-2-en-multiplicador-fp-sobr]]
- [[estado-del-rob-tras-emitir-el-segundo-fadd-d-instruccion-6-e]]
- [[implementacion-de-btb-generica-ampliacion-de-btac-con-bits-d]]
- [[latencias-y-grado-de-segmentacion-de-uf-fp-en-problema-1]]
- [[numero-de-tablas-bht-en-predictor-correlacionado-m-n]]
- [[parametros-de-pipeline-in-order-5-etapas-para-analisis-de-ha]]
- [[parametros-de-tomasulo-con-especulacion-para-problema-2-exam]]
- [[simulacion-paso-a-paso-de-tomasulo-con-especulacion-tabla-ci]]
- [[tasa-de-fallos-de-predictor-dinamico-de-2-bits-inicializado]]
