---
tipo: "dato"
titulo: "Secuencia exacta de ciclos para cada instrucción en la simulación (ciclos 1-15)"
temas: ["ac", "cronograma", "fadd", "fdiv", "fld", "fmul", "fsub", "tomasulo"]
claves: ["ciclo 1 emisión fld f6", "ciclo 5 emisión fld f2", "ciclo 6 emisión fmul.d", "ciclo 7 emisión fsub.d", "ciclo 8 emisión fdiv.d", "ciclo 13 emisión fadd.d"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cronograma]] · [[fadd]] · [[fdiv]] · [[fld]] · [[fmul]] · [[fsub]] · [[tomasulo]]

Cronograma completo extraído de las tablas: fld f6,34(x2): emisión 1, lectura 2, ejecución 3, escritura 4. fld f2,45(x3): emisión 5, lectura 6, ejecución 7, escritura 8. fmul.d f0,f2,f4: emisión 6, lectura operandos 9 (espera f2 listo en ciclo 8), ejecución inicia 9, dura 10 ciclos (hasta ciclo 18 aprox). fsub.d f8,f6,f2: emisión 7, lectura 9 (espera f6 listo ciclo 4, f2 ciclo 8), ejecución 9-11 (2 ciclos), escritura 12. fdiv.d f10,f0,f6: emisión 8, lectura operandos espera f0 (Mult1) y f6 (Entera), ejecución inicia tras lectura, dura 9+ ciclos. fadd.d f6,f8,f2: bloqueada ciclos 10-12, emisión 13, lectura 14 (espera f8 listo ciclo 12), ejecución 14-15, escritura 16.

> ciclo 10                     Instrucción               Emisión              Operandos         completa     resultado                           fld        f6, 34(x2)              1                   2                 3            4                           fld        f2, 45(x3)              5                   6                 7            8                           fmul.d     f0, f2, f4              6                   9                           fsub.d     f8, f6, f2              7                   9                  11             12                           fdiv.d     f10, f0, f6             8                           fadd.d     f6, f8, f2
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[simulacion-ciclo-a-ciclo-del-marcador-scoreboard-de-tomasulo]] · [[latencias-de-unidades-funcionales-en-el-ejemplo-tomasulo-cic]] · [[secuencia-de-instrucciones-y-latencias-en-ejemplo-tomasulo-c]] · [[ejecucion-ciclo-a-ciclo-del-ejemplo-tomasulo-fld-fmul-d-fsub]] · [[cronograma-de-emision-ejecucion-y-escritura-por-instruccion]]
