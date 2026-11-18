---
tipo: "concepto"
titulo: "Tomasulo especulativo: excepción en instrucción especulativa se maneja en commit (pregunta 16)"
temas: ["ac", "commit", "especulacion", "excepcion", "rob", "tomasulo"]
claves: ["Tomasulo especulativo", "excepción", "commit", "ROB", "bits veneno"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[commit]] · [[especulacion]] · [[excepcion]] · [[rob]] · [[tomasulo]]

En Tomasulo con especulación (con ROB), las excepciones de instrucciones especulativas no se toman inmediatamente; se marcan (bits de veneno en el ROB/registro) y solo se procesan cuando la instrucción llega al paso de commit (confirmación en orden de programa). Si la instrucción no se confirma (p. ej., salto mal predicho), la excepción se descarta. Respuesta correcta: b).

> In the speculative version of the Tomasulo's Algorithm, an exception caused by a speculative instruction a) Is never handled b) Is handled when the instruction reaches its commit step c) Is handled just when it is produced d) None of the above
> — `repo:datos/temarios/AC/examenes/January2017.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[configuracion-tomasulo-con-especulacion-para-examen-enero-20]]
