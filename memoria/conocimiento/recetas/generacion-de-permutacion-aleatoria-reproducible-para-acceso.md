---
tipo: "receta"
titulo: "Generación de permutación aleatoria reproducible para acceso aleatorio"
temas: ["ac", "aleatoriedad", "profiling"]
claves: ["std::iota", "std::shuffle", "std::mt19937", "semilla 42", "uint32_t", "permutación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[aleatoriedad]] · [[profiling]]

Para el patrón aleatorio se crea un vector `orden` de `uint32_t` con los índices 0…N‑1 y se baraja con `std::shuffle` usando un generador Mersenne Twister (`std::mt19937`) con **semilla fija 42**. Esto garantiza que cada ejecución del patrón aleatorio use **exactamente la misma secuencia de accesos**, permitiendo comparaciones justas entre runs y entre máquinas.

> // Genera una permutación aleatoria de índices [0, 1, 2, ..., N-1].\n        // Usa una semilla fija (42)\n        std::vector<std::uint32_t> orden(N);\n        std::iota(orden.begin(), orden.end(), 0u);\n        std::shuffle(orden.begin(), orden.end(), std::mt19937(42));
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp` (cita sin comprobar)

Relacionado: [[bits-de-veneno-poison-bits-en-carga-especulativa-marcan-regi]] · [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]]
