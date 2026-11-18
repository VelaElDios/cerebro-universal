---
tipo: "receta"
titulo: "Conversión de código VLIW compactado a bucle MIPS64 segmentado con un resultado por iteración"
temas: ["ac", "mips64", "pipeline", "software-pipelining", "vliw"]
claves: ["software pipelining", "prologue", "kernel", "epilogue", "desenrollado", "latencias FP"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[mips64]] · [[pipeline]] · [[software-pipelining]] · [[vliw]]

El VLIW ejecuta 4 elementos por iteración (F2,F8,F14,F20 → F4,F10,F16,F22 → F6,F12,F18,F24). Para MIPS64 segmentado con un resultado por vuelta (software pipelining): 1) Identificar latencias: load=1 (pero uso en ciclo siguiente por forwarding), MUL.D=4, ADD.D=3, store=1. 2) Desenrollar para ocultar latencias: iniciar cargas temprano, encadenar MUL→ADD→STORE. 3) Código kernel (ciclo estable): cada iteración produce 4 resultados (o 1 si se serializa). Dado "at each turn of the loop a result is calculated", se busca iniciar una nueva iteración cada ciclo (II=1). Requiere ≥4 registros rotatorios o renombrado. Esquema típico: Ciclo 1: L.D F2,0(R1); Ciclo 2: L.D F4,8(R1); Ciclo 3: L.D F6,16(R1); Ciclo 4: MUL.D F8,F2,F0; Ciclo 5: MUL.D F10,F4,F0; Ciclo 6: MUL.D F16,F14,F0; Ciclo 7: ADD.D F6,F8,F6; ... con adelantamiento de cargas de iteración siguiente. Rellenar tabla de 15 instrucciones mostrando prologue, kernel, epilogue.

> Show the initial code for the MIPS64 processor segmented such that at each turn of the loop a result is calculated. Write the code in this table (use as many rows as you need)
> — `repo:datos/temarios/AC/examenes/June2023.pdf`

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[como-desenrollar-4-veces-y-planificar-bucle-vliw-para-maximo]] · [[desenrollamiento-de-bucle-3x-y-re-planificacion-en-vliw-para]] · [[segmentacion-software-software-pipelining-para-bucle-encript]]
