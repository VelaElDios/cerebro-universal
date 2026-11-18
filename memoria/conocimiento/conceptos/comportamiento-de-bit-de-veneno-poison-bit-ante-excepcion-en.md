---
tipo: "concepto"
titulo: "Comportamiento de bit de veneno (poison bit) ante excepción en instrucción no especulativa"
temas: ["ac", "especulacion", "poison-bit", "tomasulo"]
claves: ["poison bit", "terminating exception", "non-speculative"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[poison-bit]] · [[tomasulo]]

En especulación con poison bits, las instrucciones *especulativas* posponen la excepción poniendo el bit de veneno en el registro destino. Para instrucciones **no especulativas (normales)**, una excepción terminante se maneja inmediatamente: el SO toma el control y el programa termina (o salta al handler). No se propaga poison bit. Respuesta correcta: c) The exception is handled, and the program execution finishes.

> After a terminating exception due to a non-speculative (normal) instruction, in the “poison bit” speculation method… a) An undefined value is obtained, and the program continues b) The poison bit associated to the instruction destination register is set, and the program continues c) The exception is handled, and the program execution finishes d) None of the above
> — `repo:datos/temarios/AC/examenes/June2018.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[comportamiento-de-bits-de-veneno-poison-bits-ante-excepcion]] · [[bits-venenosos-excepcion-no-recuperable-marca-registro-desti]] · [[comportamiento-de-bits-venenosos-ante-excepcion-terminante-e]]
