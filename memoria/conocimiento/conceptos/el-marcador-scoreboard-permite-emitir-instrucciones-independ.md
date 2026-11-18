---
tipo: "concepto"
titulo: "El Marcador (Scoreboard) permite emitir instrucciones independientes mientras una espera"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["Marcador", "Scoreboard", "emisión fuera de orden", "planificación hardware"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2014A.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

El Scoreboard (Marcador) es una técnica de planificación dinámica en hardware que monitoriza dependencias y estado de unidades funcionales. Si una instrucción se detiene por hazard (RAW, estructural), el Scoreboard sigue emitiendo instrucciones posteriores que no tienen dependencias con la detenida, logrando ejecución fuera de orden (out-of-order issue).

> ¿En qué técnica de planificación hardware cuando una instrucción no se emite, se pueden emitir otras instrucciones que no dependen de ella? c) Marcador
> — `repo:datos/temarios/AC/examenes/Noviembre2014A.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]]
