---
tipo: "fuente"
titulo: "tarea1 2 mem latency (Code_Lab3)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp`.

## Resumen
Este trozo implementa un benchmark de latencia de memoria usando la técnica de "pointer chasing" (persecución de punteros). Mide la latencia media de acceso variando el tamaño del working set desde 4 KiB hasta 256 MiB (potencias de 2), realizando 50 millones de accesos dependientes por medición para evitar ejecución fuera de orden (OoO) y prefetching. Incluye calentamiento (warm-up) para poblar la TLB y evitar page faults, y previene la eliminación de código muerto (DCE) forzando el uso del resultado final.

## Lo que se sacó de él (8)
- [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]]
- [[como-compilar-y-ejecutar-el-benchmark-de-latencia-de-memoria]]
- [[construccion-de-permutacion-aleatoria-en-ciclo-para-pointer]]
- [[medicion-de-latencia-con-50-millones-de-accesos-dependientes]]
- [[parametros-fijos-del-benchmark-semilla-accesos-formato-salid]]
- [[prevencion-de-eliminacion-de-codigo-muerto-dce-en-benchmark]]
- [[rango-de-working-set-4-kib-a-256-mib-en-potencias-de-2]]
- [[tecnica-pointer-chasing-para-medir-latencia-real-de-memoria]]
