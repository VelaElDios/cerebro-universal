---
tipo: "concepto"
titulo: "Salto retardado con instrucción de bloque destino: riesgo si salto no tomado"
temas: ["ac", "branch delay slot", "delayed branch", "prediccion-saltos"]
claves: ["delayed branch", "branch delay slot", "taken", "not taken"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2011.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[branch delay slot]] · [[delayed branch]] · [[prediccion-saltos]]

Si se rellena el slot de retardo con una instrucción del bloque *destino* (target), esta se ejecuta siempre. Si el salto **no se toma** (fallo), la instrucción del destino se ejecuta erróneamente alterando el estado.

> El comportamiento del programa podría ser incorrecto si el salto finalmente no se toma
> — `repo:datos/temarios/AC/examenes/Enero2011.pdf`

Relacionado: [[penalizacion-de-salto-en-mips-resuelto-en-id-sin-prediccion]]
