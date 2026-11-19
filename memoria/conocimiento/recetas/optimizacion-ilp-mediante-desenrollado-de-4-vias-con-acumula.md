---
tipo: "receta"
titulo: "Optimización ILP mediante desenrollado de 4 vías con acumuladores independientes"
temas: ["ac", "ilp", "optimizacion", "pipeline"]
claves: ["loop unrolling", "multiple accumulators", "dependency chain", "ILP", "-O1", "hyperfine", "perf"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[ilp]] · [[optimizacion]] · [[pipeline]]

Patrón canónico para romper cadena de dependencia de acumulación y exponer ILP:
1. Declarar 4 acumuladores independientes inicializados a 0.0f:
   double acc1 = 0.0f, acc2 = 0.0f, acc3 = 0.0f, acc4 = 0.0f;
2. Desenrollar bucle avanzando de 4 en 4 (i += 4) y asignar cada elemento a un acumulador distinto:
   for (int i = 0; i < N; i += 4) {
       acc1 += v[i];
       acc2 += v[i+1];
       acc3 += v[i+2];
       acc4 += v[i+3];
   }
3. Reducir al final: sumA = acc1 + acc2 + acc3 + acc4;
Requisitos: N múltiplo de 4. Compilar con -O1 para que el compilador no haga auto-unrolling y enmascare el efecto. Verificar que suma final coincide con versión secuencial. Medir con hyperfine y perf (cycles, instructions, IPC) para cuantificar speedup y justificar mejora en uso de ALUs y reducción de stalls por dependencia RAW.

> El bucle base acumula valores en una única variable (sumA += v[i]). Cada iteración depende estrictamente del resultado de la anterior, generando parones (stalls) y desaprovechando las múltiples ALUs de la CPU.
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp` (cita sin comprobar)

Relacionado: [[alto-ilp-requiere-bajo-grado-de-dependencia-entre-instruccio]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
