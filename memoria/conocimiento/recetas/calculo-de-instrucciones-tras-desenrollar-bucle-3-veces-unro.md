---
tipo: "receta"
titulo: "Cálculo de instrucciones tras desenrollar bucle 3 veces (unroll factor 3)"
temas: ["ac", "bucles", "loop-unrolling", "pipeline"]
claves: ["desenrollamiento", "unroll 3 veces", "instrucciones resultantes", "DADDUI inmediato"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[loop-unrolling]] · [[pipeline]]

Bucle original: 6 instrucciones (I1-I6). Al desenrollar 3×: se replican las 5 instrucciones de cuerpo (I1-I5) tres veces = 15, más una sola instrucción de salto (I6) con incremento ajustado. Total = 16 instrucciones. Pero la opción correcta es 14 (c) porque el DADDUI se fusiona: en lugar de 3 DADDUI #-8, se pone 1 DADDUI #-24. Así: 3×(L.D, ADD.D, SUB.D, S.D) = 12 + 1 DADDUI #-24 + 1 BNEZ = 14.

> We unroll 3 times this loop (assuming that the number of iterations is divisible by 3): ... a) The resulting loop will be composed of 6 instructions. b) 9 instructions. c) 14 instructions. d) 18 instructions.
> — `repo:datos/temarios/AC/examenes/January2021.pdf` (cita sin comprobar)

Relacionado: [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]]
