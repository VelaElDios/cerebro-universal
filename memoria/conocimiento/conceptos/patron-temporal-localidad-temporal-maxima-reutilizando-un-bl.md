---
tipo: "concepto"
titulo: "Patrón temporal: localidad temporal máxima reutilizando un bloque que cabe en L1"
temas: ["ac", "l1", "localidad temporal", "memoria"]
claves: ["acceso_temporal", "BLOQUE", "vueltas", "L1", "localidad temporal"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[l1]] · [[localidad temporal]] · [[memoria]]

Calcula `vueltas = (N / BLOQUE) * REPETICIONES` y ejecuta `for (r=0; r<vueltas; ++r) for (i=0; i<BLOQUE; ++i) s += v[i]`. Total de accesos idéntico al secuencial (N*REPETICIONES), pero siempre sobre los mismos 4096 elementos (32 KiB). Tras la primera pasada, todo permanece en L1 → tasa de fallos L1 cercana a 0.

> // ============================================================================\n// PATRÓN 2: ACCESO TEMPORAL (Localidad Temporal Máxima)\n// Hace EXACTAMENTE el mismo número total de sumas que el acceso secuencial:\n// vueltas * BLOQUE = ((N / BLOQUE) * REPETICIONES) * BLOQUE = N * REPETICIONES.\n// Pero.... solo lee repetidamente los primeros BLOQUE elementos.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp` (cita sin comprobar)
