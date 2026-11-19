---
tipo: "concepto"
titulo: "Cálculo teórico de reducción de líneas de caché en SoA frente a AoS"
temas: ["ac", "analisis-rendimiento", "cache", "memoria"]
claves: ["cache line", "64 bytes", "16 bytes", "4 bytes", "reduction factor"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[analisis-rendimiento]] · [[cache]] · [[memoria]]

Modelo teórico para el kernel "suma de id":
- AoS: cada partícula 16 B → 4 part/linea. Para N partículas se tocan N/4 líneas de caché. Como hay ITER pasadas, referencias totales ≈ ITER × N/4.
- SoA: vector `id` contiguo, 4 B/ID → 16 ID/linea. Se tocan N/16 líneas de caché por pasada. Referencias totales ≈ ITER × N/16.
- Factor de reducción = (N/4) / (N/16) = 4× menos líneas de caché referenciadas (75% menos).
- En la práctica, `perf stat cache-references` debería reflejar ~4× menos referencias en SoA, y `cache-misses` también caerá drásticamente si el working set supera la caché.

> alcanzando 16 IDs por línea de caché de 64 B
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp`
