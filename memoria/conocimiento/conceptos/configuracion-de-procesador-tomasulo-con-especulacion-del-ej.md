---
tipo: "concepto"
titulo: "Configuración de procesador Tomasulo con especulación del Ejercicio 2"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["Tomasulo", "speculation", "ROB", "reservation stations", "load/store buffers", "CDB", "MIPS64", "FP latency"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Parámetros exactos del procesador para la simulación de Tomasulo con especulación:
- Latencias: Load/Store EX=2 ciclos, FP MUL EX=7 ciclos, FP ADD EX=3 ciclos.
- ROB: 4 entradas.
- Estaciones de reserva: 2 entradas por cada unidad FP (suma y multiplicación).
- Buffers de carga y almacenamiento: 2 entradas cada uno, separados.
- CDB: arbitraje estricto (una escritura por ciclo).
- Liberación de recursos: un recurso liberado en ciclo N solo puede usarse en ciclo N+1.
- Instrucciones a planificar: L.D F0,0(R1); L.D F2,0(R2); ADD.D F4,F0,F2; L.D F6,0(R3); MUL.D F8,F4,F6; ADD.D F10,F6,F12; S.D F8,8(R1); S.D F10,8(R2).

> Let be a MIPS64 processor using hardware speculation and dynamic scheduling using the Tomasulo technique with speculation, with the following characteristics: The load and store execution stage takes 2 cycles. The floating point (FP) multiplication execution step takes 7 cycles. The floating-point addition (FP) execution step takes 3 cycles. A 4-entry reorder buffer (ROB) is provided. 2-entry reservation stations are available for each unit in FP. It has different load and store buffers of 2 entries each. Any stage of an instruction that wants to write to the CDB (Common Data Bus) cannot do so if another instruction is already using it. In general, any resource released at a given clock cycle cannot be used until the next one.
> — `repo:datos/temarios/AC/examenes/January2024.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]] · [[parametros-de-simulacion-tomasulo-especulativo-para-mips64-e]] · [[simulacion-tomasulo-con-especulacion-parametros-de-hardware]] · [[parametros-de-tomasulo-con-especulacion-para-problema-2-exam]]
