---
tipo: "concepto"
titulo: "Especulación con bits venenosos: programa continúa y finaliza dando error ante excepción no recuperable"
temas: ["ac", "especulacion", "poison bits", "tomasulo"]
claves: ["bits venenosos", "poison bits", "excepción no recuperable", "especulación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[poison bits]] · [[tomasulo]]

Los bits venenosos (poison bits) marcan resultados de instrucciones especulativas que causaron excepciones. La excepción no se lanza inmediatamente; se propaga el bit venenoso hasta el commit. Si la instrucción llega a commit (es decir, la especulación era correcta), entonces se lanza la excepción y el programa termina con error. Si la especulación era incorrecta, la instrucción se descarta y la excepción se ignora.

> En la especulación con 'bits venenosos', al ejecutar una instrucción especulativa que genera una excepción no recuperable siempre ocurre que: a) El programa continua pero finaliza obteniendo valores indefinidos b) El programa continúa y finaliza correctamente c) El programa continua y finaliza dando un error d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[especulacion-con-poison-bits-propagacion-y-excepcion-diferid]]
