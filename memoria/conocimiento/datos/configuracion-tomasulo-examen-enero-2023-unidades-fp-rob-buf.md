---
tipo: "dato"
titulo: "Configuración Tomasulo examen enero 2023: unidades FP, ROB, buffers y restricciones de ciclo"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["Tomasulo", "FP adder", "FP multiplier", "FP divider", "ROB", "reservation station", "load buffer", "store buffer", "CDB", "ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Parámetros exactos del modelo Tomasulo usado en el ejercicio 2 del examen de enero 2023. Unidades FP totalmente segmentadas: suma/resta 4 ciclos, multiplicación 6, división 12. Carga/almacenamiento: 2 ciclos en etapa de ejecución. ROB con 4 entradas. Cada unidad FP tiene 2 reservation stations. Un load buffer y un store buffer de una entrada cada uno. Restricción de CDB: una instrucción que espera un resultado no puede iniciar su etapa de ejecución en el mismo ciclo en que el resultado llega por el CDB. Restricción de liberación: un recurso liberado en un ciclo no puede reutilizarse hasta el ciclo siguiente.

> The execution step of loads and stores takes 2 cycles. • There are three fully pipelined Floating-Point (FP) functional units: o a FP adder (also available for subtracting) that requires 4 cycles, o a FP multiplier that requires 6 cycles, and o a FP divider that requires 12 cycles. • A 4-input reorder buffer (ROB) is available. • There is a 2-entry reservation station per FP unit. • There is a 1-entry load buffer and a 1-entry store buffer. • The execution stage of an instruction that is waiting for a result cannot start in the same cycle in which the result is written to the CDB (Common Data Bus). • A resource (the ROB, a reservation station, etc.) that is released in one clock cycle cannot be used until the next clock cycle.
> — `repo:datos/temarios/AC/examenes/January2023.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]]
