---
tipo: "dato"
titulo: "Parámetros de unidades funcionales y buffers en examen AC Junio 2013 P2"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["MIPS64", "Tomasulo especulativo", "ROB 6 entradas", "Load Buffer 1", "Store Buffer 1", "latencias UF"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Configuración exacta del problema 2:
- Arquitectura: MIPS64, Tomasulo con especulación, ROB = 6 entradas
- Buffers memoria: 1 Load Buffer, 1 Store Buffer (cada uno actúa como estación de reserva única para L.D/S.D)
- Latencia ejecución L.D / S.D: 2 ciclos (cálculo dirección + acceso)
- Unidades funcionales FP:
  * Sumador/Restador (ADD.D, SUB.D): 2 unidades, 1 estación de reserva c/u, 2 ciclos ejecución
  * Multiplicador (MUL.D): 1 unidad, 2 estaciones de reserva, 8 ciclos ejecución
  * Divisor (DIV.D): 1 unidad, 3 estaciones de reserva, 10 ciclos ejecución
  * Otras UF (enteras, etc.): 1 ciclo ejecución
- Bus Común de Datos (CDB/BDC): 1 solo bus, 1 escritura/ciclo
- Restricción temporal: "en el mismo ciclo de reloj no se puede escribir un dato en el Bus de Datos Común (BDC) e iniciar la ejecución de una operación que estuviera esperando ese dato" → hazard de lectura-escritura en CDB mismo ciclo.
- Programa: 8 instrucciones (2 L.D, ADD.D, MUL.D, L.D, ADD.D, 2 S.D)

> Sumador/Restador 2 1 2; Multiplicador 1 2 8; Divisor 1 3 10; El resto de las UF emplean 1 ciclo en la etapa de ejecución.
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf` (cita sin comprobar)

Relacionado: [[ancho-y-tamano-en-bits-de-un-btb-implicito-con-1024-entradas]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[configuracion-tomasulo-con-especulacion-del-examen-ac-junio]] · [[configuracion-tomasulo-examen-enero-2023-unidades-fp-rob-buf]] · [[configuracion-de-tomasulo-con-especulacion-para-examen-ac-ju]]
