---
tipo: "concepto"
titulo: "Tres mecanismos de manejo de excepciones para instrucciones especulativas"
temas: ["ac", "pipeline", "prediccion-saltos", "tomasulo"]
claves: ["especulación", "excepciones", "DDIV*", "bits de veneno", "cooperación hardware/software"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[prediccion-saltos]] · [[tomasulo]]

El documento describe tres mecanismos para manejar excepciones en instrucciones especulativas: (a) Sin soporte de especulación: cualquier excepción termina el programa inmediatamente. (b) Cooperación hardware/software: distingue instrucciones normales y especulativas; las normales terminan el programa, las especulativas devuelven un valor indefinido (undefined) y continúan la ejecución. (c) Especulación con bits de veneno (poison bits): la excepción en instrucción especulativa marca el registro destino con poison bit=1 (dirty); si una instrucción no especulativa escribe ese registro, el bit se limpia; si una instrucción no especulativa lee un registro con poison bit=1, se lanza la excepción.

> Considering that there is a high probability that the branch condition will not be met, the compiler has generated the next version of the same code, with one speculative instruction (highlighted): DDIV* R5, R1, R5 ; speculative division
> — `repo:datos/temarios/AC/examenes/January2024.pdf` (cita sin comprobar)

Relacionado: [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]] · [[comportamiento-de-bits-de-veneno-ante-instruccion-no-especul]]
