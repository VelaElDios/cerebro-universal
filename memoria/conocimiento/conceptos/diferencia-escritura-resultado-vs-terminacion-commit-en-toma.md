---
tipo: "concepto"
titulo: "Diferencia Escritura resultado vs Terminación (Commit) en Tomasulo con ROB"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["escritura resultado CDB vs terminacion commit ROB", "diferencia write result commit"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

En Tomasulo con especulación (ROB), las 4 etapas de la tabla son distintas:
1. **Emisión (Issue)**: Instrucción despachada, entrada ROB asignada, estación de reserva asignada, operandos leídos/renombrados (Qj/Qk o Vj/Vk). 1 ciclo, en orden.
2. **Ejecución (Execution)**: Instrucción espera operandos en ER, luego ocupa UF por N ciclos (latencia). Empieza cuando operandos listos y UF libre. Múltiples ciclos según tabla de latencias.
3. **Escritura resultado (Write Result / CDB)**: Resultado viaja por BDC a ROB (entrada correspondiente) y a estaciones de reserva que esperan esa etiqueta (Q). 1 ciclo. **Restricción**: no puede coincidir en mismo ciclo con inicio de ejecución de consumidor (ver nota restricción CDB).
4. **Terminación (Commit)**: Instrucción en cabeza de ROB, resultado ya en ROB, escribe en registro arquitectónico (banco registros) y libera entrada ROB. 1 ciclo, en orden estricto. Solo 1 commit por ciclo (puerto único escritura banco registros). Si hay excepción, se vacía ROB (flush).

> Rellena la tabla indicando los ciclos en los que se completa cada etapa.                        Instrucción    Emisión   Ejecución    Escritura resultado   Terminación
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf` (cita sin comprobar)

Relacionado: [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]]
