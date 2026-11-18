---
tipo: "concepto"
titulo: "Secuencia de instrucciones y latencias en ejemplo Tomasulo (ciclos 7-13)"
temas: ["ac", "punto-flotante", "simulacion", "tomasulo"]
claves: ["fld", "fmul.d", "fsub.d", "fdiv.d", "fadd.d", "latencia", "emision", "ejecucion", "escritura"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[punto-flotante]] · [[simulacion]] · [[tomasulo]]

La secuencia consta de 6 instrucciones emitidas en ciclos consecutivos (1-6):
- fld f6,34(x2): emitida c1, ejecución c2-3, escritura c4 (latencia carga 2 ciclos)
- fld f2,45(x3): emitida c2, ejecución c3-4, escritura c5
- fmul.d f0,f2,f4: emitida c3, ejecución comienza c6 (espera f2 de carga 2), sin escritura visible aún en c13
- fsub.d f8,f6,f2: emitida c4, ejecución c6-7, escritura c8 (espera f6 de carga 1 y f2 de carga 2)
- fdiv.d f10,f0,f6: emitida c5, sin ejecución visible en c13 (espera f0 de mul y f6 de carga 1)
- fadd.d f6,f8,f2: emitida c6, ejecución c9-10, escritura c11 (espera f8 de sub y f2 de carga 2; WAW en f6 resuelto por renombrado)

> Instrucción                Emisión           Ejecución     Escritura resultado fld      f6, 34(x2)                     1                2-3                  4 fld      f2, 45(x3)                     2                3-4                  5 fmul.d   f0, f2, f4                     3                6- fsub.d   f8, f6, f2                     4                6-7 fdiv.d   f10, f0, f6                    5 fadd.d   f6, f8, f2                     6
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[ejecucion-ciclo-a-ciclo-del-ejemplo-tomasulo-fld-fmul-d-fsub]] · [[secuencia-exacta-de-ciclos-para-cada-instruccion-en-la-simul]] · [[ejecucion-paso-a-paso-de-instrucciones-fp-en-tomasulo-ciclos]]
