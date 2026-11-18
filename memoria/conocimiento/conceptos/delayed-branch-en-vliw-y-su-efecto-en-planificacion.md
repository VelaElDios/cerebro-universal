---
tipo: "concepto"
titulo: "Delayed branch en VLIW y su efecto en planificación"
temas: ["ac", "delayed-branch", "planificacion", "vliw"]
claves: ["delayed branch", "delay slot", "branch penalty", "VLIW", "static scheduling"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[delayed-branch]] · [[planificacion]] · [[vliw]]

En arquitecturas con delayed branch (como MIPS clásico y muchos VLIW), la instrucción inmediatamente posterior al salto (delay slot) se ejecuta siempre, independientemente de si el salto se toma o no. En planificación VLIW estática, el compilador debe colocar una instrucción útil en ese slot (a menudo la primera instrucción de la siguiente iteración o una operación independiente). Si no hay instrucción útil, se pone NOP. En este problema, el BNEZ al final del bucle tiene un delay slot que puede usarse para iniciar la siguiente iteración (p.ej., la primera L.D de la iteración siguiente), reduciendo la penalidad del salto a cero ciclos efectivos.

> Consider also that this processor supports forwarding and delayed branch.
> — `repo:datos/temarios/AC/examenes/January2016.pdf`

Relacionado: [[problema-de-planificacion-vliw-con-desenrollado-de-bucle-exa]] · [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
