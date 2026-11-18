---
tipo: "receta"
titulo: "Cómo medir impacto de cache-misses e IPC con hyperfine y perf en experimentos controlados"
temas: ["ac", "benchmarking", "hyperfine", "perf"]
claves: ["hyperfine", "perf stat", "cache-misses", "IPC", "cycles", "instructions", "-O1", "tarea3_1_lista.cpp", "tarea3_1_vector.cpp"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmarking]] · [[hyperfine]] · [[perf]]

Metodología estándar de la práctica para cuantificar optimizaciones:
1. Compilar con `g++ -O1` (desactiva auto-unrolling y reordenación del compilador).
2. Medir tiempo de pared con `hyperfine ./ejecutable`.
3. Medir contadores hardware con `perf stat -e cycles,instructions,cache-references,cache-misses ./ejecutable`.
4. Calcular IPC = instructions / cycles.
5. Rellenar tabla comparativa: Wall-clock Time, Tiempo sistema, Instructions, Cycles, IPC, cache-references, cache-misses.
6. Justificar resultados vinculando cache-misses a localidad espacial y IPC a dependencias de datos o fallos de predictor.

> Compila y compara ambas versiones utilizando las herramientas hyperfine (para el tiempo de ejecución) y perf (analizando cache-misses, instrucciones e IPC).
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf`

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]] · [[patron-secuencial-localidad-espacial-y-prefetcher-hardware]] · [[benchmarking-ilp-con-hyperfine-y-perf-para-medir-cycles-inst]] · [[como-benchmarkear-y-perfilar-patrones-de-acceso-con-hyperfin]] · [[como-medir-contadores-hardware-con-perf-stat-para-comparar-p]]
