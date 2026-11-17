---
tipo: "concepto"
titulo: "AoS vs SoA: desperdicio de ancho de banda en caché"
temas: ["ac", "arquitectura-computadores", "optimizacion-memoria"]
claves: ["AoS", "SoA", "cache-line", "memory-bandwidth", "Particula", "64-byte"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[optimizacion-memoria]]

En Array of Structures (AoS), cada `Particula` ocupa 16 bytes (id:int4, active:uint8_t1+3padding, data:int4, score:float4). Una línea de caché de 64 B contiene 4 partículas, pero el kernel solo usa `id` (4 B/partícula). Por tanto, 12 B de cada 16 B (75 %) son tráfico inútil. Structure of Arrays (SoA) separa los campos en vectores contiguos (`vector<int> id`, `vector<uint8_t> active`, …), de modo que un bucle sobre `id` carga 16 enteros por línea de 64 B (100 % útil). La transformación elimina el padding y permite prefetching y vectorización más eficaces.

> El algoritmo SOLO suma el campo `id`, pero al recorrer el vector se cargan en la caché también `active`, `data` y `score`: el 75% de cada línea de caché transferida desde memoria es información inútil para este cálculo.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp` (cita sin comprobar)

Relacionado: [[patron-de-salto-de-latencia-en-fronteras-de-cache]] · [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]]
