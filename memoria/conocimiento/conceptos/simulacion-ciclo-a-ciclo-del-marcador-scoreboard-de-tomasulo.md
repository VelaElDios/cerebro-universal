---
tipo: "concepto"
titulo: "Simulación ciclo a ciclo del marcador (scoreboard) de Tomasulo con instrucciones FP"
temas: ["ac", "arquitectura", "punto-flotante", "scoreboard", "tomasulo"]
claves: ["fld", "fmul.d", "fsub.d", "fdiv.d", "fadd.d", "unidades funcionales", "estado registros resultado", "ciclos emisión lectura ejecución escritura"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[punto-flotante]] · [[scoreboard]] · [[tomasulo]]

El marcador (scoreboard) de Tomasulo controla el flujo de instrucciones en tres etapas principales: 1) Emisión (issue): se reserva unidad funcional y se renombran registros destino; 2) Lectura de operandos (read operands): espera a que los operandos estén disponibles (Qj/Qk = 0); 3) Ejecución (execution): la unidad funcional computa; 4) Escritura resultado (write result): broadcast en CDB y actualización de registros. En el ejemplo, las unidades funcionales son: Entera (cargas), Mult1/Mult2 (multiplicación), Suma (suma/resta), Divide (división). Cada ciclo avanza el estado de cada instrucción y se actualizan los contadores de ciclos restantes en las UF.

> ciclo 10                     Instrucción               Emisión              Operandos         completa     resultado                           fld        f6, 34(x2)              1                   2                 3            4
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`
