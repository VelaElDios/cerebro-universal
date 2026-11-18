---
tipo: "receta"
titulo: "Desenrollado de bucle mínimo para eliminar todos los stalls en pipeline MIPS64 con FP"
temas: ["ac", "floating-point", "loop-unrolling", "mips64", "optimization", "pipeline"]
claves: ["loop unrolling", "desenrollado", "stalls", "FP latency", "register renaming"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[floating-point]] · [[loop-unrolling]] · [[mips64]] · [[optimization]] · [[pipeline]]

Factor de desenrollado mínimo = ceil(CPR_original / latencia_mínima_teórica). Para este código: latencias FP add=2, mul=4. Camino crítico: L.S → SUB.S (stall 1) → MUL.S (stall 1) → S.S (stall 3) = 6 ciclos de stalls + 7 instrucciones ≈ 13 ciclos/iteración. Teórico sin stalls: 7 instrucciones, pero limitado por FP multiplier (4 ciclos EX) y no 2 WB FP/ciclo. Desenrollar N veces: replicar cuerpo N veces con registros distintos (F0,F4,F8...; R1,R3 avanzan 4*N bytes). N mínimo tal que: 1) No hay dependencias entre instrucciones de distinta iteración desenrollada. 2) Se llenan huecos de stalls con instrucciones de otras iteraciones. 3) Se respeta límite 1 WB FP/ciclo. Típicamente N=4 para este patrón (4 FP ops: load, add, mul, store) permite intercalar y saturar pipeline. Código resultante: 11 instrucciones mostradas en examen (4 loads, 4 adds, 4 muls, 4 stores, 2 address updates, 1 branch) → 19 instrucciones para 4 resultados → CPR ≈ 19/4 ≈ 4.75 ciclos/resultado.

> c) Indicate the code obtained after applying the loop unrolling technique the minimum number of times to avoid all stalls:
> — `repo:datos/temarios/AC/examenes/June2020.pdf`

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[como-calcular-stalls-en-pipeline-mips64-con-operand-forwardi]]
