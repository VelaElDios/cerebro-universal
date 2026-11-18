---
tipo: "concepto"
titulo: "Definiciones clave: basic block, antidependencia, loop unrolling, planificación estática, software pipelining, Scoreboard, Tomasulo CDB, predicción saltos (preguntas 7-15)"
temas: ["ac", "ilp", "pipeline", "planificacion", "prediccion-saltos", "scoreboard", "tomasulo"]
claves: ["basic block", "antidependencia", "WAR hazard", "loop unrolling", "planificación estática", "software pipelining", "Scoreboard", "hazard estructural", "CDB", "Tomasulo", "fallo predicción", "instrucciones predicadas", "BHT"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ilp]] · [[pipeline]] · [[planificacion]] · [[prediccion-saltos]] · [[scoreboard]] · [[tomasulo]]

Respuestas correctas: 7)b) A code sequence without branch instructions. 8)c) WAR hazard (antidependencia = WAR). 9)d) None (unrolling aumenta código, reduce control dependences pero no WAW). 10)c) Compiler reorders the code to reduce dependences. 11)d) None (software pipelining solapa iteraciones, no simplifica compilador). 12)b) Structural hazards handled in issue step. 13)a) CDB = bus donde unidades funcionales envían resultados. 14)a) CDB. 15)c) Resultados especulativos se descartan, programa reanuda camino correcto.

> In instruction-level parallelism, the “basic block” term refers to: a) A sequence of branch instructions b) A code sequence without branch instructions c) A code sequence without dependences between instructions d) None of the above
> — `repo:datos/temarios/AC/examenes/June2021.pdf`

Relacionado: [[tipos-de-dependencias-y-hazards-en-codigo-mips64-de-punto-fl]] · [[definicion-de-bloque-basico-en-paralelismo-a-nivel-de-instru]] · [[que-es-un-bloque-basico-basic-block-en-ilp]] · [[tecnicas-ilp-estaticas-vs-dinamicas-pregunta-7-y-9]]
