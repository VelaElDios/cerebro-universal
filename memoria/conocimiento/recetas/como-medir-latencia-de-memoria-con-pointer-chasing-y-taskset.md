---
tipo: "receta"
titulo: "Cómo medir latencia de memoria con pointer chasing y taskset (Tarea 1.2)"
temas: ["ac", "benchmarking", "cachés", "latencia", "taskset"]
claves: ["pointer chasing", "taskset", "working set", "latencia nsec", "tarea1_2_mem_latency.cpp"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmarking]] · [[cachés]] · [[latencia]] · [[taskset]]

Compilar `tarea1_2_mem_latency.cpp` (ver cabecera para flags). Ejecutar con `taskset -c 0 ./ejecutable` para anclar al core 0 y evitar migración. El programa barre tamaños de *working set* y mide latencia media de acceso aleatorio. Representar resultados con el script `tarea1_2_pintarLatvsMem(zoom).py` (actualizar tamaños de caché y latencias en la cabecera del script). Analizar saltos de latencia al desbordar L1→L2→L3→RAM relacionándolos con los tamaños obtenidos en Tarea 1.1.

> El programa realiza pointer chasing (lecturas aleatorias) sobre un tamaño de datos creciente para observar cómo aumenta la latencia a medida que se desbordan los distintos niveles de caché. Para fijar la ejecución del programa en un único núcleo usa el siguiente comando: taskset -c <core_number> <executable_file>
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf` (cita sin comprobar)

Relacionado: [[patron-aleatorio-peor-caso-con-permutacion-fija-de-indices-s]] · [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]] · [[tecnica-pointer-chasing-para-medir-latencia-real-de-memoria]] · [[como-compilar-y-ejecutar-el-benchmark-de-latencia-de-memoria]] · [[working-set-size-vs-memory-access-latency-experiment]]
