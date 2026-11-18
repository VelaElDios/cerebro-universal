---
tipo: "receta"
titulo: "Construcción de permutación aleatoria en ciclo para pointer chasing"
temas: ["ac", "algoritmo", "benchmark", "pointer-chasing"]
claves: ["std::iota", "std::shuffle", "permutación", "ciclo", "buf", "idx", "mt19937_64"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[algoritmo]] · [[benchmark]] · [[pointer-chasing]]

1. `idx` = vector con índices 0..n-1 (n = bytes/sizeof(size_t)). 2. `shuffle` aleatoriza idx[1..n-1] manteniendo idx[0] fijo (semilla 42 reproducible). 3. `buf` mapea cada índice al siguiente en el orden barajado: `buf[idx[i]] = idx[i+1]`. 4. El último apunta al primero: `buf[idx[n-1]] = idx[0]`. Resultado: un ciclo único que visita todos los elementos exactamente una vez en orden pseudoaleatorio, eliminando patrones de acceso predecibles que el prefetcher podría explotar.

> // Construimos una permutación aleatoria en forma de ciclo:
// buf[i] contiene el índice del SIGUIENTE elemento a visitar.
std::vector<std::size_t> idx(n);
std::iota(idx.begin(), idx.end(), 0);		// Rellena: 0, 1, 2, ..., n-1
std::shuffle(idx.begin() + 1, idx.end(), rng);  // Mezcla aleatoriamente
std::vector<std::size_t> buf(n);
for (std::size_t i = 0; i + 1 < n; ++i) buf[idx[i]] = idx[i + 1];
buf[idx[n - 1]] = idx[0];
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp`

Relacionado: [[tecnica-pointer-chasing-para-medir-latencia-real-de-memoria]] · [[patron-aleatorio-peor-caso-con-permutacion-fija-de-indices-s]] · [[como-medir-latencia-de-memoria-con-pointer-chasing-y-taskset]]
