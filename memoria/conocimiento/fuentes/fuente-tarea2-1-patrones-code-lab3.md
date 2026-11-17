---
tipo: "fuente"
titulo: "tarea2 1 patrones (Code_Lab3)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp`.

## Resumen
Este trozo implementa un programa en C++ para analizar tres patrones de acceso a memoria (secuencial, temporal y aleatorio) sobre un vector de 512 MiB (2^26 enteros de 64 bits). Incluye instrucciones de compilación, ejecución, profiling con `perf stat` (ciclos, instrucciones, referencias y fallos de caché L1) y benchmarking con `hyperfine`. El código está diseñado para medir el impacto de la localidad de datos en contadores hardware.

## Lo que se sacó de él (10)
- [[como-compilar-y-ejecutar-el-benchmark-de-patrones-de-acceso]]
- [[como-hacer-benchmark-estadistico-con-hyperfine-entre-patrone]]
- [[como-interpretar-ipc-y-tasas-de-fallo-de-cache-para-cada-pat]]
- [[como-medir-contadores-hardware-con-perf-stat-para-comparar-p]]
- [[parametros-del-experimento-tamano-de-datos-bloque-y-repetici]]
- [[patron-aleatorio-peor-caso-con-permutacion-fija-de-indices-s]]
- [[patron-secuencial-localidad-espacial-y-prefetcher-hardware]]
- [[patron-temporal-localidad-temporal-maxima-reutilizando-un-bl]]
- [[tamano-del-vector-y-bloque-en-bytes-y-lineas-de-cache]]
- [[uso-de-semilla-fija-42-en-mt19937-para-reproducibilidad-del]]
