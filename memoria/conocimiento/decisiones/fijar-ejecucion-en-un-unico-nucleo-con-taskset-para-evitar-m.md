---
tipo: "decision"
titulo: "Fijar ejecución en un único núcleo con taskset para evitar migración y ruido (Tarea 1.2)"
temas: ["ac", "afinidad", "benchmarking", "metodología", "taskset"]
claves: ["taskset", "core_number", "migración", "ruido", "P-cores", "E-cores"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[afinidad]] · [[benchmarking]] · [[metodología]] · [[taskset]]

Decisión metodológica explícita en el enunciado: usar `taskset -c 0 ./ejecutable` (o el core deseado) para anclar el hilo a un core físico concreto. Esto evita:
- Migración entre cores (P-cores vs E-cores) que cambiaría frecuencias y tamaños de caché.
- Ruido por compartir caché con otros hilos.
- Variabilidad en mediciones de latencia y contadores `perf`.
Es práctica estándar en microbenchmarking de bajo nivel para obtener resultados reproducibles.

> Para fijar la ejecución del programa en un único núcleo usa el siguiente comando: taskset -c <core_number> <executable_file>
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf`

Relacionado: [[patron-aleatorio-peor-caso-con-permutacion-fija-de-indices-s]]
