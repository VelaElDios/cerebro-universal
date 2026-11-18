---
tipo: "dato"
titulo: "Configuración Tomasulo con especulación del examen AC Junio 2014 (extraordinario)"
temas: ["ac", "pipeline", "prediccion-saltos", "tomasulo"]
claves: ["ROB 4 entradas", "estacion reserva 2 entradas por UF", "buffer carga 2 entradas", "UF suma/resta", "UF multiplicacion", "UF division", "latencias ADD.D SUB.D MUL.D DIV.D L.D S.D"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]] · [[tomasulo]]

Configuración exacta del procesador del problema:
- ROB: 4 entradas
- Estaciones de reserva: 1 por UF, cada una con 2 entradas (total 3 UFs → 6 entradas de ER)
- Buffer de carga: 2 entradas
- Unidades funcionales segmentadas:
  * 1 UF suma/resta (ADD.D, SUB.D): latencia 2 ciclos
  * 1 UF multiplicación (MUL.D): latencia 4 ciclos
  * 1 UF división (DIV.D): latencia 20 ciclos
  * Carga/almacenamiento (L.D, S.D): latencia 2 ciclos (etapa ejecución)
  * Resto instrucciones: 1 ciclo
- Restricción crítica: "En el mismo ciclo de reloj no se puede escribir un dato en el Bus de Datos Común (BDC) e iniciar la ejecución de una operación que estuviera esperando ese dato" → implica que el forwarding por CDB tiene 1 ciclo de latencia efectiva para consumidores.

> Tenemos un procesador MIPS64 con especulación hardware según el método de Tomasulo con especulación y las siguientes características:  ROB de 4 entradas,  Una estación de reserva por UF con 2 entradas  Un buffer de carga de 2 entradas  UFs PF segmentadas: 1 UF para suma/resta, 1 UF para la multiplicación y 1 UF para división.  En el mismo ciclo de reloj no se puede escribir un dato en el Bus de Datos Común (BDC) e iniciar la ejecución de una operación que estuviera esperando ese dato
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[configuracion-de-tomasulo-con-especulacion-para-examen-ac-ju]] · [[configuracion-y-parametros-para-simular-tomasulo-en-problema]] · [[configuracion-de-procesador-tomasulo-con-especulacion-del-ej]]
