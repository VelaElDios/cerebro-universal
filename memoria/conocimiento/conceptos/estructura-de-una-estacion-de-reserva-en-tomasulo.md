---
tipo: "concepto"
titulo: "Estructura de una estación de reserva en Tomasulo"
temas: ["ac", "arquitectura", "tomasulo"]
claves: ["estacion de reserva", "busy", "op", "Vj", "Vk", "Qj", "Qk"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[tomasulo]]

Cada estación de reserva tiene: Nombre (identificador), Ocupada (bit busy), Op (operación a realizar), Vj/Vk (valores de operandos si están disponibles), Qj/Qk (números de estaciones de reserva que producirán los operandos si no están listos). Permite renombrado de registros y ejecución fuera de orden.

> Nombre Ocupada Op Vj Vk Qj Qk Indica si la estación de reserva y su unidad asociada está o no ocupada Operación a realizar sobre los operandos fuente Valor de los operandos fuente Estaciones de reserva que producirán el correspondiente operando fuente
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo-test-ac-q11]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo]]
