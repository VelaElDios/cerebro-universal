---
tipo: "concepto"
titulo: "Diferencia entre especulación software y hardware (falso en software)"
temas: ["ac", "compilador", "especulacion", "prediccion-saltos"]
claves: ["software speculation", "hardware speculation", "compiler", "processor bets"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[compilador]] · [[especulacion]] · [[prediccion-saltos]]

La especulación software (compile-time) es el compilador quien apuesta por una dirección de salto y mueve instrucciones de ese bloque antes del salto (requiere predicción estática eficiente y renombrado para no alterar flujo de datos). La frase falsa describe especulación hardware (runtime): el procesador apuesta y ejecuta especulativamente durante la ejecución. En software, la decisión es estática, no dinámica del procesador.

> For the software speculation (without hardware support), which of the following sentences is false? During the execution of a program, the processor bets for a branch direction and the instructions of this block are executed speculatively. These instructions will be valid when the branch result is finally known.
> — `repo:datos/temarios/AC/examenes/January2023.pdf (trozo 1 de 2)` (cita sin comprobar)
