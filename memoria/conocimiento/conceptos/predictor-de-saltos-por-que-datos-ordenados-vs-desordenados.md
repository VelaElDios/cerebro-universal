---
tipo: "concepto"
titulo: "Predictor de saltos: por qué datos ordenados vs desordenados cambian rendimiento drásticamente"
temas: ["ac", "branch-prediction", "pipeline"]
claves: ["branch predictor", "pipeline flush", "branch misprediction penalty", "sorted vs unsorted data", "if (data[i] >= 128)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Practica4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[branch-prediction]] · [[pipeline]]

CPU ejecuta especulativamente según predicción del branch predictor. Acierto → flujo continuo. Fallo → pipeline flush (penalidad 10-20 ciclos). Datos ordenados: patrón regular (muchos false, luego muchos true) → predictor aprende y acierta casi siempre. Datos desordenados: patrón aleatorio → predictor falla ~50% → penalidad masiva. Mismo código, mismos datos, distinto orden = rendimiento muy diferente.

> Sobre datos ordenados, la condición if (data[i] >= 128) da muchos false seguidos y luego muchos true seguidos: es fácil de predecir y casi siempre acierta. Sobre datos desordenados, el resultado es totalmente aleatorio; el predictor falla la mitad de las veces y el rendimiento se desploma.
> — `repo:datos/temarios/AC/Practicas/Practica4.pdf`

Relacionado: [[pointer-chasing-en-std-list-vs-acceso-contiguo-en-std-vector]] · [[calentamiento-warm-up-para-poblar-tlb-y-evitar-page-faults]] · [[por-que-el-orden-de-los-datos-afecta-al-codigo-con-salto-per]] · [[penalizacion-de-fallo-de-prediccion-de-salto-en-pipeline-sup]] · [[cuando-no-usar-branchless-trade-off-latencia-vs-previsibilid]]
