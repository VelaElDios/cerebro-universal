---
tipo: "receta"
titulo: "Prevención de eliminación de código muerto (DCE) en benchmark"
temas: ["ac", "benchmark", "dce", "dead-code-elimination", "optimizador"]
claves: ["DCE", "dead code elimination", "p == -1", "puts", "impossible"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[benchmark]] · [[dce]] · [[dead-code-elimination]] · [[optimizador]]

El compilador (con -O2) detectaría que `p` no se usa tras el bucle y eliminaría todo el bucle de medición (Dead Code Elimination). La comprobación `if (p == -1) puts("imposible")` crea un uso lateral observable de `p` que el compilador no puede probar que nunca ocurre (aunque `p` es size_t sin signo y nunca será -1). Esto fuerza al optimizador a mantener el bucle vivo. Alternativas: `asm volatile("" : : "r,m"(p) : "memory")` o `benchmark::DoNotOptimize(p)` (Google Benchmark).

> // Evita que el compilador eliminr de código muerto (DCE) (el bucle) forzando el uso de 'p'.
if (p == static_cast<std::size_t>(-1)) std::puts("imposible");
> — `repo:datos/temarios/AC/Practicas/Code_Lab3/tarea1_2_mem_latency.cpp`

Relacionado: [[medicion-de-latencia-con-50-millones-de-accesos-dependientes]]
