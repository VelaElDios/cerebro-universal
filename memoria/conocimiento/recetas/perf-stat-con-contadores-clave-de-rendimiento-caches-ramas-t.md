---
tipo: "receta"
titulo: "Perf stat con contadores clave de rendimiento (cachés, ramas, tiempo)"
temas: ["ac", "perf", "pmu", "profiling"]
claves: ["perf stat", "cycles", "instructions", "cache-references", "cache-misses", "L1-dcache-loads", "L1-dcache-load-misses", "branches", "branch-misses", "time elapsed", "user", "sys"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[perf]] · [[pmu]] · [[profiling]]

Comando base: `perf stat -e "cycles,instructions,cache-references,cache-misses,L1-dcache-loads,L1-dcache-load-misses,branches,branch-misses" ./ejecutable`. Métricas clave:
- **cycles**: ciclos de reloj totales.
- **instructions**: instrucciones retiradas → IPC = instructions/cycles.
- **cache-references / cache-misses**: accesos y fallos en L3 (último nivel).
- **L1-dcache-loads / L1-dcache-load-misses**: accesos y fallos en L1 de datos.
- **branches / branch-misses**: predicción de saltos.
Tiempos reportados: `time elapsed` (wall-clock), `user` (CPU usuario), `sys` (CPU kernel). Nota: el sistema puede tener P-cores y E-cores (hybrid).

> perf stat -e \"cycles,instructions,cache-references,cache-misses,L1-dcache-loads,L1-dcache-load-misses,branches,branch-misses\" Ejecutable_Practica cycles: Ciclos de reloj consumidos por la CPU. instructions: Instrucciones máquina completadas. cache-references: Peticiones que llegaron a la caché L3. cache-misses: Fallos en la L3 que forzaron la lectura desde la RAM. L1-dcache-loads: Lecturas a la caché de datos más cercana al núcleo (L1d). L1-dcache-load-misses: Fallos en L1d branches: Saltos de control de flujo evaluados (bucles for, condiciones if). branch-misses: Saltos predichos incorrectamente. Tiempos finales time elapsed: Tiempo total transcurrido en el reloj real. user: Tiempo de CPU consumido por tu propio código. sys: Tiempo consumido por el kernel de Linux (asignación de páginas de RAM para los 512 MiB).
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]] · [[mapeo-de-patrones-de-acceso-en-el-grafico-roofline]]
