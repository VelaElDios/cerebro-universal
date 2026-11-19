---
tipo: "concepto"
titulo: "Prevención de Dead Code Elimination (DCE) forzando uso del resultado"
temas: ["ac", "compilador", "dce", "dead-code-elimination", "optimizacion"]
claves: ["DCE", "dead code elimination", "compiler optimization", "volatile", "side effect"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[compilador]] · [[dce]] · [[dead-code-elimination]] · [[optimizacion]]

El compilador con -O2 podría eliminar el bucle completo si detecta que `p` no se usa después. Para evitar esta optimización (Dead Code Elimination), se añade una comprobación artificial al final que "usa" el valor final de `p`: `if (p == static_cast<std::size_t>(-1)) std::puts("imposible");`. Como `p` nunca será -1 (es un índice válido), el `puts` nunca se ejecuta, pero el compilador no puede probarlo estáticamente y debe conservar el bucle. Alternativas comunes: `volatile`, `asm volatile("" : : "r,m"(p) : "memory")`, o escribir `p` en una variable global.

> Evita que el compilador eliminr de código muerto (DCE) (el bucle) forzando el uso de 'p'.\nif (p == static_cast<std::size_t>(-1)) std::puts(\"imposible\");
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea1_2_mem_latency.cpp` (cita sin comprobar)
