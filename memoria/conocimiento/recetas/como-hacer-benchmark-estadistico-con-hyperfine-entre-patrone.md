---
tipo: "receta"
titulo: "Cómo hacer benchmark estadístico con hyperfine entre patrones temporal y aleatorio"
temas: ["ac", "benchmarking", "hyperfine"]
claves: ["hyperfine", "--warmup 3", "temporal", "aleatorio"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmarking]] · [[hyperfine]]

Usar `hyperfine --warmup 3 './patrones temporal' './patrones aleatorio'` para obtener tiempos de ejecución con significación estadística (warmup de 3 corridas, luego mediciones). Comparar medias, desviaciones y percentiles para cuantificar la penalización del acceso aleatorio frente al temporal.

> hyperfine --warmup 3 './patrones temporal' './patrones aleatorio'
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp`

Relacionado: [[como-benchmarkear-y-perfilar-patrones-de-acceso-con-hyperfin]] · [[benchmarking-comparativo-con-hyperfine-warmup-y-comillas]] · [[como-medir-impacto-de-cache-misses-e-ipc-con-hyperfine-y-per]]
