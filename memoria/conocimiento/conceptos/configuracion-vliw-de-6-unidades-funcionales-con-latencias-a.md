---
tipo: "concepto"
titulo: "Configuración VLIW de 6 unidades funcionales con latencias asimétricas"
temas: ["ac", "pipeline", "vliw"]
claves: ["VLIW", "unidades funcionales", "latencia EX", "latencia MEM", "forwarding", "delayed branch"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[vliw]]

Procesador VLIW con 6 unidades: INT1/INT2 (enteras/saltos, 1 ciclo EX, 1 ciclo MEM), MEM1/MEM2 (carga/almacenamiento, 1 ciclo EX, 2 ciclos MEM), FP ADD (suma FP, 1 unidad, 4 ciclos EX, 1 ciclo MEM), FP MUL (multiplicación FP, 1 unidad, 6 ciclos EX, 1 ciclo MEM). Soporta forwarding (evita paradas por dependencias RAW) y delayed branch con 1 delay slot (la instrucción tras el salto se ejecuta siempre). La planificación (scheduling) consiste en asignar cada instrucción a una unidad y ciclo concretos respetando dependencias, latencias y recursos, rellenando una tabla por ciclos con columnas INT1, INT2, MEM1, MEM2, FP ADD, FP MUL.

> The next code is run on a VLIW processor with 6 execution units: 2 integer units (for the execution of integer operations and branches), which require 1 cycle. 2 fully pipelined memory units (for stores and loads), which require two cycles for accessing memory. 2 fully pipelined FP units (for addition and multiplication), which require 4 (add) and 6 (mul) cycles.
> — `repo:datos/temarios/AC/examenes/January2019.pdf` (cita sin comprobar)

Relacionado: [[definicion-y-proposito-de-la-segmentacion-pipeline]] · [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]]
