---
tipo: "concepto"
titulo: "Técnica Poisson: carga especulativa con dirección inválida pone bit de veneno en registro destino"
temas: ["ac", "especulacion", "poison-bit", "poisson", "tomasulo"]
claves: ["Poisson", "carga especulativa", "bit veneno", "registro destino", "excepción diferida"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[poison-bit]] · [[poisson]] · [[tomasulo]]

En la técnica Poisson (especulación con carga), si una carga especulativa accede a dirección inválida, no se lanza la excepción inmediatamente; se marca el registro destino (R5) con un bit de veneno (poison bit). La excepción se pospone hasta que una instrucción no especulativa intente usar ese registro. Respuesta correcta: c.

> Indicate the behavior of a MIPS64 processor executing the speculative instruction LW* R5, 0(R1), assuming the Poisson technique. We know that R1=0 and that the access to memory addresses 0 and 1 is not allowed. a) An exception will always be launched, and the program will end b) The code will always be executed, and the program will end correctly c) The poison bit corresponding to R5 will always be set d) The poison bit corresponding to R1 will always be set
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]]
