---
tipo: "concepto"
titulo: "Métrica de comparación: operaciones por ciclo (IPC) en superscalar vs VLIW"
temas: ["ac", "ipc", "rendimiento", "superscalar", "vliw"]
claves: ["operaciones por ciclo", "IPC", "eficiencia", "speedup"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ipc]] · [[rendimiento]] · [[superscalar]] · [[vliw]]

La comparación final pide calcular el IPC (instrucciones/operaciones por ciclo) medio de cada planificación. El procesador que logre mayor IPC (más cerca de 4, el ancho de emisión) tiene mejor eficiencia. Factores: restricciones de tipo en A (2 int + 2 FP) vs libertad total en B; capacidad de reordenamiento estático en B vs emisión en orden en A; latencias idénticas en ambos. Se espera que B supere a A por flexibilidad.

> Compare the number of operations per cycle obtained for each processor. Which processor achieves the best efficiency in operations per cycle?
> — `repo:datos/temarios/AC/examenes/June 2024.pdf`

Relacionado: [[procesador-a-superscalar-mips64-4-issue-2-enteros-2-fp]] · [[procesador-b-vliw-4-issue-sin-restricciones-de-tipo-con-plan]]
