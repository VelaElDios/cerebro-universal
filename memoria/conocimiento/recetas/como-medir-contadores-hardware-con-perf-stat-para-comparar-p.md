---
tipo: "receta"
titulo: "Cómo medir contadores hardware con perf stat para comparar patrones de memoria"
temas: ["ac", "cache", "perf", "profiling"]
claves: ["perf stat", "cycles", "instructions", "cache-references", "cache-misses", "L1-dcache-loads", "L1-dcache-load-misses"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cache]] · [[perf]] · [[profiling]]

Ejecutar `perf stat` con los eventos: `cycles`, `instructions`, `cache-references`, `cache-misses`, `L1-dcache-loads`, `L1-dcache-load-misses`. Esto permite calcular IPC (instructions/cycles), tasas de fallo de caché (cache-misses/cache-references y L1-dcache-load-misses/L1-dcache-loads) y comparar el comportamiento de cada patrón de acceso.

> // perf stat -e cycles,instructions,cache-references,cache-misses,\ // L1-dcache-loads,L1-dcache-load-misses './patrones <secuencial | temporal | aleatorio>'
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp`

Relacionado: [[como-interpretar-ipc-y-tasas-de-fallo-de-cache-para-cada-pat]] · [[como-benchmarkear-y-perfilar-patrones-de-acceso-con-hyperfin]] · [[como-medir-impacto-de-cache-misses-e-ipc-con-hyperfine-y-per]]
