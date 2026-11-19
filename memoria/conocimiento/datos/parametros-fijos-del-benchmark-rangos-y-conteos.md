---
tipo: "dato"
titulo: "Parámetros fijos del benchmark: rangos y conteos"
temas: ["ac", "benchmark", "parametros", "working-set"]
claves: ["kMin", "kMax", "kAccesses", "4 KiB", "256 MiB", "50M"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[benchmark]] · [[parametros]] · [[working-set]]

Parámetros constantes del benchmark:
- `kMin = 4 * 1024` = 4 KiB (tamaño mínimo de working set, cabe en L1 típica)
- `kMax = 256ull * 1024 * 1024` = 256 MiB (tamaño máximo, excede L3 típica, fuerza acceso a RAM)
- Progresión: bucle `for (bytes = kMin; bytes <= kMax; bytes *= 2)` → 16 puntos: 4K, 8K, 16K, 32K, 64K, 128K, 256K, 512K, 1M, 2M, 4M, 8M, 16M, 32M, 64M, 128M, 256M KiB
- `kAccesses = 50'000'000` = 50 millones de accesos por punto de medición
- Tipo de elementos: `std::size_t` (8 bytes en x86-64), así que `n = bytes / sizeof(std::size_t)` elementos

> constexpr std::size_t kMin = 4 * 1024;\nconstexpr std::size_t kMax = 256ull * 1024 * 1024;\nconstexpr std::size_t kAccesses = 50'000'000;
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp` (cita sin comprobar)
