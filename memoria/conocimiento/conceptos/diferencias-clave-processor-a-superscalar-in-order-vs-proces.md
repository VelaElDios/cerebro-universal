---
tipo: "concepto"
titulo: "Diferencias clave Processor A (superscalar in-order) vs Processor B (VLIW) en Exercise 3"
temas: ["ac", "pipeline", "superscalar", "vliw"]
claves: ["in-order issue", "no register renaming", "static scheduling", "aggressive", "out-of-order scheduling", "register renaming supported"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]] · [[vliw]]

Comparación de capacidades:
Processor A (Superscalar 2-vías in-order):
- Emisión in-order: las instrucciones se emiten en orden de programa, máximo 2 por ciclo.
- Ventana de emisión "lo suficientemente grande" → no hay límite estructural de ventana, solo dependencias y recursos.
- SIN renombrado de registros → dependencias de nombre (WAR, WAW) causan hazards reales y frenan emisión.
- Hardware decide dinámicamente qué pares emitir cada ciclo respetando orden.

Processor B (VLIW 2 ops):
- Planificación estática (compilador): reordena operaciones agresivamente para maximizar ILP.
- Puede emitir 2 operaciones de CUALQUIER tipo por instrucción VLIW (sin restricciones de tipo).
- CON renombrado de registros → elimina dependencias de nombre (WAR, WAW).
- El compilador conoce latencias y recursos; genera paquetes VLIW óptimos.
- No hay hardware de emisión dinámica; el schedule es fijo en tiempo de compilación.

> Processor A is a 2-way superscalar processor with in-order issue and an issue window large enough for considering all the instructions. The processor does not support register renaming. Processor B is a VLIW processor able to issue two operations (of any type) per instruction. Static scheduling is as aggressive and efficient as possible to optimize the resulting code (operations can be scheduled out of order, and register renaming is supported).
> — `repo:datos/temarios/AC/examenes/June2019.pdf` (cita sin comprobar)

Relacionado: [[ejercicio-3-ac-june-2019-comparacion-superscalar-in-order-vs]] · [[pasos-para-resolver-exercise-3-processor-a-superscalar-in-or]] · [[diferencias-clave-entre-los-tres-modelos-de-ejecucion-supers]]
