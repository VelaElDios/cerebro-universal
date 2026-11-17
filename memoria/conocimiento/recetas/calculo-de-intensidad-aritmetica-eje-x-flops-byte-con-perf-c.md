---
tipo: "receta"
titulo: "Cálculo de intensidad aritmética (eje X: FLOPs/Byte) con perf cache-misses"
temas: ["ac", "cache-misses", "intensidad aritmética", "perf", "roofline"]
claves: ["IA", "FLOPs/Byte", "cache-misses", "64 Bytes", "Bytes desde RAM", "perf stat"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cache-misses]] · [[intensidad aritmética]] · [[perf]] · [[roofline]]

Intensidad aritmética (eje X) = Total_FLOPs / Bytes_desde_RAM
Donde Bytes_desde_RAM se aproxima con contadores hardware:
  Bytes_desde_RAM = cache-misses (perf stat -e cache-misses) * 64
Porque cada miss de último nivel (LLC) trae una cache line de 64 B.
Pasos:
1. Ejecutar con `perf stat -e cache-misses ./programa` y anotar cache-misses.
2. Multiplicar por 64 → Bytes desde RAM.
3. Dividir Total_FLOPs (receta anterior) entre esos Bytes.
Esto sitúa cada patrón (Temporal, Secuencial, Aleatorio) en el eje X.

> Sabiendo que cada fallo de caché de último nivel reportado por perf (cache-misses) obliga a la CPU a traer una línea de datos completa de 64 Bytes desde la RAM, calculamos el tráfico como: Bytes desde RAM = cache-misses (perf) * 64 Bytes.
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf`

Relacionado: [[patron-aleatorio-peor-caso-con-permutacion-fija-de-indices-s]] · [[patron-secuencial-localidad-espacial-y-prefetcher-hardware]] · [[patron-temporal-localidad-temporal-maxima-reutilizando-un-bl]]
