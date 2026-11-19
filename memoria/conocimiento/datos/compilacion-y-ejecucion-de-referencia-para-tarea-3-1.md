---
tipo: "dato"
titulo: "Compilación y ejecución de referencia para Tarea 3.1"
temas: ["ac", "build", "g++"]
claves: ["g++", "-O2", "-o lista", "-o vector", "tarea3_1_lista.cpp", "tarea3_1_vector.cpp"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[build]] · [[g++]]

Comandos exactos del enunciado para compilar ambas versiones:
```bash
# Versión base (lista)
g++ -O2 -o lista tarea3_1_lista.cpp

# Versión optimizada (vector + fusión) - archivo creado por el alumno
g++ -O2 -o vector tarea3_1_vector.cpp
```
- `-O2`: nivel de optimización estándar para medir rendimiento (inlining, vectorización, desenrollado, etc.).
- Ejecutables nombrados `lista` y `vector` para distinguirlos en `hyperfine` y `perf`.
- No se usan flags de arquitectura específica (`-march=native`) ni sanitizers; el objetivo es comparar algoritmos/contendedores con la misma configuración base.

> g++ -O2 -o lista tarea3_1_lista.cpp
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea3_1_lista.cpp`

Relacionado: [[benchmarking-con-hyperfine-y-perf-para-comparar-versiones-li]]
