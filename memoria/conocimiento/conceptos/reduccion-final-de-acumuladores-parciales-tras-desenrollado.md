---
tipo: "concepto"
titulo: "Reducción final de acumuladores parciales tras desenrollado"
temas: ["ac", "ilp", "loop unrolling", "reduction"]
claves: ["reduction", "partial sums", "accumulator reduction", "final sum"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[ac]] · [[ilp]] · [[loop unrolling]] · [[reduction]]

Tras el bucle desenrollado con k acumuladores independientes, se requiere una fase de reducción (reduction) para combinar los k valores parciales en el resultado final. En este caso k=4: `sumA = acc1 + acc2 + acc3 + acc4;`. Esta reducción añade 3 instrucciones ADD al final (coste despreciable frente a N iteraciones) y no introduce dependencias en el camino crítico del bucle. Es el patrón estándar de "parallel reduction" en bucles desenrollados para sumas, productos, min/max, etc.

> Al finalizar el bucle, sumar los 4 acumuladores en sumA. (e.g., sumA = acc1 + acc2 + acc3 + acc4;)
> — `repo:datos/temarios/AC/Practicas/Code_Lab4.zip!tarea4_1_ilp.cpp` (cita sin comprobar)

Relacionado: [[optimizacion-ilp-mediante-desenrollado-de-4-vias-con-acumula]]
