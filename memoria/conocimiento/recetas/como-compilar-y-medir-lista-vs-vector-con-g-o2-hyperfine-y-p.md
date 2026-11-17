---
tipo: "receta"
titulo: "Cómo compilar y medir lista vs vector con g++ -O2, hyperfine y perf"
temas: ["ac", "benchmark", "hyperfine", "perf"]
claves: ["g++ -O2", "hyperfine", "perf stat", "cache-misses", "IPC", "instructions"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmark]] · [[hyperfine]] · [[perf]]

Pasos de compilación y medición:
1. Compilar ambas versiones con optimización:
   ```bash
   g++ -O2 -o lista tarea3_1_lista.cpp
   g++ -O2 -o vector tarea3_1_vector.cpp
   ```
2. Verificar corrección numérica:
   ```bash
   ./lista
   ./vector
   # Ambos deben imprimir la misma "suma de cuadrados = ..."
   ```
3. Medir tiempo con hyperfine (múltiples ejecuciones, warm-up automático):
   ```bash
   hyperfine ./lista ./vector
   ```
4. Medir contadores hardware con perf (cache-misses, instrucciones, ciclos, IPC):
   ```bash
   perf stat -e cache-misses,cache-references,instructions,cycles ./lista
   perf stat -e cache-misses,cache-references,instructions,cycles ./vector
   ```
5. Documentar y justificar hallazgos: reducción de cache misses, mejora de IPC, velocidad.

> g++ -O2 -o lista tarea3_1_lista.cpp g++ -O2 -o vector tarea3_1_vector.cpp
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea3_1_lista.cpp` (cita sin comprobar)

Relacionado: [[formula-del-techo-roofline-mononucleo]] · [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]]
