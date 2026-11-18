---
tipo: "receta"
titulo: "Simulación Scoreboard vs Tomasulo básico: pasos de ejecución y ciclos"
temas: ["ac", "planificacion-dinamica", "scoreboard", "tomasulo"]
claves: ["Scoreboard", "Tomasulo", "CDB", "reservation stations", "issue/read/exec/write"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[planificacion-dinamica]] · [[scoreboard]] · [[tomasulo]]

Código: ADD.D F0,F2,F4; L.D F2,12(R2); SUB.D F6,F0,F2; MUL.D F4,F3,F2; ADD.D F6,F4,F6; S.D F4,10(R2). Latencias: L.D/S.D exec=1, ADD.D/SUB.D=2, MUL.D=5. Scoreboard: etapas Issue, Read operands, Execution, Write result. Tomasulo: Issue, Execute (espera operandos en RS), Write result (CDB). Diferencia clave: Tomasulo renombra en Issue (Qj/Qk), emite a RS aunque operandos no listos; Scoreboard espera en Read operands. Simular ciclo a ciclo respetando: resultado en CDB no usable hasta ciclo siguiente; recurso liberado no reutilizable hasta ciclo siguiente.

> Detail the execution of the code below, assuming the Scoreboard algorithm. For this, indicate in the following table the names of the execution steps and the cycle number in which each step is completed for each instruction. ... Detail the execution of the same code, but assuming now the basic version of the Tomasulo’s algorithm (without speculation).
> — `repo:datos/temarios/AC/examenes/June2018.pdf` (cita sin comprobar)

Relacionado: [[comparativa-tomasulo-vs-marcador-scoreboard]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[algoritmo-de-marcador-scoreboard-pasos-de-simulacion-para-ej]] · [[simulacion-ciclo-a-ciclo-del-marcador-scoreboard-de-tomasulo]] · [[diferencias-clave-entre-las-tres-tablas-de-planificacion-ped]]
