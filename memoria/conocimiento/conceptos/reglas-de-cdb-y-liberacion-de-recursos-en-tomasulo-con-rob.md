---
tipo: "concepto"
titulo: "Reglas de CDB y liberación de recursos en Tomasulo con ROB"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["CDB", "Common Data Bus", "resource release", "same cycle", "next cycle"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Dos reglas críticas de temporización en esta variante de Tomasulo con ROB:
1. **Escritura en CDB y despertar en el mismo ciclo**: cuando una instrucción escribe su resultado en el Common Data Bus, cualquier instrucción que estuviera esperando ese operando comienza su etapa de ejecución **en ese mismo ciclo** (no hay burbuja de un ciclo para el wake-up).
2. **Liberación de recursos con retardo de un ciclo**: si una unidad funcional, estación de reserva, entrada de ROB o load buffer se libera en el ciclo *t*, no está disponible para una nueva instrucción hasta el ciclo *t+1*. Esto afecta a la etapa de Issue (asignación de recursos) y a la reutilización de estaciones de reserva tras el Write Result.
Estas reglas son decisivas para calcular correctamente los ciclos de Execute, Write Result y Commit en la tabla de simulación.

> In the same clock cycle in which a result is written in the Common Data Bus (CDB) the execution of any instruction that was waiting for that result is initiated. A resource that is released/freed in a clock cycle cannot be used until the next cycle.
> — `repo:datos/temarios/AC/examenes/January2021.pdf` (cita sin comprobar)

Relacionado: [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]] · [[actualizacion-de-la-btb-tras-ejecutar-el-salto]]
