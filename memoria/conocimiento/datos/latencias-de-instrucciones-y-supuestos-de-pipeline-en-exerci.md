---
tipo: "dato"
titulo: "Latencias de instrucciones y supuestos de pipeline en Exercise 3 AC June 2019"
temas: ["ac", "pipeline", "superscalar", "vliw"]
claves: ["L.D MEM 2 ciclos", "MUL.D EX 2 ciclos", "resto 1 ciclo", "fully pipelined", "forwarding", "delay branch 1 slot"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]] · [[vliw]]

Parámetros de temporización para el ejercicio:
- Instrucciones de carga (L.D): etapa MEM dura 2 ciclos.
- Multiplicaciones (MUL.D): etapa EX dura 2 ciclos.
- Todas las demás operaciones (SUB.D, ADD.D, LSH, etc.): 1 ciclo en su etapa correspondiente.
- Unidades funcionales: totalmente segmentadas (aceptan nueva operación cada ciclo).
- Forwarding: habilitado (resultados disponibles tan pronto se producen).
- Control de saltos: delay branch con 1 delay slot (la instrucción tras el salto se ejecuta siempre).

> Assume that load instructions require 2 cycles for their MEM step, multiplications require 2 cycles for their EX step, and the rest of operations require 1 cycle. Besides, we know that all functional units are fully pipelined, forwarding is supported, and delay branch is used (with 1 delay slot).
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[ejercicio-3-ac-june-2019-comparacion-superscalar-in-order-vs]]
