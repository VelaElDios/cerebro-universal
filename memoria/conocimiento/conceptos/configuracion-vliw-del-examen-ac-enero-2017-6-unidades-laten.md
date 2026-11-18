---
tipo: "concepto"
titulo: "Configuración VLIW del examen AC enero 2017 (6 unidades, latencias y forwarding)"
temas: ["ac", "examen", "planificacion", "vliw"]
claves: ["VLIW", "2 integer units", "2 memory units", "2 FP units", "latency 1", "latency 3", "latency 4", "forwarding", "delayed branch", "1 delay slot"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[planificacion]] · [[vliw]]

Procesador VLIW de 6 vías de ejecución usado en el examen de enero 2017:
- 2 unidades enteras (INT1, INT2): operaciones ALU enteras y saltos, latencia 1 ciclo.
- 2 unidades de memoria (MEM1, MEM2): carga y almacenamiento, totalmente segmentadas (fully pipelined), latencia 3 ciclos.
- 2 unidades FP: una para suma (FP ADD) y otra para multiplicación (FP MUL), totalmente segmentadas, latencia 4 ciclos.
- Soporte de forwarding (reenvío de resultados) y salto retardado (delayed branch) con exactamente 1 slot de retardo.
Esta configuración define las restricciones de recursos y latencias para la planificación estática del bucle.

> Exercise 3 (2 points). The next code is run on a VLIW processor with 6 execution units: • 2 integer units (used for integer ALU operations and branch operations), with a 1-cycle latency • 2 fully pipelined memory units (for store and load operations), with a 3-cycle latency • 2 fully pipelined FP units (one for addition and the other for multiplication), with a 4-cycle latency As usual, assume that this processor supports forwarding and delayed branch (with 1 delay slot).
> — `repo:datos/temarios/AC/examenes/January2017.pdf`
