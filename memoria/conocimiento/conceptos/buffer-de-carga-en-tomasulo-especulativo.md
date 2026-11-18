---
tipo: "concepto"
titulo: "Buffer de carga en Tomasulo especulativo"
temas: ["ac", "especulacion", "load buffer", "tomasulo"]
claves: ["speculative Tomasulo", "load buffer", "circular queue", "operands"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[load buffer]] · [[tomasulo]]

En la versión especulativa de Tomasulo, el **load buffer** (y el store buffer) actúan como **estaciones de reserva para instrucciones de memoria**. Las instrucciones de carga obtienen sus operandos (dirección base + offset) del buffer de carga, y el buffer gestiona la especulación: la carga se ejecuta, pero su resultado no se hace visible hasta el commit; si hay fallo de predicción, se descarta. No es una cola circular ni almacena solo resultados no especulativos.

> In the speculative version of Tomasulo, the load buffer… c) Is used by the instructions to obtain their operands.
> — `repo:datos/temarios/AC/examenes/January2018.pdf` (cita sin comprobar)

Relacionado: [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[buffer-de-carga-en-tomasulo-especulativo-pregunta-18]] · [[configuracion-y-parametros-para-simular-tomasulo-en-problema]]
