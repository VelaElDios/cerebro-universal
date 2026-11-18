---
tipo: "receta"
titulo: "Configuración y parámetros para simular Tomasulo en problema de examen (MIPS64, UF segmentadas, latencias dadas)"
temas: ["ac", "buffers-carga-almacenamiento", "estaciones-reserva", "latencias", "simulacion", "tomasulo"]
claves: ["Tomasulo", "UF suma/resta", "UF multiplicación", "UF división", "estaciones reserva", "buffer carga", "buffer almacenamiento", "ciclos ejecución", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[buffers-carga-almacenamiento]] · [[estaciones-reserva]] · [[latencias]] · [[simulacion]] · [[tomasulo]]

Parámetros clave para simulación: 3 UF segmentadas (ADD, MUL, DIV) con 2 estaciones de reserva cada una. Load buffer: 2 entradas. Store buffer: 1 entrada. Latencias ejecución: L.D=2, ADD.D=2, MUL.D=6, DIV.D=10. Reglas de timing: (1) Resultado en CDB en ciclo X → instrucción esperando puede empezar ejecución en ciclo X+1. (2) Recurso liberado en ciclo X → disponible en ciclo X+1. Estas restricciones evitan solapamiento de escritura CDB e inicio ejecución, y de liberación y reuso de estación/buffer. Esencial para diagramas de Gantt ciclo a ciclo.

> Disponemos de un procesador con arquitectura MIPS64 equipado con planificación dinámica según el algoritmo de Tomasulo. Supón que: • Todas las UF están segmentadas. Hay una UF para suma/resta, otra UF para multiplicación y otra UF para división. Hay dos estaciones de reserva por UF, un buffer de carga con 2 entradas y un buffer de almacenamiento con 1 entrada. • La etapa de ejecución de la instrucción L.D requiere 2 ciclos de reloj, mientras que la ejecución de las instrucciones ADD.D, MUL.D y DIV.D requiere 2, 6 y 10 ciclos, respectivamente. • La ejecución de una instrucción que está esperando un resultado no puede comenzar en el mismo ciclo en el que este resultado es escrito en el Bus Común de Datos. • Un recurso que es liberado en un ciclo de reloj no puede ser usado hasta el siguiente ciclo.
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[buffer-de-carga-en-tomasulo-especulativo]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[parametros-estandar-para-simular-tomasulo-con-especulacion-e]] · [[configuracion-tomasulo-con-especulacion-del-examen-ac-junio]] · [[parametros-de-simulacion-tomasulo-con-especulacion-del-exame]]
