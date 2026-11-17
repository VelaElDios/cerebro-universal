---
tipo: "decision"
titulo: "Cuándo NO usar branchless (trade-off: latencia vs. previsibilidad)"
temas: ["ac", "branchless", "optimizacion", "tradeoff"]
claves: ["branchless", "cmov", "predication", "always-better", "latency"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[branchless]] · [[optimizacion]] · [[tradeoff]]

**No siempre**. Consideraciones:
1. **Latencia extra**: `x * (x>=128)` ejecuta multiplicación y suma *incondicionalmente*. Si la condición es rara (p. ej. 1 % true), el `if` salta la suma el 99 % de las veces → menos uops.
2. **Dependencia de datos**: la multiplicación crea cadena de dependencias (suma → siguiente iteración) que puede limitar ILP; el `if` bien predicho permite especulación.
3. **Tamaño de código**: branchless puede aumentar presión en I-cache si se usa mucho.
4. **Compilador**: a `-O3` GCC/Clang ya convierten `if` simples en `cmov` o vectorizan; forzar branchless manual solo tiene sentido cuando el compilador *no* lo hace (patrones complejos, punteros, llamadas).
Regla práctica: perfilar ambos; usar branchless cuando la tasa de misprediction > ~5 % y el cuerpo del `if` es barato.

> - ¿Es siempre preferible una versión branchless en cualquier caso?
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp`

Relacionado: [[formula-del-techo-roofline-mononucleo]] · [[cuando-preferir-aos-sobre-soa-en-la-practica]]
