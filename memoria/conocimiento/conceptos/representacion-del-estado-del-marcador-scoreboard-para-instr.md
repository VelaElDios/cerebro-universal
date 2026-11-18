---
tipo: "concepto"
titulo: "Representación del estado del marcador (scoreboard) para instrucciones FP"
temas: ["ac", "arquitectura", "punto-flotante", "scoreboard", "tomasulo"]
claves: ["fld", "fmul.d", "fsub.d", "fdiv.d", "fadd.d", "emisión", "lectura operandos", "ejecución completa", "escritura resultado", "unidades funcionales", "registro resultado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[punto-flotante]] · [[scoreboard]] · [[tomasulo]]

El marcador muestra para cada instrucción FP cuatro etapas con su ciclo: Emisión (issue), Lectura de operandos (read operands), Ejecución completa (execution complete), Escritura de resultado (write result). Las instrucciones del ejemplo son cargas (fld), multiplicación double (fmul.d), resta double (fsub.d), división double (fdiv.d) y suma double (fadd.d). Cada fila avanza por ciclos sucesivos hasta completar la escritura.

> Estado de las instrucciones Lectura Ejecución Escritura ciclo 16 Instrucción Emisión Operandos completa resultado fld f6, 34(x2) 1 2 3 4
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[simulacion-ciclo-a-ciclo-del-marcador-scoreboard-de-tomasulo]] · [[como-leer-la-evolucion-ciclo-a-ciclo-de-un-marcador-con-carg]] · [[ejemplo-de-simulacion-del-marcador-con-instrucciones-de-punt]]
