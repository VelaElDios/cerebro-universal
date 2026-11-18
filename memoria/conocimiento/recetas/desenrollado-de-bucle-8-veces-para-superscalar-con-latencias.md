---
tipo: "receta"
titulo: "Desenrollado de bucle 8 veces para superscalar con latencias FP"
temas: ["ac", "loop-unrolling", "planificacion", "superscalar"]
claves: ["desenrollado 8x", "unrolling", "latencia 3", "latencia 2", "latencia 1", "emisión 2int+2FP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[loop-unrolling]] · [[planificacion]] · [[superscalar]]

Pasos para planificar en Procesador A: 1) Replicar el cuerpo del bucle 8 veces, renombrando registros (F2, F4, F6, R2, R4, R3) para evitar dependencias falsas (WAR/WAW). 2) Ordenar instrucciones ciclos a ciclos respetando: máx 2 enteras + 2 FP por ciclo; latencias: L.D→ALU PF (1), ALU PF→ALU PF (3), ALU PF→S.D (2); forwarding y ramas retrasadas (el salto BNE tiene slot de retardo). 3) Rellenar huecos con instrucciones de otras iteraciones. 4) La tabla de planificación muestra en cada ciclo: Instr.1, Instr.2 (enteras), Instr.3, Instr.4 (FP). Objetivo: maximizar IPC (instrucciones por ciclo).

> For Processor A, unroll the code 8 times and schedule it as compactly as possible, indicating the instructions issued in each cycle.
> — `repo:datos/temarios/AC/examenes/June 2024.pdf`

Relacionado: [[procesador-a-superscalar-mips64-4-issue-2-enteros-2-fp]] · [[tabla-de-latencias-para-instrucciones-consecutivas-en-mips64]]
