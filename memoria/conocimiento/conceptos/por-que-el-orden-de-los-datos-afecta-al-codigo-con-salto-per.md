---
tipo: "concepto"
titulo: "Por qué el orden de los datos afecta al código con salto pero no al branchless"
temas: ["ac", "branch-prediction", "branchless", "pipeline"]
claves: ["sorted-vs-unsorted", "branch-predictor", "data-dependency"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[branch-prediction]] · [[branchless]] · [[pipeline]]

- **Con salto (`sumar_con_salto`)**: el predictor de ramas aprende patrones. Datos ordenados → larga racha de `false` seguida de larga racha de `true` → predictor acierta casi siempre → pipeline fluye. Datos desordenados → patrón aleatorio → ~50 % fallos → flushes constantes → 10-20 ciclos extra por fallo.
- **Sin salto (`sumar_sin_salto`)**: no hay instrucción de salto condicional dependiente de datos. El flujo de control es lineal; la ALU ejecuta `cmp`+`setge`+`imul`+`add` siempre. El tiempo depende solo de latencia/throughput de esas instrucciones, no de la historia de ramas previas.

> // - ¿Por qué sumar_con_salto tarda tan diferente con datos // ordenados vs. desordenados si el código es idéntico? // - ¿Por qué a sumar_sin_salto le es indiferente el orden?
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp`

Relacionado: [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]] · [[cuando-preferir-aos-sobre-soa-en-la-practica]] · [[predictor-de-saltos-por-que-datos-ordenados-vs-desordenados]] · [[cuando-no-usar-branchless-trade-off-latencia-vs-previsibilid]] · [[penalizacion-de-fallo-de-prediccion-de-salto-en-pipeline-sup]]
