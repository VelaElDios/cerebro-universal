---
tipo: "concepto"
titulo: "Planificación por software (software pipelining) y desenrollado de bucles"
temas: ["ac", "loop unrolling", "pipeline", "software pipelining"]
claves: ["software pipelining", "prologue", "kernel", "epilogue", "desenrollado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop unrolling]] · [[pipeline]] · [[software pipelining]]

El software pipelining solapa iteraciones: prologue (llenado), kernel (estado estable), epilogue (vaciado). El kernel tiene tantas instrucciones como el cuerpo original (aquí 6), pero reordenadas para eliminar paradas. El número total de instrucciones en el bucle modificado (kernel) es el mismo que el original. La opción correcta es b) The modified loop will have the same number of instructions as the original, in this case 6 instructions.

> We apply software pipelining to this loop: Bucle: L.D F0, 0(R1) ;I1 stall ADD.D F2, F0, F1 ;I2 stall SUB.D F3, F2, F0 ;I3 stall S.D F3, 0(R1) ;I4 DADDUI R1, R1, #-8 ;I5 stall BNEZ R1, Bucle ;I6 Assuming the indicated stalls and that there is not delayed branch…
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[segmentacion-software-software-pipelining-modifica-codigo-pa]] · [[calculo-de-instrucciones-tras-desenrollar-bucle-3-veces-unro]] · [[desenrollado-de-bucle-minimo-para-eliminar-todos-los-stalls]]
