---
tipo: "receta"
titulo: "Cómo compilar y ejecutar el benchmark de patrones de acceso a memoria"
temas: ["ac", "benchmarking", "cpp", "perf"]
claves: ["g++", "-O2", "patrones", "secuencial", "temporal", "aleatorio"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[benchmarking]] · [[cpp]] · [[perf]]

Compilar con optimización O2: `g++ -O2 -o patrones tarea2_1_patrones.cpp`. Ejecutar pasando uno de tres argumentos: `secuencial`, `temporal` o `aleatorio`. El programa reserva 512 MiB (vector de 2^26 int64_t inicializados a 1), recorre según el patrón elegido 4 veces (REPETICIONES) e imprime `patron=<nombre> resultado=<suma>`.

> g++ -O2 -o patrones tarea2_1_patrones.cpp // 2. Run: ./patrones <secuencial | temporal | aleatorio>
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea2_1_patrones.cpp`

Relacionado: [[como-compilar-y-ejecutar-el-benchmark-de-latencia-de-memoria]] · [[como-benchmarkear-y-perfilar-patrones-de-acceso-con-hyperfin]] · [[como-hacer-benchmark-estadistico-con-hyperfine-entre-patrone]]
