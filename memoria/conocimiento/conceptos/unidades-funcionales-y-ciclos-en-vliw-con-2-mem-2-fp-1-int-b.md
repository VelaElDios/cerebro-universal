---
tipo: "concepto"
titulo: "Unidades funcionales y ciclos en VLIW con 2 mem, 2 FP, 1 int/branch por ciclo"
temas: ["ac", "ilp", "unidades-funcionales", "vliw"]
claves: ["Mem 1", "Mem 2", "FP 1", "FP 2", "integer/branch", "fully segmented", "jump delay ignored"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2023.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ilp]] · [[unidades-funcionales]] · [[vliw]]

El VLIW emite hasta 5 operaciones/ciclo: 2 memoria (carga/almacenamiento), 2 FP (add/mul/div), 1 entero/salto. "Fully segmented" = totalmente segmentadas (pipelined), pueden aceptar nueva operación cada ciclo. "Jump delay ignored" = el salto no introduce burbujas (branch delay slot = 0 o predicción perfecta). En la tabla dada (12 ciclos), contar ciclos donde cada tipo de unidad tiene operación no-NOP: Integer FU: ciclos 6, 10, 11, 12 → 4 ciclos. Adder FP FU: ciclos 7, 8 → 2 ciclos (ADD.D en FP1 y FP2). Multiplier FP FU: ciclos 3, 4 → 2 ciclos (MUL.D en FP1 y FP2). MEM stage: ciclos 1,2,3,4,11,12 → 6 ciclos (4 cargas + 2 stores por ciclo en ciclos 1-4, 2 stores en 11-12).

> Two memory operations, two FP operations, and one integer (or jump) can be issued in each cycle. All FP units are fully segmented. The jump delay is ignored
> — `repo:datos/temarios/AC/examenes/June2023.pdf` (cita sin comprobar)

Relacionado: [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]] · [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]]
