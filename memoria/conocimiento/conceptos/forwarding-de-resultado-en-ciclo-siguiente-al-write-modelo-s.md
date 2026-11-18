---
tipo: "concepto"
titulo: "Forwarding de resultado en ciclo siguiente al Write (modelo superscalar examen)"
temas: ["ac", "forwarding", "pipeline", "superscalar"]
claves: ["result available", "next cycle", "write stage", "RAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[forwarding]] · [[pipeline]] · [[superscalar]]

Regla de forwarding para el Ejercicio 3: si una instrucción está en etapa **Write en ciclo N**, su resultado puede ser leído por una instrucción en etapa **Execute en ciclo N+1** (no en N). Esto implica una latencia efectiva de **2 ciclos** entre Execute del productor y Execute del consumidor (Execute productor en N-1 → Write en N → Execute consumidor en N+1). En la tabla de ciclos, esto se ve como: I1 Execute en c2, Write en c3 → I2 (que necesita R1) Execute en c4 como mínimo.

> The result of an instruction is available to other instructions at the next cycle in which that result is written.
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[configuracion-superscalar-4-issue-para-diagramas-de-pipeline]]
