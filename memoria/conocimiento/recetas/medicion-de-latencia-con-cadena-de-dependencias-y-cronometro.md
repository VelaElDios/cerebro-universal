---
tipo: "receta"
titulo: "Medición de latencia con cadena de dependencias y cronómetro high-resolution"
temas: ["ac", "benchmark", "chrono", "nanoseconds", "steady_clock"]
claves: ["steady_clock", "duration", "nano", "kAccesses", "data dependency"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[benchmark]] · [[chrono]] · [[nanoseconds]] · [[steady_clock]]

Metodología de medición precisa:
1. Usar `std::chrono::steady_clock` (monotónico, no afectado por ajustes de reloj del sistema)
2. Capturar tiempo antes (`t0`) y después (`t1`) del bucle de accesos
3. Bucle con dependencia estricta: `p = buf[p]` - el procesador no puede calcular la siguiente dirección hasta completar la carga actual
4. 50 millones de iteraciones (`kAccesses = 50'000'000`) para amortizar overhead del bucle y obtener medida estable
5. Calcular latencia media: `(t1 - t0) en nanosegundos / kAccesses`
6. Imprimir resultado en ns con 2 decimales

> auto t0 = std::chrono::steady_clock::now();\nfor (std::size_t i = 0; i < kAccesses; ++i) p = buf[p];\nauto t1 = std::chrono::steady_clock::now();\ndouble ns = std::chrono::duration<double, std::nano>(t1 - t0).count() / kAccesses;
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp` (cita sin comprobar)
