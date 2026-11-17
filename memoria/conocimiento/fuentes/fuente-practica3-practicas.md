---
tipo: "fuente"
titulo: "Practica3 (Practicas)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Practica3.pdf`.

## Resumen
Este trozo describe la Práctica 3 de Arquitectura de Computadores (curso 2026/27), centrada en la interacción software-hardware para optimizar el rendimiento. La Parte I (Lab3) cubre: caracterización de la topología hardware con `lstopo`, medición de latencia de memoria mediante *pointer chasing* y análisis de desbordes de caché, construcción del modelo Roofline del procesador usando `lscpu` y el benchmark STREAM, y evaluación de tres patrones de acceso a memoria (temporal, espacial, aleatorio) con `hyperfine` y `perf stat` para cuantificar tiempos, fallos de caché y posicionarlos en el gráfic
Este trozo define el punto de inflexión (ridge point) del modelo Roofline y detalla las fórmulas para mapear patrones de acceso (Temporal, Secuencial, Aleatorio) en la gráfica: cálculo de FLOPs totales, rendimiento real en GFLOPs/s (eje Y) e intensidad aritmética en FLOPs/Byte (eje X) usando cache-misses de perf y líneas de 64 Bytes.

## Lo que se sacó de él (13)
- [[calculo-de-flops-totales-para-el-kernel-de-la-tarea-2-1]]
- [[calculo-de-intensidad-aritmetica-eje-x-flops-byte-con-perf-c]]
- [[calculo-del-rendimiento-real-eje-y-gflops-s-con-hyperfine]]
- [[como-benchmarkear-y-perfilar-patrones-de-acceso-con-hyperfin]]
- [[como-calcular-y-representar-puntos-de-patrones-en-el-grafico]]
- [[como-caracterizar-la-topologia-hardware-con-lstopo-tarea-1-1]]
- [[como-generar-el-modelo-roofline-del-procesador-con-lscpu-y-s]]
- [[como-medir-latencia-de-memoria-con-pointer-chasing-y-taskset]]
- [[eventos-de-hardware-disponibles-en-perf-stat-para-analisis-d]]
- [[fijar-ejecucion-en-un-unico-nucleo-con-taskset-para-evitar-m]]
- [[mapeo-de-patrones-de-acceso-en-el-grafico-roofline]]
- [[punto-de-inflexion-ridge-point-en-el-modelo-roofline]]
- [[tres-patrones-de-acceso-a-memoria-evaluados-en-la-practica-t]]
