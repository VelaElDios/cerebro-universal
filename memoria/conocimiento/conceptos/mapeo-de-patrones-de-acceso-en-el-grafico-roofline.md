---
tipo: "concepto"
titulo: "Mapeo de patrones de acceso en el gráfico Roofline"
temas: ["ac", "aleatorio", "patrones acceso", "roofline", "secuencial", "temporal"]
claves: ["Temporal", "Secuencial", "Aleatorio", "hyperfine", "perf stat", "mapeo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[aleatorio]] · [[patrones acceso]] · [[roofline]] · [[secuencial]] · [[temporal]]

Cada patrón se representa como un punto (X, Y) en el Roofline:
- X (Intensidad Aritmética) = Total_FLOPs / (cache-misses * 64)  [perf stat]
- Y (Rendimiento Real)     = Total_FLOPs / (tiempo_hyperfine * 1e9) [hyperfine]

Esperado cualitativamente:
- Temporal: alta IA (reuso en L1) → punto a la derecha, cerca del techo compute.
- Secuencial: IA media (prefetcher ayuda) → punto intermedio.
- Aleatorio: baja IA (casi cada acceso miss) → punto a la izquierda, limitado por ancho de banda.

La comparación visual muestra si el kernel satura memoria o cómputo en cada caso.

> Para posicionar el patrón de acceso (Temporal, Secuencial o Aleatorio) en la gráfica, utilizaremos los tiempos obtenidos con hyperfine y los contadores de hardware medidos con perf stat.
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf`

Relacionado: [[patron-temporal-localidad-temporal-maxima-reutilizando-un-bl]] · [[patron-secuencial-localidad-espacial-y-prefetcher-hardware]] · [[patron-aleatorio-peor-caso-con-permutacion-fija-de-indices-s]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]] · [[mapeo-de-patrones-de-acceso-en-grafico-roofline-gflops-s-y-f]] · [[como-calcular-y-representar-puntos-de-patrones-en-el-grafico]] · [[tres-patrones-de-acceso-a-memoria-evaluados-en-la-practica-t]]
