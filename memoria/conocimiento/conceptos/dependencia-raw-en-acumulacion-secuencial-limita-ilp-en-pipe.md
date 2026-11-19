---
tipo: "concepto"
titulo: "Dependencia RAW en acumulación secuencial limita ILP en pipeline"
temas: ["ac", "dependencias", "ilp", "pipeline"]
claves: ["RAW hazard", "data dependency", "pipeline stall", "accumulation", "sum reduction"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[dependencias]] · [[ilp]] · [[pipeline]]

En un pipeline in-order o superscalar, la instrucción `sumA += v[i]` crea una dependencia RAW (Read After Write) en `sumA`: la iteración i+1 no puede leer `sumA` hasta que la iteración i haya escrito el resultado. Esto serializa el bucle a 1 iteración por ciclo (o peor, según latencia de ADD), impidiendo que múltiples ALUs trabajen en paralelo. El desenrollado con 4 acumuladores elimina esta dependencia entre iteraciones adyacentes, permitiendo emitir 4 ADDs independientes por ciclo (sujeto a ancho de issue y puertos de ejecución).

> El bucle base acumula valores en una única variable (sumA += v[i]). Cada iteración depende estrictamente del resultado de la anterior, generando parones (stalls) y desaprovechando las múltiples ALUs de la CPU.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp` (cita sin comprobar)

Relacionado: [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[antidependencia-siempre-genera-hazard-war-en-pipeline-in-ord]]
