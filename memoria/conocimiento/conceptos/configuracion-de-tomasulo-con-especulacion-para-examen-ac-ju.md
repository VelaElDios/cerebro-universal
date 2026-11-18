---
tipo: "concepto"
titulo: "Configuración de Tomasulo con especulación para examen AC Junio 2012"
temas: ["ac", "pipeline", "prediccion-saltos", "tomasulo"]
claves: ["Tomasulo especulación", "MIPS64", "buffer carga", "buffer almacenamiento", "estaciones reserva", "CDB", "ROB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]] · [[tomasulo]]

Configuración completa del procesador para el ejercicio: MIPS64 con Tomasulo especulativo. Buffers: carga 2 entradas (ejecución 2 ciclos), almacenamiento 1 entrada (ejecución 2 ciclos). Unidades funcionales FP: 2 Sumador/Restador (2 ciclos, 2 estaciones cada una), 2 Multiplicador (6 ciclos, 2 estaciones cada una), 1 Divisor (12 ciclos, 2 estaciones). CDB con restricción: no se puede escribir en el bus e iniciar ejecución de operación esperando ese dato en el mismo ciclo. ROB de 10 entradas. Secuencia de 8 instrucciones típica de cómputo FP con dependencias RAW y WAW.

> Tenemos un procesador MIPS64 con especulación hardware según el método de Tomasulo con especulación. Se dispone de un Bus de Datos Común y se supone que en el mismo ciclo de reloj no se puede escribir un dato en este bus e iniciar la ejecución de una operación que estuviera esperando ese dato.
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]] · [[configuracion-tomasulo-con-especulacion-del-examen-ac-junio]] · [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]] · [[configuracion-de-procesador-tomasulo-con-especulacion-del-ej]]
