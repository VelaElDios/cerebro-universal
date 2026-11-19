---
tipo: "decision"
titulo: "Uso de taskset -c 0 para fijar afinidad de CPU y reducir variabilidad"
temas: ["ac", "benchmark", "cpu-affinity", "taskset", "variabilidad"]
claves: ["taskset", "CPU affinity", "core pinning", "noise reduction", "steady_clock"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[benchmark]] · [[cpu-affinity]] · [[taskset]] · [[variabilidad]]

Decisión de ejecutar con `taskset -c 0` para fijar el proceso al core lógico 0. Razones:
1. Evita migración del hilo entre cores por el scheduler del SO, que causaría variabilidad en latencias (diferentes distancias a caché, estado de caché diferente)
2. Aísla la medición de interferencia de otros procesos en otros cores
3. Complementa el uso de `steady_clock` (monotónico) para medición de tiempo
4. En sistemas con NUMA o caches compartidas por core, garantiza topología consistente
Es práctica estándar en microbenchmarks de latencia de memoria para obtener resultados reproducibles.

> Ejecutar: taskset -c 0 ./mem_latency
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp`
