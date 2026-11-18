---
tipo: "receta"
titulo: "Cómo leer la tabla de estado de instrucciones en simulación Tomasulo"
temas: ["ac", "ejecucion", "emision", "escritura", "simulacion", "tabla-estado", "tomasulo"]
claves: ["ciclo", "instruccion", "emision", "ejecucion", "escritura-resultado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ejecucion]] · [[emision]] · [[escritura]] · [[simulacion]] · [[tabla-estado]] · [[tomasulo]]

La tabla "Estado de las instrucciones" tiene 4 columnas por ciclo:
1. Instrucción: mnemónico y operandos (ej. "fld f6, 34(x2)").
2. Emisión: ciclo en que se emitió (asignó estación de reserva / buffer de carga).
3. Ejecución: rango de ciclos de ejecución (ej. "2-3" = ciclos 2 y 3; "6-" = empieza en 6, fin desconocido).
4. Escritura resultado: ciclo en que escribe en CDB y actualiza registro/estaciones (ej. "4").
En ciclos 7-13 la tabla no cambia (emisión ya pasó), solo avanza la columna Ejecución (ej. fadd.d: "9-" → "9-10" → "9-10" con escritura 11 en c11). Esto permite ver cuándo empieza/termina cada instrucción y cuándo se libera su estación de reserva.

> Estado de las instrucciones   ciclo 7                           Instrucción                Emisión           Ejecución     Escritura resultado
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[secuencia-de-instrucciones-y-latencias-en-ejemplo-tomasulo-c]] · [[como-leer-la-tabla-de-estado-de-tomasulo-en-ciclos-consecuti]] · [[como-se-traza-la-ejecucion-ciclo-a-ciclo-en-el-algoritmo-de]] · [[como-leer-la-tabla-de-estado-de-instrucciones-en-el-marcador]]
