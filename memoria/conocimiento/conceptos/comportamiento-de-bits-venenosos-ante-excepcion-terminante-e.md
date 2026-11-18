---
tipo: "concepto"
titulo: "Comportamiento de bits venenosos ante excepción terminante en instrucción no especulativa"
temas: ["ac", "bits venenosos", "especulación", "tomasulo"]
claves: ["poison bits", "excepción terminante", "instrucción normal"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bits venenosos]] · [[especulación]] · [[tomasulo]]

Los bits venenosos (poison bits) solo diferencian excepciones en instrucciones especulativas. Si una instrucción normal (no especulativa) causa una excepción terminante, el programa se detiene inmediatamente; no se propaga un bit venenoso.

> In the poison bits technique, if a normal (non-speculative) instruction results in a terminating exception: The execution of the program is stopped
> — `repo:datos/temarios/AC/examenes/January2022.pdf` (cita sin comprobar)

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[comportamiento-de-bits-de-veneno-ante-instruccion-no-especul]] · [[comportamiento-de-bits-de-veneno-poison-bits-ante-excepcion]] · [[bits-venenosos-en-especulacion-excepcion-no-recuperable-marc]] · [[comportamiento-de-bit-de-veneno-poison-bit-ante-excepcion-en]]
