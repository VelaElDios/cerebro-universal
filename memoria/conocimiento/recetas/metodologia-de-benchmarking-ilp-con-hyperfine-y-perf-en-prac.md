---
tipo: "receta"
titulo: "Metodología de benchmarking ILP con hyperfine y perf en práctica AC"
temas: ["ac", "benchmarking", "hyperfine", "perf", "rendimiento"]
claves: ["hyperfine", "perf stat", "cycles", "instructions", "IPC", "-O1", "compilation flags"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[benchmarking]] · [[hyperfine]] · [[perf]] · [[rendimiento]]

Pasos estándar de la práctica para medir y comparar ILP:
1. Compilar ambas versiones con -O1 (evita auto-vectorización/unrolling del compilador):
   g++ -O1 -o ilp_base tarea_4_1_ilp.cpp
   g++ -O1 -o ilp_opt tarea_4_1_ilp_opt.cpp
2. Verificar corrección: ejecutar ambos y confirmar que `Suma A` coincide exactamente.
3. Medir tiempo de pared con hyperfine (múltiples runs, warmup, media/mediana):
   hyperfine --warmup 3 './ilp_base' './ilp_opt'
4. Medir contadores hardware con perf stat (ciclos, instrucciones, IPC):
   perf stat -e cycles,instructions ./ilp_base
   perf stat -e cycles,instructions ./ilp_opt
5. Calcular IPC = instructions / cycles. Comparar speedup = time_base / time_opt.
6. Justificar: reducción de stalls por RAW, mayor ocupación de ALUs, IPC más cercano al ancho de issue.

> Comparar ambas versiones con hyperfine y perf (cycles, instructions, IPC). Justificar los resultados.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp` (cita sin comprobar)

Relacionado: [[calculo-de-operaciones-por-ciclo-ipc-en-planificacion-vliw-d]] · [[definicion-de-peak-performance-rendimiento-pico]]
