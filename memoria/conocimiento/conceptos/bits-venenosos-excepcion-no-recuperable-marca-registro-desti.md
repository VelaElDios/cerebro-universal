---
tipo: "concepto"
titulo: "Bits venenosos: excepción no recuperable marca registro destino y programa continúa"
temas: ["ac", "bits-venenosos", "especulacion", "tomasulo"]
claves: ["bits venenosos", "excepción no recuperable", "registro destino", "especulación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bits-venenosos]] · [[especulacion]] · [[tomasulo]]

En especulación con bits venenosos (poison bits), cuando una instrucción (especulativa o no) causa una excepción no recuperable (ej. fallo de página), no se lanza la excepción inmediatamente. En su lugar, se marca el bit venenoso en el registro destino (o entrada ROB). La excepción se difiere hasta que una instrucción intenta usar ese registro como operando (o hace commit). El programa continúa ejecutando otras instrucciones independientes. Respuesta correcta: b) Se activa el bit venenoso del registro destino de la instrucción y el programa continua.

> Ante una excepción no recuperable causada por una instrucción no especulativa, en la especulación con 'bits venenosos' se cumple que: a) Se obtiene un valor indefinido y el programa continua b) Se activa el bit venenoso del registro destino de la instrucción y el programa continua c) La excepción se atiende y el programa finaliza d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf`

Relacionado: [[bits-venenosos-en-especulacion-excepcion-no-recuperable-marc]] · [[bits-venenosos-en-carga-especulativa-excepcion-diferida-hast]]
