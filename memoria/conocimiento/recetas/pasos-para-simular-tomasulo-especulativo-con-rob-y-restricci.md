---
tipo: "receta"
titulo: "Pasos para simular Tomasulo especulativo con ROB y restricciones de timing (guía práctica)"
temas: ["ac", "pipeline", "simulacion", "tomasulo"]
claves: ["issue", "execute", "write result", "commit", "CDB", "ROB", "reservation station", "load buffer"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[simulacion]] · [[tomasulo]]

Algoritmo paso a paso para rellenar la tabla de 4 columnas (Issue, Execution, Write result, Commit) por instrucción:
1. **Ciclo 0**: Estado inicial, todo libre.
2. **Issue (en orden, 1 por ciclo si hay RS/ROB/Load Buffer libre)**:
   - Asignar entrada ROB (siguiente cola circular), marcar Busy=yes, Destination=reg destino, Value=tag o valor.
   - Asignar RS (si FP) o Load Buffer (si load/store) si hay libre. Rellenar operandos: si disponibles en RF/ROB → valor; si no → tag de productor (ROB index o RS tag).
   - Si no hay recurso estructural (RS, ROB, LB) → stall issue.
3. **Execution start**: Cuando **todos** los operandos de la RS/LB tienen valor (no tags) **Y** hay FU libre **Y** se cumple la regla CDB: si el último operando llegó por CDB en ciclo N, execution empieza en N+1.
   - Duración: Load/Store=1, FP ADD=4, FP MUL=6, DIV.D= (no dada, asumir latencia conocida o dejar variable).
4. **Execution end**: Ciclo start + latencia - 1 (si latencia=1, start=end).
5. **Write result (CDB)**: En el ciclo **siguiente** al execution end (porque "result is available at the next cycle in which that result is written" — aunque esa frase es del Ejercicio 3, en Tomasulo clásico el write es en el ciclo siguiente a execution end). Broadcast por CDB: actualiza RS esperando ese tag, actualiza ROB entry (Value=resultado, Status=Write), libera RS/LB (pero **regla de liberación**: no reutilizable hasta ciclo siguiente).
6. **Commit (en orden de ROB)**: Cuando la entrada ROB está en head y Status=Write, commit en ese ciclo (o siguiente si hay regla de 1 ciclo). Libera entrada ROB (regla de liberación: libre para issue en ciclo siguiente). Actualiza RF arquitectónico.
7. **Avanzar ciclo a ciclo** registrando para cada instrucción: Issue cycle, Execution start-end, Write result cycle, Commit cycle.
8. **Para la tabla ROB**: Congelar estado en el ciclo donde Execution end del primer L.D. (instr 3). Volcar las 4 entradas ROB con sus campos.

> Detail the execution of the code below when the basic version of Tomasulo's algorithm with speculation is used. To do so, indicate in the table below the start and end cycle number for each of the steps of each instruction (NB: For 1-cycle instruction steps, you must annotate just 1 cycle in the table).
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[parametros-de-simulacion-tomasulo-especulativo-para-mips64-e]] · [[restricciones-de-timing-en-tomasulo-con-especulacion-examen]]
