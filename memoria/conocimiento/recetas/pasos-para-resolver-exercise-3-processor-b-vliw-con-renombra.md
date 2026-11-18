---
tipo: "receta"
titulo: "Pasos para resolver Exercise 3 Processor B (VLIW con renombrado y schedule agresivo)"
temas: ["ac", "pipeline", "static scheduling", "vliw"]
claves: ["VLIW 2 ops", "static scheduling aggressive", "out-of-order scheduling", "register renaming supported"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[static scheduling]] · [[vliw]]

Metodología para rellenar tabla Processor B (ciclos 1-12):
1. Renombrar registros para eliminar WAR/WAW: asignar registro físico nuevo a cada escritura.
2. Construir grafo de dependencias RAW reales (tras renombrado).
3. Programar (schedule) operaciones en ciclos respetando:
   - Máx 2 ops/ciclo (cualquier tipo).
   - Latencias: L.D MEM=2, MUL.D EX=2, resto 1.
   - Forwarding: consumidor puede empezar EX en ciclo siguiente a productor fin EX/MEM.
   - Unidades totalmente segmentadas → sin límites de inicio salvo 2 ops/ciclo.
4. Objetivo: minimizar ciclos totales (makespan).
5. Generar paquetes VLIW por ciclo (hasta 2 ops).
6. Rellenar tabla: cada fila = ciclo, columnas = operaciones emitidas ese ciclo con sus etapas.
Nota: al tener renombrado, SUB.D F7,F1,F2 y L.D F4,0(R10) pueden ir en paralelo si no hay RAW entre ellas.

> Processor B is a VLIW processor able to issue two operations (of any type) per instruction. Static scheduling is as aggressive and efficient as possible to optimize the resulting code (operations can be scheduled out of order, and register renaming is supported).
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[ejercicio-3-ac-june-2019-comparacion-superscalar-in-order-vs]] · [[latencias-de-instrucciones-y-supuestos-de-pipeline-en-exerci]]
