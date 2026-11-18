---
tipo: "concepto"
titulo: "Técnica pointer chasing para medir latencia real de memoria"
temas: ["ac", "arquitectura-computadores", "benchmark"]
claves: ["pointer chasing", "OoO", "prefetching", "latencia memoria", "working set"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[benchmark]]

El pointer chasing crea una cadena de dependencias de datos estricta: cada acceso a memoria devuelve la dirección del siguiente acceso. Esto impide que el procesador ejecute instrucciones fuera de orden (Out-of-Order execution) o haga prefetching, ya que la dirección del siguiente acceso no se conoce hasta completar el actual. Así se mide la latencia real de cada nivel de la jerarquía de memoria (L1, L2, L3, RAM) según el working set size.

> // Usa la técnica de "pointer chasing": cada acceso depende del anterior, // de modo que el procesador no puede solapar (OoO) ni precargar accesos // (prefetching), permitiendo medir la latencia real de la jerarquía de memoria.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp`

Relacionado: [[como-medir-latencia-de-memoria-con-pointer-chasing-y-taskset]] · [[construccion-de-permutacion-aleatoria-en-ciclo-para-pointer]] · [[medicion-de-latencia-con-50-millones-de-accesos-dependientes]]
