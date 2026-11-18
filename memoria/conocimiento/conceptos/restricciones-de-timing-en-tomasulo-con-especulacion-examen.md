---
tipo: "concepto"
titulo: "Restricciones de timing en Tomasulo con especulación (examen AC)"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["CDB", "hazard", "burbuja", "liberación recurso", "especulación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Dos reglas de timing que cambian la simulación estándar de Tomasulo:
1. **CDB-to-Execution delay**: Si una instrucción espera un operando que llega por CDB en ciclo N, su etapa de ejecución no puede empezar hasta el ciclo N+1 (mínimo 1 ciclo de burbuja). Esto modela el tiempo de captura del bus y latch de operandos en las RS.
2. **Resource release latency**: Cuando una RS, entrada de ROB o load buffer se libera en ciclo N, no puede ser reasignada hasta el ciclo N+1. Esto evita colisiones de puerto de escritura/lectura en la misma arista de reloj.
Ambas reglas añaden ciclos de burbuja respecto al modelo ideal y son cruciales para obtener la tabla de ciclos correcta en el examen.

> The execution stage of an instruction that is waiting for a result cannot start in the same cycle in which the result is written to the CDB (Common Data Bus). • A resource that is released in one clock cycle cannot be used until the next clock cycle.
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[reglas-de-cdb-y-liberacion-de-recursos-en-tomasulo-con-rob]] · [[restriccion-de-uso-del-cdb-y-liberacion-de-recursos-en-tomas]] · [[restriccion-cdb-mismo-ciclo-en-tomasulo-no-iniciar-ejecucion]]
