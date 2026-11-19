---
tipo: "decision"
titulo: "Atributos GCC para forzar salto real y desactivar optimizaciones vectoriales"
temas: ["ac", "pipeline", "rendimiento"]
claves: ["__attribute__", "optimize", "no-tree-vectorize", "no-if-conversion", "no-if-conversion2"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[pipeline]] · [[rendimiento]]

Para que el compilador no optimice el salto condicional convirtiéndolo en instrucciones SIMD (vectorización) o en movimiento condicional (cmov/if-conversion), se usan atributos de función en GCC:
- `no-tree-vectorize`: desactiva la vectorización automática de bucles
- `no-if-conversion`: desactiva la conversión de if a instrucciones condicionales (cmov)
- `no-if-conversion2`: desactiva una segunda pasada de if-conversion

Esto fuerza a que se genere una instrucción de salto real (`jcc`) que el predictor de saltos debe predecir, permitiendo medir su efecto.

> __attribute__((optimize(\"no-tree-vectorize\", \"no-if-conversion\", \"no-if-conversion2\")))
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_2_branchless.cpp`
