---
tipo: "decision"
titulo: "Compilar con -O2 y medir con perf/hyperfine en la práctica AC"
temas: ["ac", "benchmark", "compilacion", "hyperfine", "perf"]
claves: ["-O2", "g++", "hyperfine", "perf stat", "cache-references", "cache-misses", "IPC"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmark]] · [[compilacion]] · [[hyperfine]] · [[perf]]

Decisión pedagógica del enunciado:
- Usar `-O2` (no `-O3` ni `-march=native`) para que el compilador no oculte el efecto de layout con auto-vectorización agresiva.
- `hyperfine` para tiempo de pared (mediana de varias corridas, warm-up automático).
- `perf stat -e cache-references,cache-misses,instructions,cycles` para contadores HW; IPC = instructions/cycles.
- Comparar AoS vs SoA en la misma máquina sin turbo/ASLR (`perf stat -r 10 …`).

> Compile:        Build both executables with -O2 optimization:\n                      g++ -O2 -o aos tarea3_2_aos.cpp\n                      g++ -O2 -o soa tarea3_2_soa.cpp\n   7. Benchmarking:   Compare both versions using hyperfine and perf\n                      (cache-references, cache-misses, instructions, IPC).
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_2_aos.cpp` (cita sin comprobar)

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]] · [[como-compilar-y-medir-lista-vs-vector-con-g-o2-hyperfine-y-p]] · [[como-medir-impacto-de-cache-misses-e-ipc-con-hyperfine-y-per]] · [[benchmarking-ilp-con-hyperfine-y-perf-para-medir-cycles-inst]]
