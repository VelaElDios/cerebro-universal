---
tipo: "dato"
titulo: "Parámetros de temporización del examen AC June 2022 Exercise 4"
temas: ["ac", "examen", "latencias", "pipeline"]
claves: ["MEM 2 cycles", "ADD.D 1 cycle", "MUL.D 3 cycles", "delayed branch 2 slots", "fully pipelined"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[latencias]] · [[pipeline]]

Latencias funcionales (ciclos hasta que resultado disponible para forwarding): L.D / S.D -> etapa MEM = 2 ciclos. ADD.D -> etapa EX = 1 ciclo. MUL.D -> etapa EX = 3 ciclos. Todas las unidades totalmente en tubería (nueva operación cada ciclo). Branch delayed: 2 delay slots (las 2 instrucciones siguientes al salto se ejecutan siempre). Data forwarding asumido. 32 registros FP de 64 bits.

> We assume the following timing parameters: 2 cycles for the MEM stage in loads and stores, 1 cycle to complete the EX stage of ADD.D instructions, and 3 cycles to complete the EX stage of the MUL.D instruction.
> — `repo:datos/temarios/AC/examenes/June2022.pdf`

Relacionado: [[desenrollado-4x-de-bucle-mips64-fp-con-renombrado-de-registr]] · [[planificacion-en-vliw-4-operaciones-sin-restricciones-de-tip]]
