---
tipo: "concepto"
titulo: "Cálculo de operaciones por ciclo (IPC) en planificación VLIW de bucle"
temas: ["ac", "ipc", "planificacion", "rendimiento", "vliw"]
claves: ["operations per cycle", "IPC", "throughput", "steady state", "iniciacion de iteraciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ipc]] · [[planificacion]] · [[rendimiento]] · [[vliw]]

La pregunta (b) pide el número de operaciones por ciclo (IPC) alcanzado en estado estacionario (steady state) y su justificación. En VLIW con planificación de bucle (software pipelining / loop unrolling implícito en la tabla), el IPC se calcula como:
IPC = (número de instrucciones útiles ejecutadas por iteración en estado estacionario) / (ciclos de reloj por iteración en estado estacionario = II, Initiation Interval).
El máximo teórico es 6 ops/ciclo (6 unidades), pero las dependencias y latencias (cargas 3 ciclos, FP 4 ciclos) y el único slot de retardo del salto limitan el II mínimo. La justificación debe mostrar el diagrama de precedencias, el II mínimo conseguido, y contar cuántas de las 12 instrucciones se emiten cada II ciclos en la planificación óptima (incluyendo la instrucción en el delay slot del BNEZ).

> b) How many operations per cycle are reached? Justify the solution.
> — `repo:datos/temarios/AC/examenes/January2017.pdf`

Relacionado: [[codigo-del-bucle-a-planificar-en-vliw-examen-ac-enero-2017]]
