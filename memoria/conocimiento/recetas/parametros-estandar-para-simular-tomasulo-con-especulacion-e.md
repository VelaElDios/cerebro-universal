---
tipo: "receta"
titulo: "Parámetros estándar para simular Tomasulo con especulación en ejercicios de examen"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["parámetros simulación", "buffer carga 2", "buffer store 1", "UF FP", "ciclos ejecución", "estaciones reserva"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Plantilla de configuración para resolver ejercicios de Tomasulo especulativo:
- Load Buffer: 2 entries, 2-cycle execution
- Store Buffer: 1 entry, 2-cycle execution
- FP Add/Sub: 2 units × 2 reservation stations each, 2-cycle latency
- FP Mul: 2 units × 2 reservation stations each, 6-cycle latency
- FP Div: 1 unit × 2 reservation stations, 12-cycle latency
- CDB: single bus, cannot broadcast result and start dependent execution in same cycle
- ROB: 10 entries
- Instruction mix: 3 loads, 2 FP adds, 1 FP mul, 2 stores

> El sistema dispone de un buffer de carga con 2 entradas y un buffer de almacenamiento con 1 entrada. La etapa de ejecución de ambas operaciones requiere 2 ciclos. Además, dispone de varias UF en coma flotante con 2 estaciones de reserva por UF y las siguientes características: Sumador/Restador 2 cantidad 2 ciclos, Multiplicador 2 cantidad 6 ciclos, Divisor 1 cantidad 12 ciclos
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]]
