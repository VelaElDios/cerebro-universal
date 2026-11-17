---
tipo: "dato"
titulo: "Latencias de unidades funcionales en el ejemplo Tomasulo (ciclos)"
temas: ["ac", "fadd", "fdiv", "fld", "fmul", "fsub", "latencias", "tomasulo"]
claves: ["Mult1 10 ciclos", "Divide 9 ciclos", "Suma 2 ciclos", "Entera 1 ciclo carga"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[fadd]] · [[fdiv]] · [[fld]] · [[fmul]] · [[fsub]] · [[latencias]] · [[tomasulo]]

Latencias observadas en la simulación: Unidad Entera (cargas fld): 1 ciclo de ejecución (emisión ciclo 1, lectura 2, ejecución 3, escritura 4). Multiplicador (Mult1, fmul.d): 10 ciclos de ejecución (inicia ejecución ciclo 9, aún con 4 ciclos restantes en ciclo 15). Divisor (Divide, fdiv.d): 9+ ciclos (inicia ejecución ciclo 8, aún con 2 ciclos restantes en ciclo 15). Sumador (Suma, fsub.d/fadd.d): 2 ciclos de ejecución (fsub.d: ejecución ciclos 9-11; fadd.d: ejecución ciclo 14-15).

> Ciclos que     10     2             Mult1            SI            Mult     f0    f2        f4           SI SI
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[simulacion-ciclo-a-ciclo-del-marcador-scoreboard-de-tomasulo]]
