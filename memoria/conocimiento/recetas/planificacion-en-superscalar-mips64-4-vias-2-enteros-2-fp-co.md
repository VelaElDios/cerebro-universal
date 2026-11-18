---
tipo: "receta"
titulo: "Planificación en superscalar MIPS64 4 vías (2 enteros + 2 FP) con branch delayed 2 slots"
temas: ["ac", "examen", "pipeline", "superscalar"]
claves: ["Processor A", "5-stage superscalar", "issue 4 per cycle", "2 integer 2 FP", "delayed branch 2 slots"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[examen]] · [[pipeline]] · [[superscalar]]

Restricciones de emisión: máx 2 instrucciones enteras + 2 FP por ciclo. Orden en programa dentro de cada tipo (in-order issue per type). Dependencias verdaderas (RAW) respetadas vía forwarding: resultado de L.D disponible tras 2 ciclos (fin MEM), ADD.D tras 1 ciclo (fin EX), MUL.D tras 3 ciclos (fin EX). S.D necesita dato listo en ciclo de emisión (store usa valor en etapa MEM). DADDUI enteras, 1 ciclo EX. BNEZ salto condicional con 2 delay slots: las 2 instrucciones inmediatamente posteriores al BNEZ en código estático se emiten en los 2 ciclos siguientes al salto (o mismo ciclo si caben) y se ejecutan siempre. Planificar minimizando burbujas: intercalar instrucciones de distintas iteraciones desenrolladas para ocultar latencias. Tabla de salida: Cycle | Integer | Integer | FP | FP.

> Processor A. 5-stage superscalar MIPS64, which can issue 4 instructions per cycle: two integer and two floating-point.
> — `repo:datos/temarios/AC/examenes/June2022.pdf`

Relacionado: [[desenrollado-4x-de-bucle-mips64-fp-con-renombrado-de-registr]] · [[procesador-a-superscalar-mips64-4-issue-2-enteros-2-fp]] · [[configuracion-de-pipeline-mips64-para-problema-de-examen-lat]] · [[planificacion-en-vliw-4-operaciones-sin-restricciones-de-tip]]
