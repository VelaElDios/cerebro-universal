---
tipo: "fuente"
titulo: "Code Lab3.zip!tarea1 2 mem latency (Practicas)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp`.

## Resumen
Este trozo implementa un benchmark de latencia de memoria usando la técnica de "pointer chasing" (persecución de punteros). Mide la latencia media de acceso para tamaños de working set desde 4 KiB hasta 256 MiB (potencias de 2), realizando 50 millones de accesos dependientes por medición. El código incluye calentamiento (warm-up) para poblar la TLB, una cadena de dependencias de datos estricta que impide ejecución fuera de orden y prefetching, y evita la eliminación de código muerto por el compilador.

## Lo que se sacó de él (8)
- [[como-compilar-y-ejecutar-el-benchmark-de-latencia-de-memoria]]
- [[construccion-del-array-de-pointer-chasing-con-permutacion-ci]]
- [[fase-de-warm-up-para-poblar-tlb-y-evitar-page-faults-durante]]
- [[medicion-de-latencia-con-cadena-de-dependencias-y-cronometro]]
- [[parametros-fijos-del-benchmark-rangos-y-conteos]]
- [[prevencion-de-dead-code-elimination-dce-forzando-uso-del-res]]
- [[tecnica-pointer-chasing-para-medir-latencia-real-de-memoria]]
- [[uso-de-taskset-c-0-para-fijar-afinidad-de-cpu-y-reducir-vari]]
