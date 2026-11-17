---
tipo: "fuente"
titulo: "Practica4 (Practicas)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Practica4.pdf`.

## Resumen
Esta práctica de Arquitectura de Computadores (Parte II) enseña a optimizar rendimiento mediante diseño cache-friendly (vector frente a lista), paralelismo a nivel de instrucción (desenrollado manual con 4 acumuladores para romper cadenas de dependencia) y programación sin saltos (branchless) para evitar fallos del predictor de ramas. Se usan hyperfine y perf con contadores hardware (cache-misses, IPC, ciclos) compilando a -O1 para desactivar optimizaciones automáticas y medir el efecto puro de las transformaciones de código.
Este trozo define las herramientas de análisis de rendimiento (lstopo, Hyperfine, Perf) con sus comandos de instalación y uso, detalla el cálculo del punto de inflexión y el mapeo de patrones de acceso en el modelo Roofline (rendimiento real en GFLOPs/s e intensidad aritmética en FLOPs/Byte a partir de contadores de caché), y describe la tarea de optimización estructural AoS→SoA con esquema de código, comparación de versiones y pregunta sobre aprovechamiento de línea de caché.

## Lo que se sacó de él (15)
- [[benchmarking-comparativo-con-hyperfine-warmup-y-comillas]]
- [[como-medir-impacto-de-cache-misses-e-ipc-con-hyperfine-y-per]]
- [[compilar-con-o1-para-desactivar-auto-unrolling-y-reordenacio]]
- [[desenrollado-manual-manual-unrolling-con-4-acumuladores-para]]
- [[instalacion-y-uso-rapido-de-lstopo-hwloc-para-topologia-de-m]]
- [[mapeo-de-patrones-de-acceso-en-grafico-roofline-gflops-s-y-f]]
- [[parametros-fijos-del-experimento-20-millones-de-lecturas-n-m]]
- [[perf-stat-con-contadores-clave-de-rendimiento-caches-ramas-t]]
- [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]]
- [[porcentaje-de-aprovechamiento-de-linea-de-cache-en-aos-acced]]
- [[predictor-de-saltos-por-que-datos-ordenados-vs-desordenados]]
- [[programacion-branchless-reemplazar-if-condicional-por-aritme]]
- [[punto-de-inflexion-knee-del-modelo-roofline-mononucleo]]
- [[tarea-3-2-aos-vs-soa-marcada-como-opcional-en-anexo-c]]
- [[transformacion-aos-a-soa-para-optimizacion-de-cache-esquema]]
