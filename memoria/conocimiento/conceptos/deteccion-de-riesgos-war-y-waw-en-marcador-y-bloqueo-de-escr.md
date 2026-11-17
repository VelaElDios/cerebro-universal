---
tipo: "concepto"
titulo: "Detección de riesgos WAR y WAW en marcador y bloqueo de escritura"
temas: ["ac", "arquitectura", "hazard", "riesgos", "scoreboard", "war", "waw"]
claves: ["WAR", "WAW", "riesgo", "bloqueada", "escritura resultado", "registro destino", "fadd.d", "f6"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[hazard]] · [[riesgos]] · [[scoreboard]] · [[war]] · [[waw]]

En el ciclo 9 la instrucción `fadd.d f6, f8, f2` aparece marcada como **Bloqueada** en la columna de Escritura resultado. Esto ilustra dos riesgos clásicos que el marcador detecta y frena:

- **Riesgo WAR (Write After Read)**: `fadd.d` escribe en **f6**, pero `fsub.d` (ciclo 7) y `fdiv.d` (ciclo 8) **leen f6** como operando fuente. El marcador obliga a `fadd.d` a esperar hasta que **todas las instrucciones previas que lean f6 hayan completado su lectura de operandos** (Rj/Rk=SI). En el ciclo 9, `fsub.d` ya leyó (ciclo 8b), pero `fdiv.d` aún no (su Qk=1 indica que espera a UF 1 para f6).

- **Riesgo WAW (Write After Write)**: la primera instrucción `fld f6, 34(x2)` ya escribió f6 en el ciclo 4. Sin renombrado de registros, una segunda escritura en f6 (`fadd.d`) sería WAW. El marcador la bloquea hasta que sea seguro (en máquinas con scoreboard puro, esto requiere que la primera escritura haya terminado y no quede ninguna lectura pendiente).

La combinación WAR+WAW sobre f6 hace que `fadd.d` se quede en «Bloqueada» al final del fragmento. En implementaciones reales (Tomasulo con renombrado) el WAW se elimina, pero el WAR persiste hasta que los consumidores lean el valor.

> Bloqueada fadd.d f6, f8, f2
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[estructura-del-marcador-scoreboard-en-arquitectura-de-comput]] · [[como-leer-la-evolucion-ciclo-a-ciclo-de-un-marcador-con-carg]]
