---
tipo: "concepto"
titulo: "Working set size vs memory access latency experiment"
temas: ["ac", "computer-architecture", "memory-hierarchy", "performance-analysis"]
claves: ["working set", "memory latency", "cache hierarchy", "microbenchmark"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[computer-architecture]] · [[memory-hierarchy]] · [[performance-analysis]]

Experimento clásico de arquitectura de computadores: se mide el tiempo de acceso a memoria (latencia) mientras se varía el tamaño del conjunto de trabajo (working set). Al recorrer un array de tamaño creciente, cuando el working set cabe en L1 la latencia es mínima; al superar L1 caen misses en L2 y sube la latencia; igual al superar L2 (L3) y L3 (RAM). La gráfica resultativa muestra escalones en las fronteras de capacidad de cada caché, permitiendo estimar tamaños reales de caché y penalizaciones de miss.

> Genera una gráfica de la latencia de acceso según el tamaño del working set.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_pintarLatvsMem.py`

Relacionado: [[patron-de-salto-de-latencia-en-fronteras-de-cache]] · [[como-graficar-latencia-vs-working-set-con-jerarquia-de-cache]] · [[tamanos-de-cache-de-ejemplo-y-latencias-medidas-en-el-script]]
