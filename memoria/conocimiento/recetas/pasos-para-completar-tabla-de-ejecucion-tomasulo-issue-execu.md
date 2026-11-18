---
tipo: "receta"
titulo: "Pasos para completar tabla de ejecución Tomasulo (Issue, Execution, Writing, Commit)"
temas: ["ac", "tomasulo"]
claves: ["Issue", "Execution", "Writing result", "Commit", "RAW", "structural hazard", "program order", "CDB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[tomasulo]]

Para cada instrucción (L.D F0,0(R1); L.D F2,0(R2); ADD.D F6,F0,F2; S.D F6,0(R3)) rellenar cuatro columnas: Issue (ciclo inicio-fin), Execution (ciclo inicio-fin), Writing (ciclo inicio-fin), Commit (ciclo). Reglas: 1) Issue en orden de programa, una por ciclo si hay entrada libre en ROB y estación/buffer correspondiente. 2) Execution empieza cuando operandos disponibles (RAW resuelto) y unidad funcional libre; dura latencia fija (load/store 1, FP add 2, FP mul 4). 3) Writing (escritura en CDB) al terminar Execution si CDB libre; si ocupado, espera (structural hazard). 4) Commit en orden de programa, cuando instrucción está en cabeza de ROB y Writing completado; libera recursos. 5) Anotar causa de parada: RAW (esperar operando), structural hazard (unidad/CDB ocupada), program order (esperar instrucciones anteriores en Issue/Commit).

> Detail the execution of the code shown in the table, assuming that no exceptions occur. Indicate the start and end cycle numbers for each of the steps of each instruction and, where applicable, the reason for stopping the execution of the step in question (a RAW, a structural hazard, the order of the program, etc.).
> — `repo:datos/temarios/AC/examenes/June2025.pdf`

Relacionado: [[parametros-de-recursos-y-latencias-para-tomasulo-con-especul]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]] · [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]]
