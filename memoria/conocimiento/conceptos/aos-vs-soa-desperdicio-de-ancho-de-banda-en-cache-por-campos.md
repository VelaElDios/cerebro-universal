---
tipo: "concepto"
titulo: "AoS vs SoA: desperdicio de ancho de banda en caché por campos no usados"
temas: ["ac", "aos-soa", "cache", "optimizacion-memoria"]
claves: ["Array of Structures", "Structure of Arrays", "cache line", "memory bandwidth", "Particula"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[aos-soa]] · [[cache]] · [[optimizacion-memoria]]

En Array of Structures (AoS), cada estructura Particula ocupa 16 bytes (id:4, active:1+3padding, data:4, score:4). Una línea de caché de 64 bytes contiene 4 partículas. Si el algoritmo solo accede a `id` (4 bytes), se cargan 16 bytes útiles por línea de 64 bytes → 25% de utilización, 75% de desperdicio. En Structure of Arrays (SoA), los `id` se almacenan contiguos en un vector `int id[]`; 64 bytes / 4 bytes = 16 IDs por línea de caché → 100% de utilización para este kernel.

> El algoritmo SOLO suma el campo `id`, pero al recorrer el vector se cargan en la caché también `active`, `data` y `score`: el 75% de cada línea de caché transferida desde memoria es información inútil para este cálculo.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp` (cita sin comprobar)
