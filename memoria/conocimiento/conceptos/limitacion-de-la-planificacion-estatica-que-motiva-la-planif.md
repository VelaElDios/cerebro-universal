---
tipo: "concepto"
titulo: "Limitación de la planificación estática que motiva la planificación dinámica"
temas: ["ac", "emision-en-orden", "marcador", "planificacion-dinamica", "tomasulo"]
claves: ["planificación dinámica", "emisión en orden", "marcador", "Tomasulo", "unidad funcional libre", "instrucción parada"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[emision-en-orden]] · [[marcador]] · [[planificacion-dinamica]] · [[tomasulo]]

La planificación estática (compilador) emite instrucciones en orden programa. En tiempo de ejecución, si una instrucción se bloquea (p.ej. cache miss, dependencia de datos no resuelta), todo el pipeline se atasca aunque haya instrucciones independientes listas y unidades funcionales libres. La planificación dinámica (hardware: marcador / scoreboard o algoritmo Tomasulo) permite emisión fuera de orden (out-of-order): instrucciones posteriores independientes avanzan mientras las anteriores esperan, maximizando uso de unidades funcionales.

> Principal limitación de las técnicas de planificación estática: Emisión en orden de las instrucciones. Si una instrucción i queda parada, ninguna instrucción j posterior puede continuar, aun cuando j sea independiente de las que están en ejecución, y la unidad funcional que j necesita esté libre
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[planificacion-dinamica-tomasulo-orden-de-ejecucion-por-dispo]] · [[planificacion-dinamica-orden-de-ejecucion-por-disponibilidad]] · [[planificacion-dinamica-sin-especulacion-emision-en-orden-eje]]
