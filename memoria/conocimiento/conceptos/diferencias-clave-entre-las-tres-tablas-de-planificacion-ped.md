---
tipo: "concepto"
titulo: "Diferencias clave entre las tres tablas de planificación pedidas (Scoreboard vs Tomasulo básico vs Tomasulo especulativo)"
temas: ["ac", "pipeline", "scoreboard", "tomasulo"]
claves: ["Issue", "Read operands", "Execution", "Write result", "Commit"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[scoreboard]] · [[tomasulo]]

Tres columnas de tabla distintas reflejan las fases de cada método: (1) Scoreboard: 4 fases - Issue (emisión, chequeo WAW y estructural), Read operands (espera RAW, lectura de registros), Execution (cálculo), Write result (chequeo WAR, escritura en registro). (2) Tomasulo básico: 3 fases - Issue (emisión, renombrado implícito vía RS, asignación RS/buffer), Execution (espera operandos por CDB, cálculo), Write result (broadcast por CDB, liberación RS). No hay fase Commit; escritura en registro arquitectónico en Write result. (3) Tomasulo especulativo: 4 fases - Issue (asigna entrada ROB + RS/buffer), Execution (igual), Write result (escribe en ROB, broadcast CDB), Commit (escritura en registro arquitectónico en orden, resolución excepciones). El ROB impone orden de commit y permite especulación/rollback.

> Instruction             Issue        Read operands         Execution     Write result / Instruction                Issue             Execution                  Write result / Instruction            Issue           Execution          Write result         Commit
> — `repo:datos/temarios/AC/examenes/June2021.pdf` (cita sin comprobar)

Relacionado: [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]]
