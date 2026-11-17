---
tipo: "concepto"
titulo: "Penalización de fallo de predicción de salto en pipeline superscalar"
temas: ["ac", "branch-prediction", "microarquitectura", "pipeline"]
claves: ["misprediction", "pipeline-flush", "10-20 ciclos", "branch-predictor"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[branch-prediction]] · [[microarquitectura]] · [[pipeline]]

Cuando el predictor de ramas falla (misprediction), el pipeline debe:
1. Detectar el error (etapa de ejecución/retiro).
2. Vaciar (flush) todas las instrucciones especulativas ya emitidas.
3. Recuperar el PC correcto y reiniciar la fetch.
Coste típico en núcleos modernos (Skylake, Zen 3, Golden Cove): **10–20 ciclos** de burbuja.
En el experimento, datos desordenados (~50 % de `x >= 128` aleatorio) causan ~50 % de fallos → lentitud drástica frente a datos ordenados (predictor acierta casi siempre tras la transición).

> Con datos desordenados, las bifurcaciones impredecibles provocan fallos de predicción que obligan a vaciar el pipeline (penalización de 10-20 ciclos).
> — `repo:datos/temarios/AC/Practicas/Code_Lab4/tarea4_2_branchless.cpp` (cita sin comprobar)

Relacionado: [[interpretacion-de-regiones-memory-bound-vs-compute-bound-en]] · [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]]
