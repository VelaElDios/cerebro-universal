---
tipo: "receta"
titulo: "Cómo compilar y ejecutar el benchmark de latencia de memoria"
temas: ["ac", "benchmark", "compilacion", "ejecucion"]
claves: ["g++", "-O2", "taskset", "mem_latency", "compilar", "ejecutar"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmark]] · [[compilacion]] · [[ejecucion]]

**Compilar:** `g++ -O2 -o mem_latency tarea1_2_mem_latency.cpp` (optimización O2 obligatoria para medir latencia real sin overhead de debug). **Ejecutar:** `taskset -c 0 ./mem_latency` fija el proceso al core 0 para evitar migración entre cores y variabilidad en cachés/TLB. **Salida:** imprime dos columnas: "Tamaño(KiB)" y "Latencia(ns)". **Graficar:** Tamaño del bloque (eje X) vs. Latencia media en nanosegundos (eje Y) para ver los escalones de la jerarquía de memoria.

> - Compilar: g++ -O2 -o mem_latency tarea1_2_mem_latency.cpp
- Ejecutar: taskset -c 0 ./mem_latency
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp` (cita sin comprobar)

Relacionado: [[tecnica-pointer-chasing-para-medir-latencia-real-de-memoria]] · [[como-medir-latencia-de-memoria-con-pointer-chasing-y-taskset]] · [[como-compilar-y-ejecutar-el-benchmark-de-patrones-de-acceso]]
