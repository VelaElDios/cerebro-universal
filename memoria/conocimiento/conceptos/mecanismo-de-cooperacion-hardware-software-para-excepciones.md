---
tipo: "concepto"
titulo: "Mecanismo de cooperación hardware/software para excepciones especulativas"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["hardware/software cooperation", "undefined value", "speculative instruction", "exception handling"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

En este mecanismo, el hardware distingue instrucciones normales y especulativas. Ante una excepción en instrucción especulativa, la rutina de servicio devuelve un valor indefinido (undefined) en el registro destino y la ejecución prosigue sin abortar. Las instrucciones normales que causan excepción terminan el programa. En las tablas del examen, la DDIV* especulativa pone R5←undefined; las instrucciones siguientes (BNE, DDIV, DADDI, DADD) se ejecutan normalmente y el programa termina con R5=undefined si no hay escritura posterior, o con el valor escrito si la hay.

> The processor has a hardware/software cooperation mechanism that distinguishes between normal and speculative instructions. If the instruction that throws the exception is normal, the exception's service routine will terminate the program, but if it is speculative, the routine will return an undefined value (without aborting the execution).
> — `repo:datos/temarios/AC/examenes/January2024.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[tres-mecanismos-de-manejo-de-excepciones-para-instrucciones]] · [[mecanismo-cooperacion-hardware-software-sin-distincion-instr]] · [[funcionamiento-detallado-de-bits-de-veneno-poison-bits-en-es]]
