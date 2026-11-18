---
tipo: "receta"
titulo: "Cómo calcular stalls en pipeline MIPS64 con operand forwarding y latencias FP conocidas"
temas: ["ac", "floating-point", "forwarding", "mips64", "pipeline", "stalls"]
claves: ["L.S", "SUB.S", "MUL.S", "S.S", "DADDUI", "BNE", "FP Adder/Subtractor 2 ciclos", "FP Multiplier 4 ciclos", "WB flotante e entero mismo ciclo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2020.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[floating-point]] · [[forwarding]] · [[mips64]] · [[pipeline]] · [[stalls]]

Para calcular stalls entre instrucciones consecutivas en este pipeline MIPS64: 1) Identificar dependencias RAW (registro destino → registro fuente). 2) Saber latencia de cada unidad funcional: FP add/sub=2 ciclos EX, FP mul=4 ciclos EX, integer=1 ciclo EX. 3) Con operand forwarding, el resultado está disponible al final de EX del productor. 4) El consumidor necesita el dato en su etapa EX. 5) Si productor termina EX en ciclo C, consumidor puede empezar EX en C+1 (forwarding). 6) Restricción: no dos WB flotantes en mismo ciclo; sí un WB flotante + uno entero. 7) Saltos resueltos en ID → no hay penalty si delayed branch. 8) Ejemplo: L.S (load FP, 1 ciclo EX+MEM) → SUB.S (FP add, 2 ciclos EX): L.S WB en ciclo 4, SUB.S EX empieza ciclo 3 → stall 1 ciclo para alinear WB. SUB.S (2 ciclos EX) → MUL.S (4 ciclos EX): SUB.S WB ciclo 6, MUL.S EX empieza ciclo 5 → stall 1 ciclo. MUL.S (4 ciclos EX) → S.S (store FP, 1 ciclo EX): MUL.S WB ciclo 10, S.S EX necesita dato → stall 3 ciclos. DADDUI (integer, 1 ciclo EX) → DADDUI: sin stalls (forwarding integer). DADDUI → BNE: resuelto en ID, delayed branch → 0 stalls.

> Operand forwarding is supported • A value can be written and read from a register in the same clock cycle • All the dependences are detected and solved in the ID stage • Branches are completely solved in the ID stage • Delayed branch is supported • In the same cycle two floating-point WB operations are not allowed • In the same cycle it is possible to perform a floating-point WB and a integer WB • All the functional units are pipelined • The next table shows the number of cycles employed by each functional unit: FP Adder/Subtractor 2, FP Multiplier 4, FP Divider 8, Rest of units 1
> — `repo:datos/temarios/AC/examenes/June2020.pdf` (cita sin comprobar)

Relacionado: [[ancho-y-tamano-en-bits-de-un-btb-implicito-con-1024-entradas]] · [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[configuracion-de-pipeline-mips64-para-problema-de-examen-lat]] · [[tabla-de-latencias-para-instrucciones-consecutivas-en-mips64]] · [[analisis-de-stalls-en-bucle-mips64-con-forwarding-y-ramas-re]]
