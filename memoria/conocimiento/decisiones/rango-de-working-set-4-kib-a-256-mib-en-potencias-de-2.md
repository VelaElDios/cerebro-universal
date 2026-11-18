---
tipo: "decision"
titulo: "Rango de working set: 4 KiB a 256 MiB en potencias de 2"
temas: ["ac", "benchmark", "diseno-experimento"]
claves: ["kMin", "kMax", "4 KiB", "256 MiB", "working set", "potencias de 2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmark]] · [[diseno-experimento]]

El working set varía desde 4 KiB (típico L1 data cache) hasta 256 MiB (supera L3 y llega a RAM principal) en potencias de 2 (bytes *= 2). Esto permite ver claramente los "escalones" de latencia al cruzar fronteras de caché: L1 (~4-32 KiB), L2 (~256 KiB-1 MiB), L3 (~4-32 MiB), y memoria principal (>32 MiB). El paso por potencias de 2 da puntos equidistantes en escala logarítmica para gráficas claras.

> constexpr std::size_t kMin = 4 * 1024;		// 4Kib
constexpr std::size_t kMax = 256ull * 1024 * 1024;	// 256 MiB
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp`

Relacionado: [[tecnica-pointer-chasing-para-medir-latencia-real-de-memoria]] · [[tamanos-de-cache-de-ejemplo-y-latencias-medidas-en-el-script]] · [[como-medir-latencia-de-memoria-con-pointer-chasing-y-taskset]] · [[working-set-size-vs-memory-access-latency-experiment]]
