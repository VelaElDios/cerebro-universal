---
tipo: "concepto"
titulo: "Condición necesaria para que la especulación sea válida"
temas: ["ac", "especulacion", "excepciones", "poison-bits", "tomasulo"]
claves: ["speculation", "valid speculation", "exceptions", "poison bits", "register renaming"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[excepciones]] · [[poison-bits]] · [[tomasulo]]

La especulación requiere que las excepciones de instrucciones especulativas no se tomen hasta que la instrucción se confirme (no especulativa). Esto se logra con bits venenosos (poison bits) que marcan resultados excepcionales y lanzan la excepción solo al usar el registro. Respuesta: b. The registers used by the program are not modified (implícito: estado arquitectónico no modificado hasta commit).

> What condition must be met for speculation to be valid?
> — `repo:datos/temarios/AC/examenes/June2025.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[buffer-de-carga-en-tomasulo-especulativo]]
