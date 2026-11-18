---
tipo: "receta"
titulo: "Cálculo de speedup VLIW vs MIPS64 segmentado considerando mejor planificación"
temas: ["ac", "ilp", "rendimiento", "speedup", "vliw"]
claves: ["speedup", "ciclos por iteración", "II", "initiation interval", "best performance", "lowest stalls"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ilp]] · [[rendimiento]] · [[speedup]] · [[vliw]]

Speedup = (Ciclos MIPS64 por iteración en estado estable) / (Ciclos VLIW por iteración en estado estable). VLIW: tabla dada tiene 12 ciclos para 4 resultados (4 elementos procesados: F2,F8,F14,F20 → stores en ciclos 11-12). Iteración VLIW = 12 ciclos / 4 resultados = 3 ciclos/resultado. MIPS64 segmentado (apartado b): determinar II (intervalo de iniciación) mínimo sin hazards. Con latencias load=1, mul=4, add=3, store=1 y forwarding, el camino crítico: load → mul (4) → add (3) → store. Dependencia load-use: 1 ciclo. MUL→ADD: 4 ciclos. ADD→STORE: 3 ciclos. II mínimo = max(1,4,3) = 4 ciclos/resultado si no hay recursos duplicados. Pero MIPS64 tiene 1 FP adder, 1 FP multiplier → II=4. Speedup = 4 / 3 = 1.33x. Si MIPS64 tiene múltiples unidades FP, II podría ser 1. Explicar cálculo detallado.

> What is the speedup obtained by the VLIW processor with respect to the code in section b) of the segmented MIPS64 processor? Explain the calculations made and consider that the code is scheduled to obtain the best performance (i.e. the lowest number of stalls).
> — `repo:datos/temarios/AC/examenes/June2023.pdf`

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]]
