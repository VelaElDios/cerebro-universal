---
tipo: "receta"
titulo: "Mapeo de patrones de acceso en gráfico Roofline (GFLOPs/s y FLOPs/Byte)"
temas: ["ac", "benchmarking", "hyperfine", "perf", "roofline"]
claves: ["intensidad aritmética", "GFLOPs/s", "FLOPs/Byte", "cache-misses", "64 Bytes", "hyperfine", "perf stat"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmarking]] · [[hyperfine]] · [[perf]] · [[roofline]]

Pasos para colocar un patrón (Temporal, Secuencial, Aleatorio) en el Roofline:
1. **Medir tiempo** con Hyperfine (usar `--warmup` y comillas). Tomar la media en segundos.
2. **Medir contadores** con `perf stat -e "cache-misses,..." ./ejecutable`. Anotar `cache-misses` (LLC misses).
3. **Calcular FLOPs totales**: en la práctica `Total_FLOPs = N * REPETICIONES * 4` (4 ops por elemento: suma).
4. **Eje Y (Rendimiento real, GFLOPs/s)**: `Y = Total_FLOPs / (tiempo_seg * 1e9)`.
5. **Eje X (Intensidad aritmética, FLOPs/Byte)**: `Bytes_RAM = cache_misses * 64`; `X = Total_FLOPs / Bytes_RAM`.
6. Representar (X, Y) en el gráfico con los techos teóricos.

> Para posicionar el patrón de acceso (Temporal, Secuencial o Aleatorio) en la gráfica, utilizaremos los tiempos obtenidos con hyperfine y los contadores de hardware medidos con perf stat. 1. Cálculo del Rendimiento Real (Y: GFLOPs/s) El rendimiento se obtiene dividiendo el número total de operaciones de punto flotante (FLOPs) ejecutadas por el algoritmo entre su tiempo de ejecución en segundos. Y = Total_FLOPs / (Tiempo ejecución en segundos (hyperfine) * 10^9) 2. Cálculo de la Intensidad Aritmética (X: FLOPs/Byte) La Intensidad Aritmética (IA) mide cuántas operaciones hace la CPU por cada Byte que viaja desde la memoria principal. X = IA = Total_FLOPs / Bytes desde RAM Sabiendo que cada fallo de caché de último nivel reportado por perf (cache-misses) obliga a la CPU a traer una línea de datos completa de 64 Bytes desde la RAM, calculamos el tráfico como: Bytes desde RAM = cache-misses (perf) * 64 Bytes.
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf` (cita sin comprobar)

Relacionado: [[punto-de-inflexion-knee-del-modelo-roofline-mononucleo]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]]
