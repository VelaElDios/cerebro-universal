---
tipo: "receta"
titulo: "Cómo rellenar tabla de ejecución con bits venenosos (casos R1=0 y R1=5)"
temas: ["ac", "pipeline"]
claves: ["L.D", "ADD.D", "BNEZ", "speculative", "poison bits", "exception"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]]

Para rellenar la tabla: 1) Identificar instrucciones especulativas (marcadas con *): L.D F2,0(R2) y ADD.D F6,F0,F2. 2) Evaluar cada caso según valor inicial de R1. Caso a) R1=0: BNEZ R1,jump no salta (R1==0), por tanto la instrucción especulativa ADD.D F6,F0,F2 se ejecuta pero su resultado no se confirma; la instrucción no especulativa ADD.D F6,F0,F4 sobrescribe F6. Caso b) R1=5: BNEZ salta a jump, por tanto la instrucción especulativa ADD.D F6,F0,F2 se confirma y la no especulativa no se ejecuta. 3) Marcar registros dirty cuando reciben valor especulativo. 4) Marcar Mem(Rx) prohibited si la dirección es inválida (R1=0 o R2=0 en caso a; R2=0 en caso b). 5) Excepción solo si se usa registro dirty o dirección prohibited en instrucción no especulativa (commit).

> Instructions marked with * are speculative. Fill in the execution table showing the values after each instruction for the following two cases: a) First case Initial State R1 0 R2 0 R3 8 F0 0 F2 0 F4 0 F6 0 Mem(R1) prohibited Mem(R2) prohibited Mem(R3) 1 b) Second case Initial State R1 5 R2 0 R3 7 F0 0 F2 0 F4 0 F6 0 Mem(R1) 1 Mem(R2) prohibited Mem(R3) 1
> — `repo:datos/temarios/AC/examenes/June2025.pdf` (cita sin comprobar)

Relacionado: [[planificacion-estatica-con-bits-venenosos-convencion-dirty-p]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]]
