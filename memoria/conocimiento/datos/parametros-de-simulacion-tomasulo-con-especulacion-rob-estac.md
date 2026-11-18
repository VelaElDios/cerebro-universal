---
tipo: "dato"
titulo: "Parámetros de simulación Tomasulo con especulación: ROB, estaciones de reserva, buffer de carga"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["ROB 6 entradas", "estación reserva 2 entradas por UF", "buffer carga 1 entrada", "especulación hardware"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Configuración exacta para la simulación del Problema 3: ROB (Reorder Buffer) con 6 entradas. Una estación de reserva por cada Unidad Funcional (UF), cada una con 2 entradas. Un único buffer de carga (Load Buffer) con 1 entrada. El procesador usa especulación hardware según Tomasulo con especulación (incluye ROB para confirmación en orden). No hay buffer de almacenamiento mencionado (quizás se usa estación de reserva de store o buffer separado no limitado). Estas restricciones estructurales causan paradas por falta de entradas (structural hazards) durante la emisión.

> • El sistema cuenta con un ROB de 6 entradas, una estación de reserva por UF con 2 entradas y un buffer de carga de 1 entrada
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`

Relacionado: [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[configuracion-de-recursos-para-tomasulo-especulativo-en-exam]] · [[configuracion-tomasulo-con-especulacion-del-examen-ac-junio]] · [[configuracion-tomasulo-con-rob-para-simulacion-de-examen-ene]]
