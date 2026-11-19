---
tipo: "concepto"
titulo: "Métricas hardware clave para comparar patrones de acceso"
temas: ["ac", "cache", "perf", "rendimiento"]
claves: ["IPC", "cycles", "instructions", "cache-references", "cache-misses", "L1-dcache-loads", "L1-dcache-load-misses"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[cache]] · [[perf]] · [[rendimiento]]

El script de `perf stat` recoge seis contadores para calcular:
- **IPC** = `instructions / cycles` → throughput real del núcleo.
- **Tasa de fallos de caché global** = `cache-misses / cache-references`.
- **Tasa de fallos L1 data** = `L1-dcache-load-misses / L1-dcache-loads`.
- **Tiempos de ejecución** (wall-clock) con `hyperfine`.
Se espera: secuencial ≈ temporal (alto IPC, bajas tasas de fallo) ≫ aleatorio (bajo IPC, altas tasas de fallo).

> perf stat -e cycles,instructions,cache-references,cache-misses,\n      L1-dcache-loads,L1-dcache-load-misses './patrones <secuencial | temporal | aleatorio>'\n   5. Análisis:      Comparar IPC, tasa de fallos de caché y tiempos de ejecución.
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp` (cita sin comprobar)

Relacionado: [[calculo-de-operaciones-por-ciclo-ipc-en-planificacion-vliw-d]] · [[ecuacion-fundamental-del-tiempo-de-ejecucion-en-arquitectura]]
