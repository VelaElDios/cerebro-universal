---
tipo: "concepto"
titulo: "Procesador A: Superscalar MIPS64 4-issue (2 enteros + 2 FP)"
temas: ["ac", "pipeline", "superscalar"]
claves: ["superscalar", "4-issue", "MIPS64", "unidades funcionales", "forwarding", "ramas retrasadas"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[superscalar]]

Procesador superscalar de 5 etapas, emisión en orden (in-order) de hasta 4 instrucciones/ciclo: 2 enteras (incluyen accesos memoria y saltos) y 2 de punto flotante. Tiene forwarding y ramas retrasadas (delayed branches). Todas las unidades funcionales están totalmente segmentadas (fully pipelined). Para planificar el bucle desenrollado 8 veces, hay que respetar las latencias de la tabla y las restricciones de emisión (máx 2 int + 2 FP por ciclo).

> Processor A. Superscalar MIPS64 with 5 stages, which can launch 4 instructions per cycle: two integer (including memory accesses and branches) and two floating-point.
> — `repo:datos/temarios/AC/examenes/June 2024.pdf`
