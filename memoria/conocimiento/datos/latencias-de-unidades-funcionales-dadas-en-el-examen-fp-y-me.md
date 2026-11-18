---
tipo: "dato"
titulo: "Latencias de unidades funcionales dadas en el examen (FP y memoria)"
temas: ["ac", "latencias", "pipeline", "tomasulo"]
claves: ["FP ADD", "FP MUL", "DIV.D", "Load", "Store", "ciclos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[latencias]] · [[pipeline]] · [[tomasulo]]

Latencias explícitas del enunciado (Ejercicio 2):
- Load/Store execution: **1 ciclo**
- FP Multiplication (MUL.D): **6 ciclos**
- FP Addition (ADD.D, SUB.D): **4 ciclos**
- **DIV.D**: **NO ESPECIFICADA** en el texto. En exámenes reales suele darse o asumirse conocida (p.ej. 12-20 ciclos). Para simulación exacta hay que consultar el resto del examen o asumir un valor estándar del temario.
- Ejercicio 3 (superscalar): **Todas las instrucciones 1 ciclo** en cada etapa (Decode, Execute, Write), independientemente de tipo (LW, DADD, DSUB).

> The load and store execution stage takes 1 cycle. The floating-point multiplication (FP) execution step takes 6 cycles. The floating-point addition (FP) execution step takes 4 cycles.
> — `repo:datos/temarios/AC/examenes/January2022.pdf` (cita sin comprobar)

Relacionado: [[parametros-de-simulacion-tomasulo-especulativo-para-mips64-e]] · [[configuracion-superscalar-4-issue-para-diagramas-de-pipeline]]
