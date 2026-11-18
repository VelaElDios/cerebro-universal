---
tipo: "decision"
titulo: "Por qué fusionar bucles de normalización y suma de cuadrados en una sola pasada"
temas: ["ac", "bucles", "optimizacion", "temporal-locality"]
claves: ["loop fusion", "temporal locality", "L1 cache", "two-pass vs single-pass"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[optimizacion]] · [[temporal-locality]]

Decisión de diseño: fusionar los dos bucles (normalizar + sumar cuadrados) en uno solo.
- **Problema del original**: primer bucle toca todos los elementos (llena L1/L2), pero al terminar, la caché está llena de los últimos elementos. El segundo bucle vuelve a leer desde el principio → los primeros elementos ya fueron expulsados (capacidad finita de L1 ≈ 32-48 KB, L2 ≈ 256-512 KB). Con 20M floats (80 MB), solo una fracción cabe en caché.
- **Solución**: un solo bucle que lee, normaliza y acumula inmediatamente. El dato normalizado se consume mientras está en registros/L1 → cero relecturas de memoria principal.
- **Trade-off**: ligera pérdida de claridad (mezcla dos operaciones), pero ganancia masiva en ancho de banda de memoria y latencia. En kernels memory-bound, la fusión de bucles es una optimización estándar.

> // - Recorrer los datos en dos bucles rompe la localidad temporal: al iniciar // la segunda pasada, los primeros elementos ya han sido expulsados de la caché.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp`

Relacionado: [[como-fusionar-dos-bucles-en-uno-solo-para-aprovechar-localid]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]] · [[como-transformar-std-list-a-std-vector-con-reserva-previa-pa]] · [[patron-temporal-localidad-temporal-maxima-reutilizando-un-bl]]
