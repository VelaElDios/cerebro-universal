---
tipo: "concepto"
titulo: "Técnica pointer chasing para medir latencia real de memoria"
temas: ["ac", "arquitectura-computadores", "benchmark", "memoria", "rendimiento"]
claves: ["pointer chasing", "OoO", "prefetching", "latencia memoria", "working set"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp", "repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[benchmark]]

El pointer chasing crea una cadena de dependencias de datos estricta: cada acceso a memoria devuelve la dirección del siguiente acceso. Esto impide que el procesador ejecute instrucciones fuera de orden (Out-of-Order execution) o haga prefetching, ya que la dirección del siguiente acceso no se conoce hasta completar el actual. Así se mide la latencia real de cada nivel de la jerarquía de memoria (L1, L2, L3, RAM) según el working set size.

> // Usa la técnica de "pointer chasing": cada acceso depende del anterior, // de modo que el procesador no puede solapar (OoO) ni precargar accesos // (prefetching), permitiendo medir la latencia real de la jerarquía de memoria.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp`

Relacionado: [[como-medir-latencia-de-memoria-con-pointer-chasing-y-taskset]] · [[construccion-de-permutacion-aleatoria-en-ciclo-para-pointer]] · [[medicion-de-latencia-con-50-millones-de-accesos-dependientes]]

## Ampliación (2026-11-19, )
La técnica de pointer chasing crea una cadena de dependencias de datos donde cada acceso a memoria depende del resultado del anterior (p = buf[p]). Esto fuerza al procesador a esperar la latencia completa de cada acceso, serializando las accesos y midiendo la latencia real de la jerarquía de memoria (L1, L2, L3, RAM) sin que la ejecución fuera de orden (OoO) ni el prefetching oculten la latencia. El benchmark varía el tamaño del working set (4 KiB a 256 MiB) para observar cómo cambia la latencia según qué nivel de caché contiene los datos.
