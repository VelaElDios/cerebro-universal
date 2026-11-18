---
tipo: "decision"
titulo: "Orden de emisión en orden (in-order issue) con ejecución fuera de orden en el ejemplo"
temas: ["ac", "ejecucion-fuera-orden", "emision-orden", "tomasulo"]
claves: ["emision", "ciclo", "instruccion", "estacion-reserva", "buffer-carga"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[ejecucion-fuera-orden]] · [[emision-orden]] · [[tomasulo]]

El ejemplo ilustra emisión en orden (in-order issue): las 6 instrucciones se emiten en ciclos 1-6 consecutivos sin saltos, aunque sus operandos no estén listos. La ejecución es fuera de orden (out-of-order execution):
- fmul.d (c3) espera f2 hasta c6 (carga 2 termina c4, +1 ciclo para CDB).
- fsub.d (c4) espera f6 (carga 1 c4) y f2 (c5) → empieza c6.
- fdiv.d (c5) espera f0 (mul) y f6 (carga 1) → no empieza en c13.
- fadd.d (c6) espera f8 (sub c8) y f2 (c5) → empieza c9.
La escritura en registro (write result) también es fuera de orden: fsub.d escribe c8, fadd.d c11, fmul.d y fdiv.d aún no en c13.

> Instrucción                Emisión           Ejecución     Escritura resultado fld      f6, 34(x2)                     1                2-3                  4 fld      f2, 45(x3)                     2                3-4                  5 fmul.d   f0, f2, f4                     3                6- fsub.d   f8, f6, f2                     4                6-7 fdiv.d   f10, f0, f6                    5 fadd.d   f6, f8, f2                     6
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[cronograma-de-emision-ejecucion-y-escritura-por-instruccion]] · [[secuencia-de-instrucciones-y-latencias-en-ejemplo-tomasulo-c]] · [[ejecucion-ciclo-a-ciclo-del-ejemplo-tomasulo-fld-fmul-d-fsub]]
