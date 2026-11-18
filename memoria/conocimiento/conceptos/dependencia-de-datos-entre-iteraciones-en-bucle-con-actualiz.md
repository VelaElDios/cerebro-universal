---
tipo: "concepto"
titulo: "Dependencia de datos entre iteraciones en bucle con actualización de puntero (registro x1)"
temas: ["ac", "bucles", "dependencias-entre-iteraciones", "pipeline"]
claves: ["dependencia entre iteraciones", "loop-carried", "registro x1", "bucle fld fadd.d fsd addi bne"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[dependencias-entre-iteraciones]] · [[pipeline]]

El registro x1 se actualiza en cada iteración (`addi x1, x1, -8`) y se usa como base para las direcciones de carga/almacenamiento (`fld f0, 0(x1)`, `fsd f2, 0(x1)`) y para la condición de salto (`bne x1, x3, Bucle`). Esto crea una dependencia de datos entre iteraciones (loop-carried dependence) a través de x1. Los registros f0 y f2 se renuevan cada iteración sin depender de valores de iteraciones anteriores.

> Considera el siguiente bucle: Bucle: fld f0, 0(x1) fadd.d f2, f0, f4 fsd f2, 0(x1) addi x1, x1, -8 bne x1, x3, Bucle Indica cuál de las siguientes afirmaciones es cierta: ... Hay una dependencia de datos entre iteraciones que afecta al registro x1
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
