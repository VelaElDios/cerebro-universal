---
tipo: "decision"
titulo: "Diferencias clave entre los tres modelos de ejecución superscalar (examen AC)"
temas: ["ac", "pipeline", "renaming", "superscalar"]
claves: ["in-order", "out-of-order", "renaming", "WAR", "WAW", "ROB", "scoreboard"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[renaming]] · [[superscalar]]

Qué cambia en cada modelo y por qué afecta al diagrama:
- **Modelo a) In-order / In-order**: Issue en orden de programa, máx 4/ciclo. Execute en orden de issue (scoreboard simple), máx 5/ciclo. Write en orden de programa, máx 4/ciclo. Las dependencias RAW/WAR/WAW causan stalls en decode o execute. No hay salto de instrucciones.
- **Modelo b) OoO exec / No renaming / In-order write**: Issue en orden (4/ciclo). Execute fuera de orden: una instrucción puede empezar execute si sus operandos están listos y hay FU libre, **pero** no puede saltar una instrucción anterior que escribe el mismo registro (WAW) ni una que lee el registro que va a escribir (WAR), porque no hay renombrado. Write sigue en orden de programa (commit in-order), máx 4/ciclo. Esto requiere scoreboard con seguimiento de WAR/WAW.
- **Modelo c) OoO exec / Con renaming / OoO write**: Issue en orden (4/ciclo) con renombrado de registros de destino (eliminando WAR/WAW). Execute fuera de orden puro: solo RAW real (flow dependence) frena. Write fuera de orden: cada instrucción escribe en su ciclo de write tan pronto termina execute y hay puerto de write libre (máx 4/ciclo). Equivale a Tomasulo con ROB pero sin latencias variables (todo 1 ciclo).
Puntos críticos para el dibujo:
- I2 espera a I1 (RAW R1) en todos los modelos.
- I6 escribe R8 (WAW con I3) y lee R1 (RAW con I1).
- I7 escribe R3 (WAW con I4) y lee R3 (WAR con I4) y R1 (RAW con I1).
- En modelo b, I6 no puede ejecutar antes que I3 termine write (WAW en R8) e I7 no puede ejecutar antes que I4 termine write (WAR en R3).
- En modelo c, renombrado elimina WAW/WAR: I6 e I7 ejecutan tan pronto tienen R1 y R3 (renombrado) listos.

> a) In-order execution and in-order writing. b) Out-of-order execution, without renaming capacity, and in-order writing. c) Out-of-order execution with renaming (assuming enough registers for this), and out-of-order writing.
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[definicion-de-dependencia-de-salida-waw-entre-dos-instruccio]] · [[antidependencia-war-y-dependencia-de-salida-waw-definiciones]]
