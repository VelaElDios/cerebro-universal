---
tipo: "receta"
titulo: "Medición de latencia con 50 millones de accesos dependientes"
temas: ["ac", "benchmark", "chrono", "medicion", "nanosegundos"]
claves: ["kAccesses", "50'000'000", "steady_clock", "duration", "nano", "latencia media"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmark]] · [[chrono]] · [[medicion]] · [[nanosegundos]]

Bucle de `kAccesses = 50'000'000` iteraciones: `p = buf[p]`. Cada iteración depende del resultado de la anterior (data dependency), serializando la ejecución. Tiempo medido con `std::chrono::steady_clock` (monotónico, no afectado por ajustes de reloj). Latencia media = (t1 - t0) en nanosegundos / kAccesses. 50M accesos dan suficiente tiempo total (>0.1s incluso en L1) para reducir ruido de medición y overhead del bucle.

> constexpr std::size_t kAccesses = 50'000'000; 	// 50 millones de accesos por medición
// Dependencia de datos estricta: bloquea la ejecución fuera de orden (OoO) y el prefetching.
//---- el procesador no puede calcular el paso i+1 hasta que no haya terminado de leer el paso i.
for (std::size_t i = 0; i < kAccesses; ++i) p = buf[p];
double ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / kAccesses;
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp` (cita sin comprobar)

Relacionado: [[tecnica-pointer-chasing-para-medir-latencia-real-de-memoria]] · [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]] · [[rango-de-working-set-4-kib-a-256-mib-en-potencias-de-2]] · [[como-medir-latencia-de-memoria-con-pointer-chasing-y-taskset]]
