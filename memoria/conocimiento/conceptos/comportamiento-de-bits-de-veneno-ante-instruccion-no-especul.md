---
tipo: "concepto"
titulo: "Comportamiento de bits de veneno ante instrucción no especulativa que usa registro con poison bit activo"
temas: ["ac", "tomasulo"]
claves: ["poison bits", "speculative execution", "exception handling", "MIPS64"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

En arquitectura MIPS64 con especulación y bits de veneno (poison bits), si una instrucción **no especulativa** intenta usar un registro origen que tiene el poison bit activado (porque una carga especulativa anterior falló), la excepción asociada a ese poison bit **debe ser atendida inmediatamente**, terminando el programa si procede. No se propaga el poison bit al destino, ni se ignora. Opción correcta: (c) The exception that set the poison bit of F1 will be attended (causing, if applicable, the termination of the program).

> What happens when a MIPS64-based processor executes the non-speculative instruction MUL.D F0, F1, F2, if register F1 has the poison bit activated (set)?
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[comportamiento-de-bits-de-veneno-poison-bits-ante-excepcion]] · [[comportamiento-de-bit-de-veneno-poison-bit-ante-excepcion-en]] · [[tecnica-poisson-carga-especulativa-con-direccion-invalida-po]]
