---
tipo: "receta"
titulo: "Adelantamiento (forwarding) para riesgos RAW"
temas: ["ac", "adelantamiento", "forwarding", "pipeline", "raw"]
claves: ["resultado ALU a entrada ALU", "latches", "DSUB no necesita R1 en ciclo 3 sino en 4"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[adelantamiento]] · [[forwarding]] · [[pipeline]] · [[raw]]

El forwarding (adelantamiento) evita stalls en dependencias RAW ALU-ALU. Cuando el productor está en EX/MEM o MEM/WB, su resultado se enruta directamente a las entradas de la ALU del consumidor que está en EX. Ejemplo: DADD en EX produce resultado al final de EX; DSUB en ID necesita el operando en EX del ciclo siguiente → se forwarda desde latch EX/MEM a entrada ALU. También funciona para operandos de direcciones de load/store (ej. LD R4,0(R1) → SD R4,12(R1) forwarda R1 y R4 desde latches).

> Adelantamiento: es una técnica hardware para que cuando ocurre un riesgo por dependencia de datos, la lógica de control seleccione el resultado de la ALU como entrada a la misma ALU • DSUB no necesita R1 en el ciclo 3, sino en el 4 • El adelantamiento puede generalizarse para que cualquier unidad funcional pueda pasar un resultado directamente a la unidad funcional que lo necesite
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)

Relacionado: [[dependencia-de-datos-en-pipeline-riesgo-solo-si-instruccione]] · [[riesgo-load-use-en-pipeline-mips-con-forwarding]] · [[limitacion-del-adelantamiento-hazard-load-use-load-use-penal]]
