---
tipo: "concepto"
titulo: "Problema examen AC: Tomasulo con especulación, buffers carga/almacenamiento y UF múltiples"
temas: ["ac", "especulacion", "tomasulo"]
claves: ["Tomasulo", "especulación", "buffer carga 2 entradas", "buffer almacenamiento 1 entrada", "Bus Datos Común", "UF PF"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Diciembre2010.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[especulacion]] · [[tomasulo]]

Configuración Tomasulo para examen: especulación hardware, Common Data Bus (CDB) con restricción: no escritura e inicio ejecución mismo ciclo. Buffers: carga 2 entradas (latencia 2 ciclos), almacenamiento 1 entrada (latencia 2 ciclos). UF PF: 2 Sumador/Restador (2 RS c/u, 2 ciclos), 2 Multiplicador (2 RS c/u, 6 ciclos), 1 Divisor (2 RS, 12 ciclos). Programa: 3 LD, ADDD, MULTD, DIVD, ADDD, SD. Rellenar tabla: Emisión, Ejecución, Escritura resultado, Terminación.

> Tenemos un procesador con especulación hardware según el método de Tomasulo con especulación. Se dispone de un Bus de Datos Común y se supone que en el mismo ciclo de reloj no se puede escribir un dato en este bus e iniciar la ejecución de una operación que estuviera esperando ese dato.
> — `repo:datos/temarios/AC/examenes/Diciembre2010.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo]] · [[diferencia-entre-buffers-de-carga-y-de-almacenamiento-en-la]] · [[parametros-de-simulacion-tomasulo-con-especulacion-del-exame]] · [[configuracion-tomasulo-con-especulacion-del-examen-ac-junio]] · [[configuracion-y-parametros-para-simular-tomasulo-en-problema]]
