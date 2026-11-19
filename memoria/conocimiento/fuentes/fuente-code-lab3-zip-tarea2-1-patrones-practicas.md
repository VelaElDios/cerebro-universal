---
tipo: "fuente"
titulo: "Code Lab3.zip!tarea2 1 patrones (Practicas)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp`.

## Resumen
Este trozo implementa un programa en C++ para analizar tres patrones de acceso a memoria (secuencial, temporal y aleatorio) sobre un array de 512 MiB (2²⁶ enteros de 64 bits). El objetivo es medir con `perf` el impacto de la localidad de datos en contadores hardware como ciclos, instrucciones, fallos de caché L1 y referencias de caché. Cada patrón realiza exactamente el mismo número total de accesos (N × REPETICIONES = 268 M lecturas), pero con distinta localidad espacial y temporal. El acceso aleatorio usa una permutación fija (semilla 42) para reproducibilidad.

## Lo que se sacó de él (6)
- [[como-compilar-y-ejecutar-el-benchmark-de-patrones-de-acceso]]
- [[generacion-de-permutacion-aleatoria-reproducible-para-acceso]]
- [[metricas-hardware-clave-para-comparar-patrones-de-acceso]]
- [[parametros-fijos-del-benchmark-tamano-de-array-bloque-y-repe]]
- [[tres-patrones-de-acceso-a-memoria-para-evaluar-localidad-de]]
- [[uso-de-int64-t-y-vector-inicializado-a-1-para-evitar-optimiz]]
