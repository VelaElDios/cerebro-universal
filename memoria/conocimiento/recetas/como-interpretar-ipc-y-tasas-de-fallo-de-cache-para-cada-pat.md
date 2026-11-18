---
tipo: "receta"
titulo: "Cómo interpretar IPC y tasas de fallo de caché para cada patrón"
temas: ["ac", "análisis", "cache-miss-rate", "ipc", "perf"]
claves: ["IPC", "cache miss ratio", "L1-dcache-load-misses", "cycles", "instructions"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[análisis]] · [[cache-miss-rate]] · [[ipc]] · [[perf]]

Métricas clave a comparar entre los tres patrones: (1) IPC = instructions / cycles (mayor = mejor aprovechamiento pipeline). (2) L1 miss rate = L1-dcache-load-misses / L1-dcache-loads. (3) LLC miss rate = cache-misses / cache-references. (4) Tiempo real (hyperfine). Esperado: secuencial ≈ temporal en IPC alto y miss rate bajo; aleatorio con IPC bajo y miss rate alto.

> 5. Analysis:    Compare IPC, cache miss ratios, and execution runtimes.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp`

Relacionado: [[como-medir-contadores-hardware-con-perf-stat-para-comparar-p]] · [[como-medir-impacto-de-cache-misses-e-ipc-con-hyperfine-y-per]] · [[como-benchmarkear-y-perfilar-patrones-de-acceso-con-hyperfin]]
