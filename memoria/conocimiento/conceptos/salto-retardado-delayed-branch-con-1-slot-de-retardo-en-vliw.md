---
tipo: "concepto"
titulo: "Salto retardado (delayed branch) con 1 slot de retardo en VLIW"
temas: ["ac", "delayed-branch", "planificacion", "vliw"]
claves: ["delayed branch", "1 delay slot", "BNEZ", "slot de retardo", "planificacion estatica"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[delayed-branch]] · [[planificacion]] · [[vliw]]

En este VLIW, el salto condicional BNEZ tiene 1 delay slot: la instrucción inmediatamente posterior al salto en el código secuencial se ejecuta siempre (tanto si el salto se toma como si no). En la planificación VLIW, esto significa que la instrucción en el delay slot debe colocarse en el mismo ciclo o en un ciclo anterior al BNEZ en la tabla de planificación, y no puede ser movida después del salto. El compilador/planificador debe rellenar ese slot con una instrucción útil (a menudo una de las DADDUI o una carga de la siguiente iteración si hay desenrollado) o dejarlo como NOP si no hay instrucción independiente disponible. Esto afecta al cálculo de operaciones por ciclo (IPC) porque el slot de retardo cuenta como operación ejecutada en el ciclo del salto.

> As usual, assume that this processor supports forwarding and delayed branch (with 1 delay slot).
> — `repo:datos/temarios/AC/examenes/January2017.pdf`

Relacionado: [[codigo-del-bucle-a-planificar-en-vliw-examen-ac-enero-2017]]
