---
tipo: "decision"
titulo: "Restricción de conflicto en Bus Común de Datos (BDC/CDB): no escritura e inicio de ejecución simultáneos"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["BDC", "CDB", "conflicto bus", "escritura resultado", "inicio ejecución", "mismo ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Regla crítica para la simulación de ciclos: Si en ciclo C una instrucción escribe su resultado en el BDC (Common Data Bus), ninguna otra instrucción que estuviera esperando ese dato (en estación de reserva o buffer de carga) puede comenzar su etapa de ejecución en ese mismo ciclo C. Debe esperar al ciclo C+1 para leer el valor del bus (o del registro/ROB) y empezar EX. Esto añade 1 ciclo de latencia efectiva para consumidores directos (RAW) respecto al modelo ideal Tomasulo donde el forwarding es inmediato en el mismo ciclo. Afecta al cálculo de "Ejecución" y "Escritura resultado" en la tabla.

> • En el mismo ciclo de reloj no se puede escribir un dato en el Bus de Datos Común (BDC) e iniciar la ejecución de una operación que estuviera esperando ese dato.
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]]
