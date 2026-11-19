---
tipo: "fuente"
titulo: "Code Lab4.zip!tarea3 1 lista (Practicas)"
temas: ["ac"]
claves: []
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]]

Documento aprendido: `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp`.

## Resumen
Este trozo es el código base ineficiente de la Tarea 3.1 de Arquitectura de Computadores: genera 20 millones de lecturas de sensor en un `std::list`, las normaliza en un primer bucle y calcula la suma de cuadrados en un segundo bucle. El enunciado pide optimizarlo sustituyendo la lista por `std::vector` con `reserve(N)` y fusionando ambos bucles en una sola pasada para mejorar la localidad de caché y evitar el "pointer chasing" y las asignaciones dinámicas por nodo.

## Lo que se sacó de él (8)
- [[benchmarking-con-hyperfine-y-perf-para-comparar-versiones-li]]
- [[compilacion-y-ejecucion-de-referencia-para-tarea-3-1]]
- [[fusion-de-bucles-loop-fusion-para-localidad-temporal]]
- [[optimizar-std-list-a-std-vector-con-reserva-y-fusion-de-bucl]]
- [[overhead-de-asignacion-por-nodo-en-std-list-vs-reserva-unica]]
- [[parametros-fijos-de-la-tarea-3-1-n-media-distribucion-semill]]
- [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]]
- [[usar-indice-size-t-en-bucle-fusionado-en-lugar-de-iteradores]]
