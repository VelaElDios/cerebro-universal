---
tipo: "receta"
titulo: "Planificación en superescalar grado 2 con/sin renombramiento"
temas: ["ac", "pipeline", "superscalar"]
claves: ["superescalar grado 2", "emisión en orden", "ejecución fuera de orden", "renombramiento de registros", "adelantamiento", "ventana de instrucciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]]

Modelo: Superescalar grado 2 (emite hasta 2 instr/ciclo). Etapas: IF, ID, EX (2 ciclos aritmética), MEM (2 ciclos carga), WB. Adelantamiento (forwarding) disponible.
Código (7 instr): LW R2, DADD R4, DSUB R6, LW R5, DSUB R9, DADD R8, DSUB R5.
Dependencias clave (RAW):
- R2: LW(1) → DADD(2), DADD(6), DSUB(7)
- R5: LW(4) → DSUB(7) ; también DADD(2) lee R5 viejo, DSUB(7) escribe R5 nuevo (WAW en R5)
- R8: DSUB(3) → DADD(6) ; DADD(6) escribe R8 (WAW en R8)
- R9: DSUB(5) lee y escribe R9 (WAR consigo misma? No, misma instr)
a) **En orden (in-order issue, in-order exec, in-order commit)**: Emite 2/ciclo en orden. Si dependencia RAW no resuelta por forwarding, stall en ID. EX 2 ciclos, MEM 2 ciclos (loads). Dibujar diagrama de Gantt ciclo a ciclo.
b) **Fuera de orden sin renombramiento (OOO issue/exec, in-order commit, sin renombrar)**: Ventana grande. Emite en orden pero puede ejecutar fuera de orden cuando operandos listos y UF libre. **Peligro**: WAR/WAW reales frenan emisión/ejecución porque no hay renombramiento. Aquí: WAW en R5 (instr 2 y 7) y R8 (instr 3 y 6) obligan a serializar. WAR en R5 (instr 4 carga R5, instr 7 usa R5 viejo? No, instr 7 lee R5 nuevo de instr 4 y R2; instr 2 lee R5 viejo → WAR entre 2 y 4 si 4 ejecuta antes que 2 lea). Sin renombramiento, hay que respetar orden de escritura/lectura arquitectónico.
c) **Fuera de orden con renombramiento (OOO issue/exec/commit, renombramiento completo)**: Registros arquitectónicos → físicos. Elimina WAR/WAW. Emite 2/ciclo, renombra destinos, despacha a RS cuando operandos listos. Ejecuta en cuanto UF libre. Commit en orden (ROB). Máximo paralelismo.
Para resolver: hacer tabla ciclo × etapa × instr, marcar cuándo empieza/termina EX, MEM, WB, y cuándo se hace forwarding.

> se ejecuta en un superescalar de grado 2, capaz de emitir cualquier tipo de instrucción por ciclo. El procesador invierte 2 ciclos para la etapa MEM en las cargas y 2 ciclos para completar la etapa EX de las operaciones aritméticas. Además, implementa adelantamiento.
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[bucle-de-calculo-y-i-a-x-i-2-en-ensamblador-mips64]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
