---
tipo: "dato"
titulo: "Secuencia de 10 instrucciones para simulación Tomasulo Problema 3"
temas: ["ac", "fp-code", "mips64", "tomasulo"]
claves: ["L.S F1 0(R2)", "MUL.S F1 F1 F0", "L.S F2 4(R2)", "ADD.S F2 F1 F2", "S.S F2 8(R2)", "L.S F1 4(R2)", "MUL.S F1 F1 F0", "L.S F2 8(R2)", "ADD.S F2 F1 F2", "S.S F2 12(R2)"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[fp-code]] · [[mips64]] · [[tomasulo]]

Código a simular. Dos "iteraciones" de un patrón: Cargar F1, Mul F1*F0, Cargar F2, Add F1+F2, Store F2. Segunda iteración usa offsets +4, +8, +12 y recarga F1, F2. Dependencias RAW: MUL.S(1) -> ADD.S(1) (F1), L.S(2) -> ADD.S(1) (F2), ADD.S(1) -> S.S(1) (F2), MUL.S(2) -> ADD.S(2) (F1), L.S(4) -> ADD.S(2) (F2). Dependencias WAW: MUL.S(1) y MUL.S(2) escriben F1. L.S(1) y L.S(3) escriben F1. L.S(2) y L.S(4) escriben F2. ADD.S(1) y ADD.S(2) escriben F2. Tomasulo/ROB renombra via ROB entries.

> L.S F1, 0(R2); MUL.S F1, F1, F0; L.S F2, 4(R2); ADD.S F2, F1, F2; S.S F2, 8(R2); L.S F1, 4(R2); MUL.S F1, F1, F0; L.S F2, 8(R2); ADD.S F2, F1, F2; S.S F2, 12(R2)
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf` (cita sin comprobar)
