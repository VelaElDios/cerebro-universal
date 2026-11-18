---
tipo: "dato"
titulo: "Código VLIW bucle original examen enero 2023: 4 slots, 7 instrucciones con NOPs"
temas: ["ac", "pipeline", "vliw"]
claves: ["VLIW", "L.D", "DADDUI", "MUL.D", "ADD.D", "BNEZ", "S.D", "NOP", "delayed branch", "forwarding"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[vliw]]

Bucle VLIW original de 7 ciclos de instrucción (Instruction 1 a 7) para un procesador de 4 slots (ancho de issue 4). Cada fila muestra las 4 operaciones emitidas en paralelo (slot 1 a 4). El código ya está compactado al máximo según el enunciado. Incluye cargas (L.D), aritmética entera (DADDUI), multiplicación FP (MUL.D), suma FP (ADD.D), salto condicional retardado (BNEZ) y almacenamiento (S.D). Los NOPs indican slots vacíos por dependencias o falta de instrucciones independientes.

> Instruction 1 L.D F1, 0(R1) L.D F2, 0(R2) DADDUI R1, R1, #8 DADDUI R2, R2, #8 loop Instruction 2 NOP NOP NOP NOP Instruction 3 DADDUI R4, R4, #-1 NOP NOP NOP Instruction 4 NOP MUL.D F3, F1, F2 NOP NOP Instruction 5 NOP NOP NOP NOP Instruction 6 ADD.D F4, F1, F3 BNEZ R4, loop NOP NOP Instruction 7 S.D F4, -8(R1) NOP NOP NOP
> — `repo:datos/temarios/AC/examenes/January2023.pdf`

Relacionado: [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]] · [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]] · [[como-desenrollar-4-veces-y-planificar-bucle-vliw-para-maximo]] · [[codigo-del-bucle-a-planificar-en-vliw-examen-ac-enero-2017]] · [[planificacion-scheduling-de-bucle-en-vliw-con-forwarding-y-d]]
