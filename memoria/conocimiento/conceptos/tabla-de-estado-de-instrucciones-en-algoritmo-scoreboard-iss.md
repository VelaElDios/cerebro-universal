---
tipo: "concepto"
titulo: "Tabla de estado de instrucciones en algoritmo Scoreboard (Issue, Read operands, Execution Start-End, Write result)"
temas: ["ac", "dynamic-scheduling", "instruction-status", "mips64", "scoreboard"]
claves: ["Scoreboard", "Issue", "Read operands", "Execution Start", "Execution End", "Write result", "structural hazards", "WAR/WAW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2020.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dynamic-scheduling]] · [[instruction-status]] · [[mips64]] · [[scoreboard]]

Scoreboard (Marcador) rastrea 4 fases por instrucción: 1) Issue: decodifica, chequea hazards estructurales (FU libre) y WAW (registro destino libre). Si hay hazard → espera. 2) Read operands: espera hasta que no hay RAW (operandos disponibles, sin WAR pendiente). 3) Execution: ocupa FU; Start = ciclo donde empieza EX, End = Start + latencia_EX - 1. Si hazard durante EX (ej. FU ocupado por otra instrucción que empezó antes), se para y reanuda en siguiente ciclo tras resolver (+1). 4) Write result: espera hasta que no hay WAR (ninguna instrucción pendiente de leer ese registro) y puerto WB libre. Reglas clave del enunciado: FUs fully pipelined; IF/ID/MEM/WB = 1 ciclo; EX: L.D/S.D=1, ADD.D/SUB.D=2, MUL.D=4; recurso liberado en ciclo C no usable hasta C+1; 10 FUs add, 5 FUs mul.

> Complete the following instruction status table, indicating the cycle number in which each step is performed, for the code shown and according to the Scoreboard algorithm. You must complete the rows corresponding to the 6 instructions not detailed. Instruction Issue Read operands Execution Start - End Write result
> — `repo:datos/temarios/AC/examenes/June2020.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]]
