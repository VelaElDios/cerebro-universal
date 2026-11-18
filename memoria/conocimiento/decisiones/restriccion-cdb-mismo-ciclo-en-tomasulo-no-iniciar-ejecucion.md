---
tipo: "decision"
titulo: "Restricción CDB mismo ciclo en Tomasulo: no iniciar ejecución y escribir dato simultáneamente"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["CDB", "BDC", "Bus Común de Datos", "hazard estructural", "ciclo de reloj", "estación de reserva"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Decisión de diseño / restricción de temporización explícita en el enunciado:
- **Regla**: En un mismo ciclo de reloj, si una instrucción escribe su resultado en el CDB (BDC), **ninguna** otra instrucción que estuviera esperando ese dato en una estación de reserva puede **iniciar** su etapa de ejecución en ese mismo ciclo.
- **Implicación**: Añade 1 ciclo de burbuja entre "dato disponible en CDB" y "inicio de ejecución del consumidor". El consumidor debe esperar al ciclo siguiente para leer el dato (vía forwarding desde CDB o desde registro) y empezar EX.
- **Por qué**: Modela limitación real de puerto de lectura/escritura en banco de registros o en mux de entrada de ALU; evita race condition en simulación de ciclo único.
- **Cómo aplicarlo en simulación**: Cuando una instrucción termina EX y va a escribir en CDB en ciclo T, las instrucciones que esperan su tag (Qj/Qk) **no** pueden pasar de "Esperando" a "Ejecutando" en ciclo T. Lo harán en T+1.
- **Ejemplo**: MUL.D termina EX en ciclo 10, escribe CDB en ciclo 11. ADD.D que espera F8 (resultado MUL) no puede empezar EX en ciclo 11; lo hará en ciclo 12.
- Esta regla es **adicional** a la contención normal por el CDB (solo 1 escritura/ciclo).

> Considera que en el mismo ciclo de reloj no se puede escribir un dato en el Bus de Datos Común (BDC) e iniciar la ejecución de una operación que estuviera esperando ese dato.
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]]
