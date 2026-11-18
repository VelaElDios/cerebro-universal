---
tipo: "fuente"
titulo: "Junio2016 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/Junio2016.pdf`.

## Resumen
Este trozo corresponde a un examen de Arquitectura de Computadores (curso 2015/16) que incluye 30 preguntas tipo test y el inicio de dos problemas. El test cubre cálculo de tiempo de ejecución y speedup (Ley de Amdahl), definiciones de arquitectura/organización, taxonomía de Flynn, dependencias de datos y nombre, riesgos de pipeline (RAW, WAR, WAW), bloque básico, algoritmo de Tomasulo, planificación dinámica, predictores de salto (correlacionado, BTB, gselect), especulación con bits venenosos, Reorder Buffer, superescalar, etapa commit, arquitecturas Cortex-A9/Alpha/P7, GPUs, MPI, cloud, CC-N
Este trozo contiene dos problemas de un examen de Arquitectura de Computadores. El primero (incompleto) pide completar una tabla de ciclos para una secuencia de instrucciones en algoritmo Tomasulo (emisión, ejecución, escritura, terminación) y mostrar el ROB en un ciclo concreto. El segundo problema analiza un pipeline de 5 etapas (IF, ID, EX, MEM, WB) con resolución de saltos en distintas etapas, da frecuencias de saltos condicionales (30%, 75% tomados) e incondicionales (9%), y define una BTB con políticas concretas (95% acierto, solo saltos tomados, predicción NT si no está, eliminación sin

## Lo que se sacó de él (17)
- [[antidependencia-war-entre-s-d-y-daddui-por-r1-en-misma-itera]]
- [[calculo-de-cpi-base-en-pipeline-con-penalizacion-por-saltos]]
- [[calculo-de-cpi-con-btb-que-almacena-solo-saltos-tomados-y-pr]]
- [[calculo-de-speedup-con-ley-de-amdahl-ejemplo-tarjeta-grafica]]
- [[calculo-de-tiempo-de-ejecucion-con-cpi-frecuencia-e-instrucc]]
- [[definicion-de-dependencia-de-datos-verdadera-raw]]
- [[definicion-de-latencia-de-resolucion-de-salto-en-pipeline-5]]
- [[eliminacion-de-dependencias-de-nombre-mediante-renombramient]]
- [[estructura-de-btb-tabla-de-destinos-y-tabla-separada-de-bits]]
- [[excepcion-en-especulacion-hardware-atendida-solo-en-etapa-co]]
- [[frecuencias-de-saltos-en-el-examen-condicionales-30-75-tomad]]
- [[mejora-de-prestaciones-speedup-al-usar-btb-frente-a-sin-btb]]
- [[politica-de-btb-solo-entradas-para-saltos-tomados-prediccion]]
- [[predictor-correlacionado-2-1-bhr-tras-dos-saltos-tomados-des]]
- [[predictor-gselect-indice-mediante-xor-de-bits-de-pc-y-bhr]]
- [[riesgos-estructurales-en-tomasulo-en-fase-de-escritura-cdb]]
- [[secuencia-de-instrucciones-para-simulacion-tomasulo-con-div]]
