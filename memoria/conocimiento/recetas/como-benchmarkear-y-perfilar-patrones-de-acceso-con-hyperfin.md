---
tipo: "receta"
titulo: "Cómo benchmarkear y perfilar patrones de acceso con hyperfine y perf stat (Tarea 2.1.a)"
temas: ["ac", "benchmarking", "hyperfine", "perf", "profiling"]
claves: ["hyperfine", "perf stat", "cache-references", "cache-misses", "L1-dcache-load-misses", "branches", "branch-misses"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmarking]] · [[hyperfine]] · [[perf]] · [[profiling]]

1) Compilar: `g++ -O2 tarea2_1_patrones.cpp -o tarea2_1_patrones`. 2) Ejecutar cada patrón (el programa acepta argumentos para seleccionar patrón). 3) Medir tiempo con `hyperfine --warmup 3 './tarea2_1_patrones <patrón>'`. 4) Medir contadores hardware con `perf stat -e "cycles,instructions,cache-references,cache-misses,L1-dcache-loads,L1-dcache-load-misses,branches,branch-misses" ./tarea2_1_patrones <patrón>`. 5) Rellenar tabla: Patrón | Tiempo (hyperfine) | Fallos Caché (perf). 6) Calcular *speedup* secuencial vs aleatorio. 7) Identificar patrón con mayor latencia y fallos (aleatorio) y explicar por qué (invalida prefetcher, *cache misses* en todos los niveles).

> Obtén el tiempo medio de ejecución y los fallos a caché de cada patrón de acceso para ello ejecuta hyperfine y perf stat.
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf`

Relacionado: [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]] · [[como-hacer-benchmark-estadistico-con-hyperfine-entre-patrone]] · [[como-medir-contadores-hardware-con-perf-stat-para-comparar-p]] · [[como-medir-impacto-de-cache-misses-e-ipc-con-hyperfine-y-per]]
