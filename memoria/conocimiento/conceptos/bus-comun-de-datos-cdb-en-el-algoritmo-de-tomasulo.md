---
tipo: "concepto"
titulo: "Bus Común de Datos (CDB) en el algoritmo de Tomasulo"
temas: ["ac", "broadcast", "cdb", "tomasulo"]
claves: ["Common Data Bus", "CDB", "resultados", "unidades funcionales", "acceso memoria"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[broadcast]] · [[cdb]] · [[tomasulo]]

El CDB es un bus de difusión (broadcast) por el que **todas las unidades funcionales y los accesos a memoria (cargas/almacenes) publican sus resultados** (valor + etiqueta de estación de reserva). Las estaciones de reserva y el ROB (en versión con ROB) escuchan el CDB para capturar operandos que esperan (eliminando riesgos RAW) y para actualizar el estado de las instrucciones en vuelo.

> The Common Data Bus (CDB) used in the Tomasulo's scheme... a) Is the bus where the results of the functional units and the memory accesses are sent.
> — `repo:datos/temarios/AC/examenes/January2018.pdf`

Relacionado: [[contenido-de-una-estacion-de-reserva-en-tomasulo-test-ac-q11]]
