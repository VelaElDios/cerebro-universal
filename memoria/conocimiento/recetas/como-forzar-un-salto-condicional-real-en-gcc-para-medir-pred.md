---
tipo: "receta"
titulo: "Cómo forzar un salto condicional real en GCC para medir predicción de ramas"
temas: ["ac", "compiladores", "optimizacion"]
claves: ["__attribute__", "optimize", "no-tree-vectorize", "no-if-conversion", "branch-prediction"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[compiladores]] · [[optimizacion]]

Para que el predictor de ramas sea evaluado sin que el compilador elimine el salto (vectorizando o convirtiendo a `cmov`), se anota la función con:
```cpp
__attribute__((optimize("no-tree-vectorize", "no-if-conversion", "no-if-conversion2")))
```
Esto desactiva:
- `no-tree-vectorize`: evita auto-vectorización (SIMD).
- `no-if-conversion` / `no-if-conversion2`: evita transformar `if` en instrucciones condicionales (`cmov`/`csel`).
Útil en microbenchmarks de predicción de saltos y penalización de pipeline.

> // Los atributos fuerzan a GCC a dejar un salto *real*: a -O2 lo convertiría en // SIMD (tree-vectorize) o en un cmov (if-conversion) y el predictor nunca se // pondría a prueba.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp`

Relacionado: [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[cuando-preferir-aos-sobre-soa-en-la-practica]] · [[cuando-no-usar-branchless-trade-off-latencia-vs-previsibilid]] · [[programacion-branchless-reemplazar-if-condicional-por-aritme]] · [[por-que-el-orden-de-los-datos-afecta-al-codigo-con-salto-per]]
