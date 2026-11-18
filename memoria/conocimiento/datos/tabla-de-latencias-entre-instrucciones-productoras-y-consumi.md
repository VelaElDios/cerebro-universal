---
tipo: "dato"
titulo: "Tabla de latencias entre instrucciones productoras y consumidoras (AC June 2018)"
temas: ["ac", "data-hazards", "latencies", "pipeline"]
claves: ["ALU FP", "S.D", "L.D", "latency cycles"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[data-hazards]] · [[latencies]] · [[pipeline]]

Latencias en ciclos (número de ciclos que debe esperar el consumidor tras la emisión del productor): ALU FP → ALU FP = 3 (p.ej. MUL.D→ADD.D o ADD.D→ADD.D), ALU FP → S.D = 2 (resultado FP listo para almacenar), L.D → ALU FP = 1 (dato cargado listo para operación FP), L.D → S.D = 0 (carga y almacenamiento pueden ir en ciclos consecutivos sin espera). Estas latencias determinan la planificación para evitar hazards de datos.

> Instruction producing the result         Instruction using the result    Latency in cycles               ALU FP                                   ALU FP                            3               ALU FP                                   S.D                               2               L.D                                      ALU FP                            1               L.D                                      S.D                               0
> — `repo:datos/temarios/AC/examenes/June2018.pdf`
