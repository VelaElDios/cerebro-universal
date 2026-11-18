---
tipo: "concepto"
titulo: "Técnicas ILP estáticas vs dinámicas (pregunta 7 y 9)"
temas: ["ac", "ilp", "planificacion"]
claves: ["ILP estático", "ILP dinámico", "compilador", "hardware", "reordenamiento"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ilp]] · [[planificacion]]

ILP estático (pregunta 7): depende principalmente del compilador (respuesta c). El compilador reordena instrucciones, hace desenrollado de bucles, predicción estática, etc. ILP dinámico (pregunta 9): el hardware reordena instrucciones en tiempo de ejecución para reducir dependencias (respuesta c). La especulación (d) es una técnica complementaria, pero la definición central de planificación dinámica es el reordenamiento por hardware (Tomasulo, Scoreboard, ROB).

> In dynamic code scheduling: a) Compiler reorders program instructions to reduce dependences b) Compiler predicts branch instructions to reduce dependences c) Hardware reorders program instructions to reduce dependences d) Hardware speculates the execution of instructions to reduce dependences
> — `repo:datos/temarios/AC/examenes/January2017.pdf`
