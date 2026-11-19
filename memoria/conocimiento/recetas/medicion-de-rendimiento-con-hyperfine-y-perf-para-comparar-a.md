---
tipo: "receta"
titulo: "Medición de rendimiento con hyperfine y perf para comparar AoS vs SoA"
temas: ["ac", "benchmark", "hyperfine", "linux", "perf"]
claves: ["hyperfine", "perf stat", "cache-references", "cache-misses", "instructions", "IPC"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[benchmark]] · [[hyperfine]] · [[linux]] · [[perf]]

Procedimiento de benchmarking sugerido en el enunciado:
1. `hyperfine ./aos ./soa` → tiempo de ejecución medio y desviación.
2. `perf stat -e cache-references,cache-misses,instructions,cycles ./aos` y lo mismo para `./soa`.
3. Métricas clave a comparar:
   - `cache-references` y `cache-misses`: SoA debe mostrar drásticamente menos referencias y fallos.
   - `instructions`: similar en ambos (mismo trabajo útil).
   - `IPC` (instructions per cycle = instructions/cycles): SoA suele subir por menor presión de memoria.
4. Calcular reducción de líneas de caché: (refs_AoS - refs_SoA) / refs_AoS ≈ 75% esperado.

> Comparar ambas versiones con hyperfine y perf (cache-references, cache-misses, instrucciones, IPC).
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp` (cita sin comprobar)
