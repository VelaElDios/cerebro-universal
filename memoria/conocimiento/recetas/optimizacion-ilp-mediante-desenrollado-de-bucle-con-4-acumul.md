---
tipo: "receta"
titulo: "Optimización ILP mediante desenrollado de bucle con 4 acumuladores independientes"
temas: ["ac", "ilp", "loop-unrolling", "optimizacion"]
claves: ["ILP", "dependency chain", "accumulator", "unrolling", "-O1", "hyperfine", "perf"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ilp]] · [[loop-unrolling]] · [[optimizacion]]

**Problema**: Cadena de dependencia secuencial en acumulación (`sumA += v[i]`) que serializa la ejecución y subutiliza ALUs.

**Solución (4 pasos)**:
1. **Declarar 4 acumuladores independientes** inicializados a 0.0f:
   ```cpp
   double acc1 = 0.0f, acc2 = 0.0f, acc3 = 0.0f, acc4 = 0.0f;
   ```
2. **Desenrollar el bucle** avanzando de 4 en 4 (`i += 4`) y asignar cada elemento a un acumulador distinto:
   ```cpp
   for (int i = 0; i < N; i += 4) {
       acc1 += v[i];
       acc2 += v[i+1];
       acc3 += v[i+2];
       acc4 += v[i+3];
   }
   ```
3. **Sumar los 4 acumuladores** al final: `sumA = acc1 + acc2 + acc3 + acc4;`
4. **Compilar con -O1** (no -O2/-O3) para evitar auto-unrolling del compilador:
   ```bash
   g++ -O1 -o ilp_base tarea_4_1_ilp.cpp
   g++ -O1 -o ilp_opt tarea_4_1_ilp_opt.cpp
   ```

**Requisitos**: N debe ser múltiplo de 4 (el código usa 100'000'000). Ambas versiones deben producir resultado idéntico.

**Verificación**: Ejecutar ambos y comparar suma final. Benchmark con `hyperfine` y `perf stat -e cycles,instructions ./ilp_base ./ilp_opt` para medir IPC.

> El bucle base acumula valores en una única variable (sumA += v[i]). Cada iteración depende estrictamente del resultado de la anterior, generando parones (stalls) y desaprovechando las múltiples ALUs de la CPU.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_1_ilp.cpp` (cita sin comprobar)

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[formula-del-techo-roofline-mononucleo]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]]
