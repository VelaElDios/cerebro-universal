---
tipo: "dato"
titulo: "Parámetros fijos del experimento AoS/SoA (tarea 3.2)"
temas: ["ac", "benchmark", "parametros"]
claves: ["N=60000000", "ITER=4", "16-byte-struct", "64-byte-cache-line"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmark]] · [[parametros]]

- **N** = 60 000 000 partículas (≈ 960 MB en AoS).
- **ITER** = 4 pasadas completas sobre el vector.
- Tamaño de `Particula` = 16 bytes → 4 partículas por línea de 64 B.
- En SoA, el vector `id` (int32) mete 16 IDs por línea de 64 B.
- Métricas esperadas: reducción ~4× en cache-references y cache-misses al leer solo `id`.

> constexpr std::size_t N = 60'000'000;\nconstexpr int ITER = 4;
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp` (cita sin comprobar)

Relacionado: [[patron-secuencial-localidad-espacial-y-prefetcher-hardware]]
