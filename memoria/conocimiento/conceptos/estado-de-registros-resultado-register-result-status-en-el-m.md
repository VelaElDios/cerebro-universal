---
tipo: "concepto"
titulo: "Estado de registros resultado (register result status) en el marcador"
temas: ["ac", "registro-estado-resultado", "renombrado", "scoreboard", "tomasulo"]
claves: ["f0 f2 f4 f6 f8 f10 f12", "UF que escribe", "register result status"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[registro-estado-resultado]] · [[renombrado]] · [[scoreboard]] · [[tomasulo]]

La tabla "Estado de registros resultado" indica qué unidad funcional (por número) escribirá el valor final de cada registro arquitectónico. En ciclo 10: f0←Mult1(2), f6←Entera(1) y luego Suma(4), f8←Suma(4), f10←Divide(5). f2 y f4 no tienen UF asignada (valores iniciales ya en registro). f12 sin asignar. Esto permite a las instrucciones en espera (Qj/Qk) saber qué UF producirá el operando que necesitan.

> Estado de registros resultado                                        f0          f2            f4           f6          f8        f10       f12                          UF             2                                                 4          5
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[simulacion-ciclo-a-ciclo-del-marcador-scoreboard-de-tomasulo]]
