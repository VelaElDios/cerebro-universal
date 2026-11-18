---
tipo: "receta"
titulo: "Planificación en superescalar grado 2: en orden, fuera de orden sin renombramiento, fuera de orden con renombramiento"
temas: ["ac", "pipeline", "saas"]
claves: ["superescalar grado 2", "emisión en orden", "emisión fuera de orden", "renombramiento de registros", "ventana instrucciones", "adelantamiento"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2015.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[saas]]

Código: 1 LW R1,0(R0)  2 DADD R3,R5,R2  3 DSUB R6,R7,R4  4 LW R2,0(R10)  5 DSUB R9,R9,R2  6 DADD R4,R4,R5  7 DSUB R2,R2,R5. Latencias: IF/ID/IS 1 ciclo, EX (ALU) 3 ciclos, MEM (LW) 2 ciclos, WB 1 ciclo. Adelantamiento (forwarding) disponible. Ventana grande (todas las instrucciones visibles). a) En orden: emitir 2 por ciclo en orden de programa, respetando dependencias RAW (esperar en ID/IS hasta operandos listos), hazards estructurales (2 ALU, 1 MEM?). b) Fuera de orden sin renombramiento: emisión fuera de orden pero registros arquitectónicos; hazards WAR/WAW impiden reordenamiento que los viole (stall). c) Fuera de orden con renombramiento: registro renombrado elimina WAR/WAW; solo RAW limita. Mostrar diagrama de Gantt o tabla ciclos vs instrucciones con etapas.

> Muestra una planificación de instrucciones para los siguientes casos: a) Ejecución en orden b) Ejecución fuera de orden, sin capacidad de renombramiento. c) Ejecución fuera de orden, con capacidad de renombramiento.
> — `repo:datos/temarios/AC/examenes/Junio2015.pdf`

Relacionado: [[banco-de-registros-en-pipeline-mips-se-accede-en-etapas-id-y]] · [[antidependencia-war-en-bucle-entre-carga-y-actualizacion-de]] · [[antidependencia-entre-iteraciones-en-bucle-con-store-y-actua]]
