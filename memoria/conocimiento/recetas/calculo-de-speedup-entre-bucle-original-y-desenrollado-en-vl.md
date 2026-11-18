---
tipo: "receta"
titulo: "Cálculo de speedup entre bucle original y desenrollado en VLIW"
temas: ["ac", "loop-unrolling", "rendimiento", "speedup", "vliw"]
claves: ["speedup", "operaciones por ciclo", "ciclos por iteración", "overhead de salto", "ILP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop-unrolling]] · [[rendimiento]] · [[speedup]] · [[vliw]]

Speedup = (ciclos por iteración original) / (ciclos por iteración desenrollada). En A) se mide cuántos ciclos tarda una iteración del bucle original (incluyendo NOPs por latencias y salto). En C) se mide cuántos ciclos tarda el bucle desenrollado de 3 iteraciones y se divide entre 3. También puede calcularse como (ops/ciclo en C) / (ops/ciclo en A). El examen pide explícitamente comparar A) vs C).

> What is the speedup if we compare the code in A) with the code in C)?
> — `repo:datos/temarios/AC/examenes/January2018.pdf`

Relacionado: [[planificacion-vliw-de-bucle-con-latencias-dadas-examen-ac-en]] · [[desenrollado-de-bucle-loop-unrolling-3-para-vliw-y-compactac]]
