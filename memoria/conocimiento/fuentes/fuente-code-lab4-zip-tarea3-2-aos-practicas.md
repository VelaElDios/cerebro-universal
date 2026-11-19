---
tipo: "fuente"
titulo: "Code Lab4.zip!tarea3 2 aos (Practicas)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_2_aos.cpp`.

## Resumen
Este trozo es el código base (AoS) de una práctica de Arquitectura de Computadores que compara Array of Structures (AoS) frente a Structure of Arrays (SoA). El programa crea 60 millones de partículas de 16 bytes cada una (id, active, data, score) pero solo suma el campo `id` (4 bytes), desperdiciando el 75% del ancho de banda de caché. Incluye instrucciones para transformar a SoA, compilar con -O2, verificar checksums y medir con hyperfine/perf (cache-references, cache-misses, IPC).

## Lo que se sacó de él (6)
- [[aos-vs-soa-desperdicio-de-ancho-de-banda-en-cache-por-campos]]
- [[calculo-teorico-de-reduccion-de-lineas-de-cache-en-soa-frent]]
- [[cuando-preferir-aos-sobre-soa-en-la-practica]]
- [[medicion-de-rendimiento-con-hyperfine-y-perf-para-comparar-a]]
- [[parametros-del-benchmark-aos-soa-n-60m-iter-4-cache-line-64b]]
- [[transformacion-de-aos-a-soa-para-kernel-de-suma-de-ids]]
