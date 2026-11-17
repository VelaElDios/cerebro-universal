---
tipo: "decision"
titulo: "Uso de semilla fija (42) en mt19937 para reproducibilidad del patrón aleatorio"
temas: ["ac", "benchmarking", "random", "reproducibilidad"]
claves: ["mt19937", "42", "semilla fija", "shuffle", "reproducibilidad"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmarking]] · [[random]] · [[reproducibilidad]]

Se fija la semilla a 42 en `std::mt19937(42)` para que la permutación aleatoria sea idéntica en cada ejecución. Esto garantiza que las mediciones de `perf` y `hyperfine` comparen exactamente el mismo patrón de accesos, eliminando variabilidad por generación de índices distinta.

> std::shuffle(orden.begin(), orden.end(), std::mt19937(42));
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp`
