---
tipo: "dato"
titulo: "Latencia de carga FP y multiplicación doble en la simulación Tomasulo"
temas: ["ac", "latencia", "punto-flotante", "tomasulo"]
claves: ["fld latencia", "fmul.d ciclos", "escritura resultado", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[latencia]] · [[punto-flotante]] · [[tomasulo]]

Valores observados en la simulación:
- **fld (carga double)**: emitida en ciclo 1, empieza ejecución en ciclo 9, escribe resultado en ciclo 10 → latencia efectiva 9-10 ciclos desde emisión hasta escritura en CDB.
- **fmul.d (multiplicación double)**: emitida en ciclo 2, empieza ejecución en ciclo 14 (cuando operandos listos), escribe en ciclo 15 → latencia de ejecución 1 ciclo (contador Op baja de 4 a 0 en ciclos 10-14), pero espera 12 ciclos por dependencia de la carga.
- **fsd (almacenamiento double)**: emitida en ciclo 3, no muestra inicio/fin de ejecución en la tabla; depende de que fmul.d produzca f4 y la dirección esté lista (buffer Almac 1/2/3).

> fld f0, 0(x1) 1 9 10 fmul.d f4, f0, f2 2 14 15
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]] · [[latencias-asumidas-para-carga-2-ciclos-y-multiplicacion-fp-3]] · [[latencias-de-unidades-funcionales-en-el-ejemplo-tomasulo]] · [[secuencia-de-instrucciones-y-latencias-en-ejemplo-tomasulo-c]]
