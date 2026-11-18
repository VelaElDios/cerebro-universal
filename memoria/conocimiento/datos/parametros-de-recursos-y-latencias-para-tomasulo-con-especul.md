---
tipo: "dato"
titulo: "Parámetros de recursos y latencias para Tomasulo con especulación (examen June 2025)"
temas: ["ac", "tomasulo"]
claves: ["ROB", "load buffer", "reservation stations", "FP add", "FP multiply", "load/store latency", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

Configuración exacta del examen: ROB 32 entradas; Load Buffer 16 entradas; Estaciones de reserva: 2 para suma FP (ADD.D), 4 para multiplicación/división FP; Latencias de ejecución: Load/Store 1 ciclo, FP Add 2 ciclos, FP Mul 4 ciclos. Regla CDB: solo una instrucción puede escribir en el CDB por ciclo. Regla de recursos: un recurso liberado en ciclo N no puede usarse hasta ciclo N+1.

> We have an ROB with a capacity for 32 instructions, a load buffer with 16 entries, and reserve stations with 2 entries for addition and 4 for multiplication and division. The load and store execution stage uses 1 cycle. The floating-point multiplication (FP) execution step takes 4 cycles. The floating point (FP) addition execution step takes 2 cycles.
> — `repo:datos/temarios/AC/examenes/June2025.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]]
