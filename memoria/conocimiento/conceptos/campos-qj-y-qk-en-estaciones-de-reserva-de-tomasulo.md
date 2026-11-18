---
tipo: "concepto"
titulo: "Campos Qj y Qk en estaciones de reserva de Tomasulo"
temas: ["ac", "estaciones-reserva", "renombrado", "tomasulo"]
claves: ["Qj", "Qk", "reservation station", "productor"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[estaciones-reserva]] · [[renombrado]] · [[tomasulo]]

En el algoritmo de Tomasulo, cada estación de reserva guarda en Qj y Qk el identificador (etiqueta) de la estación de reserva que producirá los operandos fuente. Cuando esa estación termina, publica el resultado en el CDB y las estaciones esperando ese valor lo capturan y limpian sus Qj/Qk. Esto implementa renombrado de registros dinámico y permite ejecución fuera de orden.

> The Qj and Qk fields in a reservation station in Tomasulo store: The reservation stations that will produce the instruction source operands.
> — `repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)` (cita sin comprobar)

Relacionado: [[estructura-de-una-estacion-de-reserva-en-tomasulo]] · [[que-es-una-estacion-de-reserva-en-el-algoritmo-de-tomasulo]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo-test-ac-q11]]
