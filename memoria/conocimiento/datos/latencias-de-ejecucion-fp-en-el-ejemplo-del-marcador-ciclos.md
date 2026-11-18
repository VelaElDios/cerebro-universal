---
tipo: "dato"
titulo: "Latencias de ejecución FP en el ejemplo del marcador (ciclos 16-22)"
temas: ["ac", "fadd.d", "fdiv.d", "fld", "fmul.d", "fsub.d", "latencia", "scoreboard"]
claves: ["ciclos", "emisión", "lectura", "ejecución", "escritura", "fdiv.d 14 ciclos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[fadd.d]] · [[fdiv.d]] · [[fld]] · [[fmul.d]] · [[fsub.d]] · [[latencia]] · [[scoreboard]]

Tiempos observados en la simulación (ciclos relativos al inicio): fld: emisión→lectura 1c, lectura→ejecución 1c, ejecución→escritura 1c (total 3c). fmul.d: emisión en 6, ejecución completa en 19 (13c), escritura en 20. fsub.d: emisión en 7, ejecución completa en 11 (4c), escritura en 12. fdiv.d: emisión en 8, aún ejecutando en ciclo 22 (≥14c). fadd.d: emisión en 13, ejecución completa en 16 (3c), escritura retardada a 22 por WAR.

> fdiv.d f10, f0, f6 8
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[calculo-de-flops-ciclo-para-avx2-con-fma]] · [[latencias-de-unidades-funcionales-en-el-ejemplo-tomasulo-cic]] · [[latencias-de-unidades-funcionales-en-el-ejemplo-de-marcador]] · [[ejemplo-de-simulacion-del-marcador-con-instrucciones-de-punt]]
