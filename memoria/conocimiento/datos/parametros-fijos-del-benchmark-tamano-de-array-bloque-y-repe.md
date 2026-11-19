---
tipo: "dato"
titulo: "Parámetros fijos del benchmark: tamaño de array, bloque y repeticiones"
temas: ["ac", "benchmark", "rendimiento"]
claves: ["N=2^26", "64M elementos", "512 MiB", "BLOQUE=4096", "REPETICIONES=4", "int64_t"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[benchmark]] · [[rendimiento]]

Valores constantes usados en el experimento:
- **N = 2²⁶ = 67.108.864 elementos** de tipo `int64_t` (8 bytes cada uno) → **512 MiB** totales.
- **BLOQUE = 4096 elementos** (32 KiB) → cabe holgadamente en caché L1 típica (32–64 KiB).
- **REPETICIONES = 4** pasadas completas sobre el array para el patrón secuencial y aleatorio.
- El patrón temporal calcula `vueltas = (N / BLOQUE) * REPETICIONES` para igualar el total de accesos.

> constexpr std::size_t N = 1ull << 26;        // 2^26= 64M elementos (de tipo int64)\n                                             // Un int64 ocupa 8 bytes --> total= 64M*8= 512 MB\n//Valor del bloque\nconstexpr std::size_t BLOQUE = 4096;         // bloque pequeño: cabe de sobra en L1\nconstexpr int REPETICIONES = 4;              // Número de pasadas completas sobre los datos.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp` (cita sin comprobar)

Relacionado: [[calculo-de-speedup-con-ley-de-amdahl-fraccion-mejorada-al-do]] · [[definicion-de-peak-performance-rendimiento-pico]]
