---
tipo: "concepto"
titulo: "Riesgos de datos en RISC-V: RAW, WAW, WAR"
temas: ["ac", "hazard datos", "pipeline", "raw", "war", "waw"]
claves: ["read after write", "write after write", "write after read", "RISC-V sin unidades multiciclo", "lecturas ID escrituras WB"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[hazard datos]] · [[pipeline]] · [[raw]] · [[war]] · [[waw]]

En RISC-V de 5 etapas sin unidades multiciclo:
- RAW (Read After Write): **sí ocurre**. El consumidor lee en ID antes de que el productor escriba en WB. Requiere forwarding o stall.
- WAW (Write After Write): **no ocurre** porque solo WB escribe y las instrucciones llegan a WB en orden de programa.
- WAR (Write After Read): **no ocurre** porque todas las lecturas son en ID (temprano) y todas las escrituras en WB (tardío).
- RAR (Read After Read): no es hazard.

> RAW (read after write): una instrucción posterior trata de leer un operando antes de que lo escriba una instrucción anterior • WAW (write after write): una escritura posterior se produce antes que otra escritura anterior en el mismo destino – esto sólo es posible si varias etapas del cauce pueden volcar sus resultados, luego en RISC-V sin unidades multiciclo no se van a producir estos riesgos • WAR (write after read): una instrucción posterior trata de escribir su resultado antes de que lo haya leído una instrucción anterior – esto no puede pasar en RISC-V, pues todas las lecturas se hacen en la etapa ID y todas las escrituras en la posterior WB
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)
