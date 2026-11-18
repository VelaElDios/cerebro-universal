---
tipo: "receta"
titulo: "Simulación de ejecución Tomasulo con tabla de ciclos (issue, execution, write, commit)"
temas: ["ac", "especulacion", "tomasulo"]
claves: ["tabla ciclos", "issue", "execution", "write", "commit", "motivo parada", "RAW", "estructural", "orden programa"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January 2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[tomasulo]]

Para cada instrucción de la secuencia (10 instrucciones: L.S, MUL.S, L.S, ADD.S, S.S, L.S, MUL.S, L.S, ADD.S, S.S) se rellena una fila con cuatro etapas: Issue (inicio-fin), Execution (inicio-fin), Write (inicio-fin), Commit (inicio-fin). Se indica el número de ciclo de inicio y fin de cada etapa. Si una etapa no puede empezar o se para, se anota el motivo: RAW (dependencia de datos), peligro estructural (ej. CDB ocupado, unidad funcional ocupada), orden de programa (ej. espera a que instrucción anterior haga issue), etc. La simulación debe respetar latencias y reglas de CDB/recursos.

> Details the execution of the following code. To do so, indicate in the table below the start and end cycle number for each step of each instruction and, where appropriate, the reason for stopping the execution of the step in question (a RAW hazard, a structural hazard, the order of the program, etc.).
> — `repo:datos/temarios/AC/examenes/January 2025.pdf`

Relacionado: [[procesador-tomasulo-con-especulacion-caracteristicas-de-late]] · [[pasos-para-completar-tabla-de-ejecucion-tomasulo-issue-execu]] · [[rellenar-tabla-de-ejecucion-tomasulo-columnas-issue-executio]] · [[simulacion-de-algoritmo-tomasulo-basico-y-especulativo-con-r]]
