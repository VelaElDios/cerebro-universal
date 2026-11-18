---
tipo: "concepto"
titulo: "Patrón secuencial: localidad espacial y prefetcher hardware"
temas: ["ac", "localidad", "memoria", "prefetcher"]
claves: ["acceso_secuencial", "localidad espacial", "prefetcher", "v[i"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[localidad]] · [[memoria]] · [[prefetcher]]

Recorre el vector linealmente `for (i=0; i<N; ++i) s += v[i]` repetido 4 veces. Aprovecha localidad espacial (líneas de caché de 64 bytes cargan 8 int64_t contiguos) y el prefetcher hardware detecta el patrón y trae líneas siguientes anticipadamente. Es el caso ideal de streaming.

> // ============================================================================\n// PATRÓN 1: ACCESO SECUENCIAL Suma las posiciones v[0] + v[1] + ... + v[67108863] cuatro veces.(Localidad Espacial + Prefetcher)\n// Lee el vector elemento tras elemento, de principio a fin, 4 veces.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp` (cita sin comprobar)

Relacionado: [[patron-temporal-localidad-temporal-maxima-reutilizando-un-bl]] · [[tres-patrones-de-acceso-a-memoria-evaluados-en-la-practica-t]] · [[tamano-del-vector-y-bloque-en-bytes-y-lineas-de-cache]]
