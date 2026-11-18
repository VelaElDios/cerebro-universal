---
tipo: "dato"
titulo: "Parámetros de temporización del ejercicio VLIW (examen enero 2018)"
temas: ["ac", "latencias", "parametros", "vliw"]
claves: ["MEM 2 ciclos carga/almacenamiento", "EX ADD.D 1 ciclo", "EX MUL.D 2 ciclos", "sin delayed branch", "4 ops/instrucción VLIW"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2018.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[latencias]] · [[parametros]] · [[vliw]]

Latencias exactas dadas en el enunciado: L.D y S.D → etapa MEM = 2 ciclos; ADD.D → etapa EX = 1 ciclo; MUL.D → etapa EX = 2 ciclos; DADDUI (entero) no se especifica, se asume 1 ciclo EX típico; BNEZ → sin salto retardado, penalización completa si no se predice. VLIW emite hasta 4 operaciones por ciclo sin restricciones de tipo por ALU.

> Consider the following timing parameters: 2 cycles for the MEM stage in loads and stores, 1 cycle for the EX stage of the ADD.D instruction, and 2 cycles for the EX stage of the MUL.D instruction. Delayed branch is not supported.
> — `repo:datos/temarios/AC/examenes/January2018.pdf` (cita sin comprobar)

Relacionado: [[planificacion-vliw-de-bucle-con-latencias-dadas-examen-ac-en]]
