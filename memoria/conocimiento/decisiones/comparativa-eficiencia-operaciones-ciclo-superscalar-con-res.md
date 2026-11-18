---
tipo: "decision"
titulo: "Comparativa eficiencia operaciones/ciclo: superscalar con restricción de tipo vs VLIW sin restricción"
temas: ["ac", "pipeline", "saas"]
claves: ["operations per cycle", "efficiency", "superscalar vs VLIW", "type restriction"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[saas]]

**Métrica**: operaciones útiles emitidas por ciclo (throughput) en estado estacionario del bucle desenrollado 8×.
- **Processor A (superscalar)**: límite teórico 4 ops/ciclo, pero **partición fija 2 int + 2 FP**. El bucle tiene 8 ADD.D (FP) y 32 instrucciones enteras (8 L.D, 8 S.D, 8 DADDUI, 8 BNE). Cuello de botella FP: 8 ADD.D / 2 por ciclo = **mínimo 4 ciclos** para emitir todas las FP. En esos 4 ciclos se emiten 8 enteras (2/ciclo), quedando 24 enteras para ciclos adicionales → **mínimo 16 ciclos totales** (4 ciclos FP + 12 ciclos solo enteras a 2/ciclo). Throughput medio = 40 ops / 16 ciclos = **2.5 ops/ciclo**. Las latencias (RAW) pueden alargar esto.
- **Processor B (VLIW)**: 4 ops/ciclo **sin partición**. Puede emitir 4 L.D en un ciclo, 4 ADD.D en otro, etc. Con renombrado y reordenación agresiva, el límite son las latencias RAW y recurrencias (p.ej. cadena DADDUI→L.D siguiente). Si la recurrencia del puntero (DADDUI→L.D) permite 1 iteración/ciclo (latencia 0 con forwarding), se pueden emitir 5 ops/iteración × 8 iteraciones = 40 ops en ~8-10 ciclos → **4-5 ops/ciclo**.
**Conclusión esperada**: **Processor B (VLIW) logra mayor eficiencia** porque elimita la restricción artificial de 2 int + 2 FP y el compilador puede empaquetar operaciones de forma óptima. El superscalar desperdicia slots FP cuando no hay instrucciones FP listas (solo 8 ADD.D en todo el bucle) y slots enteros cuando las FP saturan.

> Compare the number of operations per cycle for each processor. Which processor gets the best efficiency in operations per cycle?
> — `repo:datos/temarios/AC/examenes/January2021.pdf`

Relacionado: [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]]
