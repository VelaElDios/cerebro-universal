---
tipo: "concepto"
titulo: "Tres patrones de acceso a memoria evaluados en la práctica (Tarea 2.1)"
temas: ["ac", "caché", "localidad", "patrones de acceso"]
claves: ["localidad temporal", "localidad espacial", "acceso aleatorio", "prefetching", "cache lines"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[caché]] · [[localidad]] · [[patrones de acceso]]

Definiciones canónicas usadas en la práctica:
- **Localidad temporal**: reuso de datos en ventana corta → datos en registros/L1.
- **Localidad espacial**: accesos contiguos → aprovecha líneas de caché (64 B típicas) y *hardware prefetcher*.
- **Acceso aleatorio**: patrón *pointer chasing* con índices permutados → anula prefetcher, causa *cache misses* en cascada (L1→L2→L3→RAM).
Estos tres patrones se implementan en `tarea2_1_patrones.cpp` y se compilan con `-O2`.

> En esta tarea, evaluaremos el impacto en el rendimiento de tres patrones de acceso: 1. Localidad Temporal: Reutilización de los mismos datos en cortos intervalos de tiempo, asegurando que permanezcan en los registros o en la caché L1. 2. Localidad Espacial: Acceso a direcciones de memoria contiguas. Esto aprovecha que la CPU transfiere líneas de caché completas desde la RAM, acelerando los accesos consecutivos. 3. Acceso Aleatorio: Saltos erráticos entre direcciones de memoria que invalidan cualquier intento de precarga automática (prefetching) por parte del hardware, forzando continuos fallos de caché.
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf`

Relacionado: [[patron-temporal-localidad-temporal-maxima-reutilizando-un-bl]] · [[patron-secuencial-localidad-espacial-y-prefetcher-hardware]] · [[patron-aleatorio-peor-caso-con-permutacion-fija-de-indices-s]]
