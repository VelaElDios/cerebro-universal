---
tipo: "dato"
titulo: "Eventos de hardware disponibles en perf stat para análisis de caché y predicción de saltos (Anexo A)"
temas: ["ac", "contadores hardware", "perf", "pmu"]
claves: ["cycles", "instructions", "cache-references", "cache-misses", "L1-dcache-loads", "L1-dcache-load-misses", "branches", "branch-misses"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[contadores hardware]] · [[perf]] · [[pmu]]

Lista de eventos PMU recomendados en el enunciado para `perf stat`:
- `cycles`: ciclos de reloj consumidos.
- `instructions`: instrucciones completadas (permite IPC = instructions/cycles).
- `cache-references`: peticiones que llegaron a L3.
- `cache-misses`: fallos en L3 que fuerzan lectura en RAM.
- `L1-dcache-loads`: lecturas en L1 data.
- `L1-dcache-load-misses`: fallos en L1 data.
- `branches`: saltos evaluados.
- `branch-misses`: saltos mal predichos.
Además, `perf` reporta `time elapsed`, `user`, `sys`. Nota: el sistema distingue P-cores (`cpu_core`) y E-cores (`cpu_atom`).

> perf stat -e "cycles,instructions,cache-references,cache-misses,L1-dcache-loads,L1-dcache-load-misses,branches,branch-misses" Ejecutable_Practica
> — `repo:datos/temarios/AC/Practicas/Practica3.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]] · [[perf-stat-con-contadores-clave-de-rendimiento-caches-ramas-t]] · [[como-medir-contadores-hardware-con-perf-stat-para-comparar-p]] · [[como-medir-impacto-de-cache-misses-e-ipc-con-hyperfine-y-per]]
