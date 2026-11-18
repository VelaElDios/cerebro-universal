---
tipo: "concepto"
titulo: "Qué es un bloque básico (basic block) en ILP"
temas: ["ac", "basic block", "ilp"]
claves: ["basic block", "secuencia sin saltos", "instrucciones consecutivas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[basic block]] · [[ilp]]

Un bloque básico es una secuencia de instrucciones consecutivas sin instrucciones de salto (ni condicionales ni incondicionales) en su interior; solo la última instrucción puede ser un salto. Es la unidad natural para optimizaciones locales y para la predicción de salto (el predictor decide si se toma el salto al final del bloque).

> In Instruction-Level Parallelism, the 'basic block' expression refers to… b) A code sequence without branch instructions.
> — `repo:datos/temarios/AC/examenes/January2018.pdf` (cita sin comprobar)
