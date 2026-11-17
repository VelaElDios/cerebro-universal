---
tipo: "concepto"
titulo: "Parámetros del experimento: tamaño de datos, bloque y repeticiones"
temas: ["ac", "arquitectura", "cache", "memoria"]
claves: ["N", "1ull << 26", "BLOQUE", "4096", "REPETICIONES", "4", "512 MB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[cache]] · [[memoria]]

El experimento usa N = 2^26 elementos int64_t (512 MiB totales), muy superior a la caché L3 típica. BLOQUE = 4096 elementos (32 KiB) cabe en L1 data cache. REPETICIONES = 4 pasadas completas. Total de accesos = N * REPETICIONES = 268.435.456 lecturas por ejecución.

> constexpr std::size_t N = 1ull << 26;        // 2^26= 64M elementos (de tipo int64)\n                                             // Un int64 ocupa 8 bytes --> total= 64M*8= 512 MB\n//Valor del bloque\nconstexpr std::size_t BLOQUE = 4096;         // bloque pequeño: cabe de sobra en L1\nconstexpr int REPETICIONES = 4;              // Número de pasadas completas sobre los datos.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp` (cita sin comprobar)
