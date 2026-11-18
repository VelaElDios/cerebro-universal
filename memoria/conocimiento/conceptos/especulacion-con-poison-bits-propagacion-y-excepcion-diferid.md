---
tipo: "concepto"
titulo: "Especulación con poison bits - propagación y excepción diferida"
temas: ["ac", "arquitectura", "poison-bits", "prediccion-saltos"]
claves: ["poison bit", "especulación", "excepción diferida", "propagación sucio", "instrucción no especulativa"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2014.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[arquitectura]] · [[poison-bits]] · [[prediccion-saltos]]

Con poison bits: (1) Las instrucciones especulativas (LW*) que fallan no lanzan excepción inmediata; marcan su registro destino con poison bit=1 (valor "sucio"). (2) Las instrucciones que usan registros sucios como operandos propagan el poison bit a su registro destino (también se marcan "sucios"). (3) Solo cuando una instrucción NO especulativa (confirmada) intenta usar un valor sucio como operando o escribir memoria con dato sucio, se lanza la excepción real y termina el programa. (4) Las instrucciones especulativas en ruta incorrecta (no confirmadas) se descartan sin efecto.

> c) Especulación con poison bits.
> — `repo:datos/temarios/AC/examenes/Enero2014.pdf`

Relacionado: [[tres-mecanismos-de-especulacion-evaluados-en-examen-ac-enero]] · [[convencion-etiquetas-indefinido-y-sucio-para-poison-bits-en]]
