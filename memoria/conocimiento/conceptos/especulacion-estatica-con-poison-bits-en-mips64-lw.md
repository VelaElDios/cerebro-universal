---
tipo: "concepto"
titulo: "Especulación estática con poison bits en MIPS64 (LW*)"
temas: ["ac", "mips64", "prediccion-saltos"]
claves: ["LW*", "poison bit", "especulación estática", "carga especulativa", "excepción diferida", "BEQZ", "DADDI", "DADD", "SW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips64]] · [[prediccion-saltos]]

La especulación estática con poison bits permite ejecutar instrucciones de forma especulativa (antes de saber si su camino de control se tomará) marcando los resultados con un "poison bit" si causan una excepción. En MIPS64 del temario, la instrucción LW* (carga especulativa) no lanza la excepción inmediatamente; en su lugar, propaga el poison bit al registro destino. Las instrucciones que usan un registro con poison bit propagan el bit a sus resultados. La excepción solo se materializa (y detiene el programa) cuando una instrucción no especulativa (como SW o una instrucción de salto resuelta) intenta usar un valor "envenenado" o cuando se resuelve el salto que validaba la especulación. Esto permite mover cargas por encima de saltos (code motion) sin riesgo de excepciones prematuras. En el examen, la dirección 0 es ilegal: cualquier acceso (lectura/escritura) a 0 lanza excepción. La memoria [0..1023] está inicializada a 0, pero el acceso a 0 sigue siendo ilegal.

> Se dispone de un procesador basado en el MIPS64, y diversos mecanismos para la realización de especulación estática con el siguiente código. LW* R1, 0(R1) ; Carga especulativa
> — `repo:datos/temarios/AC/examenes/Enero2015.pdf`

Relacionado: [[especulacion-con-poison-bits-propagacion-y-excepcion-diferid]] · [[especulacion-estatica-con-cargas-especulativas-lw-en-mips64]]
