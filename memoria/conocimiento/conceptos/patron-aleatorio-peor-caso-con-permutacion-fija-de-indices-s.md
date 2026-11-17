---
tipo: "concepto"
titulo: "Patrón aleatorio: peor caso con permutación fija de índices (semilla 42)"
temas: ["ac", "acceso aleatorio", "cache miss", "memoria", "mt19937"]
claves: ["acceso_aleatorio", "orden", "shuffle", "mt19937", "42", "permutación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[acceso aleatorio]] · [[cache miss]] · [[memoria]] · [[mt19937]]

Genera `vector<uint32_t> orden(N)` con `iota` y `shuffle` usando `mt19937(42)` (semilla fija para reproducibilidad). Luego `for (r=0; r<REPETICIONES; ++r) for (i=0; i<N; ++i) s += v[orden[i]]`. Salta aleatoriamente por 512 MiB → cada acceso probablemente falla en L1, L2 y L3, forzando acceso a RAM. Mide latencia máxima de memoria.

> // ============================================================================\n// PATRÓN 3: ACCESO ALEATORIO (El peor escenario posible)\n// Lee los 512 MiB saltando a posiciones desordenadas mediante un vector de índices.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp` (cita sin comprobar)
