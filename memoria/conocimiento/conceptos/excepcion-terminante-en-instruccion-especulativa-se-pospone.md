---
tipo: "concepto"
titulo: "Excepción terminante en instrucción especulativa: se pospone hasta que deja de ser especulativa"
temas: ["ac", "especulacion", "excepcion-terminante", "tomasulo"]
claves: ["excepción terminante", "instrucción especulativa", "posponer", "commit"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[excepcion-terminante]] · [[tomasulo]]

Las excepciones terminantes (non-resumable) en instrucciones especulativas no se atienden de inmediato; se espera a que la instrucción se vuelva no especulativa (llegue a commit). Si en commit sigue siendo especulativa (p. ej., predicción errónea), se descarta y la excepción no se toma. Respuesta correcta: b.

> In case of a speculative instruction causing a non-resumable (terminating) exception: a) The exception must be immediately handled b) The exception should not be handled until the instruction ceases to be speculative c) The exception should not be handled in any case d) None of the above
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[comportamiento-de-bit-de-veneno-poison-bit-ante-excepcion-en]] · [[condicion-necesaria-para-que-la-especulacion-sea-valida]] · [[bits-venenosos-excepcion-no-recuperable-marca-registro-desti]]
