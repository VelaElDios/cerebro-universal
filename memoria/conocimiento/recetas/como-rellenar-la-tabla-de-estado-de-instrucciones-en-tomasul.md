---
tipo: "receta"
titulo: "Cómo rellenar la tabla de estado de instrucciones en Tomasulo sin especulación"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["Tomasulo", "instruction status table", "Issue", "Execution", "Write result", "reservation stations", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Para completar la tabla de estado en Tomasulo sin especulación:
1. **Issue**: la instrucción se emite en el primer ciclo en que hay una estación de reserva libre para su tipo de UF y no hay riesgo estructural. Se registran los operandos (valor o etiqueta de estación que los producirá).
2. **Execution**: comienza cuando ambos operandos están disponibles (valor real o llegado por CDB). La latencia depende de la UF: típicamente ADD.D=2, MUL.D=4, DIV.D=10+ ciclos. La ejecución ocupa la UF durante esos ciclos.
3. **Write result**: en el ciclo siguiente al final de la ejecución, el resultado se difunde por el CDB; las estaciones de reserva y buffers de carga que esperan esa etiqueta capturan el valor.
Reglas clave:
- Una instrucción no puede emitirse si no hay estación libre (riesgo estructural).
- RAW: la instrucción espera en la estación hasta que los operandos llegan por CDB.
- WAW/WAR: se evitan gracias al renombrado implícito de las estaciones de reserva.
- El orden de finalización (Write result) puede ser distinto al de emisión (out-of-order completion).
- Para la secuencia del examen (DIV.D, ADD.D, SUB.D, S.D, MUL.D, DIV.D, L.D, ADD.D, MUL.D, ADD.D), simular ciclo a ciclo anotando qué estación se usa, cuándo llegan operandos y cuándo se libera la UF.

> Complete the following instruction status table, indicating the cycles in which each step is performed (TOMASULO WITHOUT speculation):
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]]
