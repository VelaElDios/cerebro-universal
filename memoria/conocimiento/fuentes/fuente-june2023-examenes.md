---
tipo: "fuente"
titulo: "June2023 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/June2023.pdf`.

## Resumen
Examen final de Arquitectura de Computadores (junio 2023) con 30 preguntas tipo test que cubren: rendimiento (peak performance, CPI, MIPS), dependencias y renombrado, pipeline MIPS64, planificación dinámica (Scoreboard, Tomasulo), superscalar vs VLIW, predicción de saltos, especulación con bits venenosos, arquitectura ARM (Neoverse, Big.Little, M2), computación en la nube/grid, MPI, multihilo y clasificación TOP500. Incluye cabecera de ejercicios prácticos (no mostrados).
Este trozo contiene tres ejercicios de un examen de Arquitectura de Computadores (junio 2023): 1) Predicción de saltos en un bucle con dos ramas (B1, B2) y un registro que alterna entre 0 y 1, evaluando predictores de un nivel (2 bits) y dos niveles (2,2) correlacionado; 2) Planificación dinámica con algoritmo Tomasulo para código MIPS64 con cargas, operaciones FP (ADD.D, MUL.D, DIV.D) y almacenamiento, con latencias dadas y restricciones de buffers/estaciones de reserva; 3) Procesador VLIW con 2 operaciones memoria, 2 FP y 1 entero/salto por ciclo, donde se da el código VLIW compactado y se p

## Lo que se sacó de él (18)
- [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
- [[calculo-de-cpi-medio-ponderado-por-mezcla-de-instrucciones]]
- [[calculo-de-speedup-vliw-vs-mips64-segmentado-considerando-me]]
- [[como-determinar-la-secuencia-real-de-saltos-y-resultados-en]]
- [[comparacion-de-rendimiento-entre-dos-maquinas-cpi-ciclo-de-r]]
- [[conversion-de-codigo-vliw-compactado-a-bucle-mips64-segmenta]]
- [[cpi-en-pipeline-con-penalizacion-por-saltos-tomados-y-delay]]
- [[definicion-de-peak-performance-rendimiento-pico]]
- [[el-renombrado-de-registros-evita-dependencias-de-nombre-war]]
- [[mips64-usa-caches-separadas-para-instrucciones-y-datos-harva]]
- [[planificacion-con-algoritmo-tomasulo-issue-execution-commit]]
- [[planificacion-dinamica-sin-especulacion-emision-en-orden-eje]]
- [[scoreboard-escribe-resultados-a-traves-del-banco-de-registro]]
- [[simulacion-de-predictor-correlacionado-de-dos-niveles-2-2-co]]
- [[simulacion-de-predictor-de-un-nivel-con-contadores-de-satura]]
- [[tipos-de-dependencias-en-codigo-fp-mips64-para-tomasulo-raw]]
- [[transformacion-por-software-pipelining-daddui-mantiene-signo]]
- [[unidades-funcionales-y-ciclos-en-vliw-con-2-mem-2-fp-1-int-b]]
