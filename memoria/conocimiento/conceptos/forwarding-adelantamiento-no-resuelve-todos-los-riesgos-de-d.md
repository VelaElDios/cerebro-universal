---
tipo: "concepto"
titulo: "Forwarding (adelantamiento) no resuelve todos los riesgos de datos en MIPS multiciclo"
temas: ["ac", "forwarding", "hazards", "mips", "pipeline"]
claves: ["adelantamiento", "forwarding", "unidad adelantamiento", "riesgos datos", "MIPS multiciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2014B.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[forwarding]] · [[hazards]] · [[mips]] · [[pipeline]]

El forwarding resuelve riesgos RAW de tipo EX→EX, MEM→EX, WB→EX, pero no resuelve: 1) Load-use hazard (LW seguido de instrucción que usa el dato → requiere 1 stall), 2) Riesgos de control (saltos), 3) Riesgos estructurales, 4) Dependencias WAR/WAW en in-order (no ocurren), pero en out-of-order sí requieren renombrado.

> Un MIPS multiciclo segmentado equipado con una unidad de adelantamiento c) No puede solucionar todas las situaciones de riesgo de datos
> — `repo:datos/temarios/AC/examenes/Noviembre2014B.pdf` (cita sin comprobar)
