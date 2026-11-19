---
tipo: "receta"
titulo: "Construcción del array de pointer chasing con permutación cíclica aleatoria"
temas: ["ac", "benchmark", "permutacion", "pointer-chasing", "vector"]
claves: ["std::iota", "std::shuffle", "mt19937_64", "permutation", "cycle"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[benchmark]] · [[permutacion]] · [[pointer-chasing]] · [[vector]]

Algoritmo para crear un ciclo único que recorre todos los elementos exactamente una vez:
1. Crear vector `idx` con valores 0, 1, 2, ..., n-1 usando `std::iota`
2. Mezclar aleatoriamente desde el segundo elemento (`idx.begin() + 1`) con `std::shuffle` y generador `mt19937_64(42)` (semilla fija para reproducibilidad)
3. Construir `buf` donde `buf[idx[i]] = idx[i+1]` para i=0..n-2, y `buf[idx[n-1]] = idx[0]` para cerrar el ciclo
4. Resultado: `buf` es una permutación que forma un único ciclo de longitud n, ideal para pointer chasing

> std::iota(idx.begin(), idx.end(), 0);\nstd::shuffle(idx.begin() + 1, idx.end(), rng);\nfor (std::size_t i = 0; i + 1 < n; ++i) buf[idx[i]] = idx[i + 1];\nbuf[idx[n - 1]] = idx[0];
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp` (cita sin comprobar)
