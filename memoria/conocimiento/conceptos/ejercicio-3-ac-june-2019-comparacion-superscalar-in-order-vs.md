---
tipo: "concepto"
titulo: "Ejercicio 3 AC June 2019: comparación superscalar in-order vs VLIW"
temas: ["ac", "pipeline", "superscalar", "vliw"]
claves: ["Exercise 3", "Processor A", "Processor B", "2-way superscalar", "VLIW", "in-order issue", "static scheduling", "register renaming"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]] · [[vliw]]

Enunciado completo del ejercicio:
Código (10 instrucciones):
  L.D   F1, 0(R1)
  L.D   F2, 0(R2)
  SUB.D F7, F1, F2
  MUL.D F3, F8, F4
  L.D   F4, 0(R10)
  ADD.D F1, F3, F5
  LSH   R12, R13, R14
  SUB.D F2, F2, F7
  ADD.D F4, F14, F6
  ADD.D F20, F10, F6

Procesador A: superscalar 2-vías, emisión in-order, ventana de emisión ilimitada, SIN renombrado de registros.
Procesador B: VLIW 2 operaciones/instrucción, planificación estática agresiva/eficiente, operaciones pueden reordenarse, CON renombrado de registros.

Suposiciones comunes:
- Carga (L.D): MEM = 2 ciclos
- Multiplicación (MUL.D): EX = 2 ciclos
- Resto operaciones: 1 ciclo
- Unidades funcionales totalmente segmentadas (pipelined)
- Forwarding soportado
- Delay branch con 1 delay slot

Se debe rellenar tabla de ciclos para cada procesador (hasta ciclo 12).

> Exercise 3 (2 points). Detail the execution of the following code in two different processors (A and B): Processor A is a 2-way superscalar processor with in-order issue and an issue window large enough for considering all the instructions. The processor does not support register renaming. Processor B is a VLIW processor able to issue two operations (of any type) per instruction. Static scheduling is as aggressive and efficient as possible to optimize the resulting code (operations can be scheduled out of order, and register renaming is supported).
> — `repo:datos/temarios/AC/examenes/June2019.pdf` (cita sin comprobar)

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[configuracion-de-procesador-tomasulo-con-especulacion-del-ej]]
