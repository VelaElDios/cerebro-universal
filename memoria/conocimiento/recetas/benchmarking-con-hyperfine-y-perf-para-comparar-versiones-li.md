---
tipo: "receta"
titulo: "Benchmarking con hyperfine y perf para comparar versiones lista vs vector"
temas: ["ac", "benchmarking", "hyperfine", "perf", "rendimiento"]
claves: ["hyperfine", "perf stat", "cache-misses", "IPC", "cycles", "instructions", "warmup"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[benchmarking]] · [[hyperfine]] · [[perf]] · [[rendimiento]]

**Pasos de benchmarking recomendados en el enunciado:**

1. **Compilar con optimizaciones** (importante: `-O2` o `-O3`):
   ```bash
   g++ -O2 -o lista tarea3_1_lista.cpp
   g++ -O2 -o vector tarea3_1_vector.cpp
   ```

2. **Verificar corrección numérica** (salida idéntica):
   ```bash
   ./lista
   ./vector
   ```

3. **Medir tiempo de ejecución con hyperfine** (estadístico, con warmup):
   ```bash
   hyperfine --warmup 3 --runs 10 './lista' './vector'
   ```
   - `--warmup 3`: descarta 3 primeras ejecuciones (cachés frías, JIT, etc.).
   - `--runs 10`: hace 10 mediciones y reporta media, desviación, min/max.

4. **Contadores hardware con perf stat** (métricas de microarquitectura):
   ```bash
   perf stat -e cache-misses,cache-references,instructions,cycles,branches,branch-misses ./lista
   perf stat -e cache-misses,cache-references,instructions,cycles,branches,branch-misses ./vector
   ```
   Métricas clave a comparar:
   - `cache-misses` / `cache-references` → *miss rate* (debe caer drásticamente en vector).
   - `instructions` → cuenta instrucciones retiradas (vector + fusión reduce instrucciones de control de bucle).
   - `cycles` → ciclos totales (debe bajar).
   - `IPC = instructions / cycles` → debe subir (mejor aprovechamiento de pipeline).
   - `branch-misses` → predictor de saltos (bucle único vs dos bucles).

5. **Documentar y justificar**: explicar cada diferencia con conceptos de localidad espacial (vector contiguo), localidad temporal (fusión), *pointer chasing*, overhead de asignación.

> Comparar ambas versiones con hyperfine y perf (cache-misses, instrucciones, IPC) y documentar los resultados.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp` (cita sin comprobar)

Relacionado: [[optimizar-std-list-a-std-vector-con-reserva-y-fusion-de-bucl]]
