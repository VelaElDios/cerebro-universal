---
tipo: "dato"
titulo: "Parámetros fijos del experimento AoS/SoA (tarea 3.2)"
temas: ["ac", "benchmark", "parametros"]
claves: ["N=60000000", "ITER=4", "16-byte-struct", "64-byte-cache-line"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[benchmark]] · [[parametros]]

- **N** = 60 000 000 partículas (≈ 960 MB en AoS).
- **ITER** = 4 pasadas completas sobre el vector.
- Tamaño de `Particula` = 16 bytes → 4 partículas por línea de 64 B.
- En SoA, el vector `id` (int32) mete 16 IDs por línea de 64 B.
- Métricas esperadas: reducción ~4× en cache-references y cache-misses al leer solo `id`.

> constexpr std::size_t N = 60'000'000; constexpr int ITER = 4;
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp`

Relacionado: [[patron-secuencial-localidad-espacial-y-prefetcher-hardware]] · [[parametros-fijos-del-experimento-ilp-n-100m-tipo-double-valo]] · [[transformar-aos-a-soa-en-el-laboratorio-ac-tarea-3-2]] · [[parametros-del-experimento-tamano-de-datos-bloque-y-repetici]]
