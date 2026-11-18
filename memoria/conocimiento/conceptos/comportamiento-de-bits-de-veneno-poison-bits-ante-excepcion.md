---
tipo: "concepto"
titulo: "Comportamiento de bits de veneno (poison bits) ante excepción en instrucción no especulativa"
temas: ["ac", "especulacion", "poison-bits", "tomasulo"]
claves: ["poison bits", "bits veneno", "excepción finalización", "instrucción normal"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[poison-bits]] · [[tomasulo]]

Los poison bits marcan resultados de instrucciones **especulativas** que causan excepción (diferida). Si la instrucción **no es especulativa** (normal), su excepción es real y **termina el programa** inmediatamente. No se propaga veneno. Opción correcta: c. "La ejecución del programa finaliza."

> En la técnica de los bits de veneno (o poison), si una instrucción normal (no especulativa) provoca una excepción de finalización: a. La ejecución del programa continúa, pero el bit de veneno del registro destino se activa (1). b. La ejecución del programa continúa, pero el bit de veneno del registro destino se limpia (0). c. La ejecución del programa finaliza. d. Ninguna es correcta.
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[especulacion-con-poison-bits-propagacion-y-excepcion-diferid]] · [[comportamiento-de-bit-de-veneno-poison-bit-ante-excepcion-en]] · [[comportamiento-de-bits-venenosos-ante-excepcion-terminante-e]] · [[especulacion-con-bits-venenosos-programa-continua-y-finaliza]]
