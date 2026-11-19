---
tipo: "decision"
titulo: "Uso de int64_t y vector inicializado a 1 para evitar optimizaciones muertas"
temas: ["ac", "compilacion", "optimizacion"]
claves: ["int64_t", "vector<i64> v(N", "1)", "acumulación en variable s", "impresión de resultado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[compilacion]] · [[optimizacion]]

Decisiones de diseño para que el compilador no elimine el bucle:
- El array se inicializa con **valor 1** (`vector<i64> v(N, 1)`) en lugar de ceros, para que la suma no sea trivial.
- Cada patrón acumula en una variable local `i64 s` y la **devuelve**.
- `main` imprime el **resultado final** con `printf`, creando una dependencia de datos visible externamente que impide que `-O2` borre el bucle como código muerto.

> std::vector<i64> v(N, 1);\n    i64 resultado = 0;\n    // ...\n    std::printf(\"patron=%s resultado=%lld\\n\", argv[1],\n                static_cast<long long>(resultado));
> — `repo:datos/temarios/AC/Practicas/Code_Lab3.zip!tarea2_1_patrones.cpp` (cita sin comprobar)

Relacionado: [[alto-ilp-requiere-bajo-grado-de-dependencia-entre-instruccio]] · [[detenciones-en-pipeline-afectan-negativamente-a-prestaciones]]
