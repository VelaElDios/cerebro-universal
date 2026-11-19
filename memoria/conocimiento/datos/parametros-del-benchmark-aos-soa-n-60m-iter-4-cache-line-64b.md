---
tipo: "dato"
titulo: "Parámetros del benchmark AoS/SoA: N=60M, ITER=4, cache line=64B"
temas: ["ac", "benchmark", "cache", "rendimiento"]
claves: ["N", "ITER", "60000000", "64 bytes", "16 bytes", "4 particulas", "16 IDs"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[benchmark]] · [[cache]] · [[rendimiento]]

Constantes del experimento:
- N = 60,000,000 partículas (≈ 960 MB en AoS: 60M × 16 B).
- ITER = 4 pasadas completas sobre el array.
- Tamaño de partícula AoS = 16 bytes → 4 partículas por línea de caché de 64 B.
- Vector `id` en SoA: 4 bytes por ID → 16 IDs por línea de caché de 64 B.
- Teóricamente, SoA reduce referencias de caché a 1/4 para este kernel (solo se tocan las líneas que contienen IDs).

> constexpr std::size_t N = 60'000'000; constexpr int ITER = 4; // total: 16 bytes -> 4 partículas por línea de 64 B
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp` (cita sin comprobar)
