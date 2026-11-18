---
tipo: "decision"
titulo: "Uso de delayed branch con 1 delay slot en VLIW para ocultar latencia de salto"
temas: ["ac", "pipeline", "vliw"]
claves: ["delayed branch", "delay slot", "planificación", "salto condicional"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[vliw]]

El procesador VLIW implementa delayed branch con un único delay slot: la instrucción situada inmediatamente después del salto en el código secuencial se ejecuta siempre, independientemente de si el salto se toma o no. En la planificación, esto permite colocar una instrucción útil (que no dependa del salto) en ese slot, evitando una burbuja. En el bucle dado, la instrucción posterior a BNEZ es la primera del bucle (L.S F1,0(R1)), pero al ser un bucle, el delay slot se puede llenar con una instrucción de la propia iteración (p.ej., un DADDUI) o de la siguiente, siempre que sea segura. El compilador/planificador debe reordenar instrucciones para aprovechar el slot.

> assume that this processor supports forwarding and delayed branch (with 1 delay slot)
> — `repo:datos/temarios/AC/examenes/January2019.pdf`

Relacionado: [[planificacion-scheduling-de-bucle-en-vliw-con-forwarding-y-d]] · [[definicion-de-latencia-de-salto-y-huecos-de-retardo]] · [[delayed-branch-en-vliw-y-su-efecto-en-planificacion]] · [[salto-retardado-delayed-branch-con-1-slot-de-retardo-en-vliw]]
