---
tipo: "fuente"
titulo: "January2018 (examenes)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/examenes/January2018.pdf`.

## Resumen
Examen final de Arquitectura de Computadores (enero 2018) con 30 preguntas tipo test y dos ejercicios prácticos. El test cubre: ley de Amdahl, cálculo de MIPS, organización vs arquitectura, VLIW, dependencias (datos, salida, anti), técnicas ILP (desenrollado, predicción, especulación), bloques básicos, Scoreboard, Tomasulo (CDB, versión especulativa, bits veneno), predictores de salto (BHT, correlacionador 2,1), superscalar (commit, políticas de issue, estructuras), Intel P6 (ROB), multicore, CORTEX-A9, hilos, SIMD, cloud y GPGPU/SIMT. Los ejercicios piden: análisis de dependencias y pipelinin
Este trozo contiene el Ejercicio 3 de un examen de Arquitectura de Computadores (enero 2018). Pide planificar un bucle para un procesador VLIW de 4 operaciones por instrucción (sin restricciones de tipo por ALU), calcular operaciones por ciclo, desenrollar 3 veces el bucle y compactar el código VLIW, y finalmente calcular el speedup entre la versión original y la desenrollada. Se dan latencias: 2 ciclos MEM para carga/almacenamiento, 1 ciclo EX para ADD.D, 2 ciclos EX para MUL.D, y no hay salto retardado.

## Lo que se sacó de él (16)
- [[buffer-de-carga-en-tomasulo-especulativo]]
- [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]]
- [[calculo-de-mips-a-partir-de-frecuencia-cpi-por-tipo-y-mezcla]]
- [[calculo-de-speedup-entre-bucle-original-y-desenrollado-en-vl]]
- [[definicion-de-dependencia-de-salida-waw-entre-dos-instruccio]]
- [[dependencias-en-el-bucle-de-ejemplo-vliw-examen-ac-2018]]
- [[desenrollado-de-bucle-loop-unrolling-3-para-vliw-y-compactac]]
- [[implementacion-de-la-bht-en-predictor-dinamico-de-2-bits]]
- [[manejo-de-riesgos-estructurales-en-scoreboard]]
- [[metrica-operaciones-por-ciclo-opc-en-vliw]]
- [[numero-de-bhr-en-un-predictor-correlacionador-de-dos-niveles]]
- [[parametros-de-temporizacion-del-ejercicio-vliw-examen-enero]]
- [[planificacion-vliw-de-bucle-con-latencias-dadas-examen-ac-en]]
- [[proposito-del-desenrollado-de-bucles-loop-unrolling]]
- [[que-es-un-bloque-basico-basic-block-en-ilp]]
- [[recuperacion-ante-fallo-de-prediccion-de-salto-misprediction]]
