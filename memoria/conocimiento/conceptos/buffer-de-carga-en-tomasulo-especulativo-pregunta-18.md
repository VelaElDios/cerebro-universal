---
tipo: "concepto"
titulo: "Buffer de carga en Tomasulo especulativo (pregunta 18)"
temas: ["ac", "especulacion", "load-buffer", "tomasulo"]
claves: ["Tomasulo especulativo", "load buffer", "cola circular", "instrucciones no especulativas", "lectura operandos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[load-buffer]] · [[tomasulo]]

Respuesta correcta: d) None of the above. En Tomasulo especulativo, el load buffer almacena direcciones y datos de cargas especulativas, permite desambiguación de memoria y reenvío de datos a instrucciones dependientes; no es cola circular obligatoria, no guarda solo resultados no especulativos, y las instrucciones leen operandos de estaciones de reserva/CDB, no directamente del load buffer.

> In the speculative version of the Tomasulo algorithm, the load buffer: a) Is implemented by a circular queue b) Stores the results of non-speculative instructions c) Is accessed by the instructions for operand reading d) None of the above
> — `repo:datos/temarios/AC/examenes/June2021.pdf`

Relacionado: [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]]
