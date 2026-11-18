---
tipo: "receta"
titulo: "Diagrama pipeline superscalar: ejecución fuera de orden con renombramiento y escritura fuera de orden"
temas: ["ac", "out-of-order", "out-of-order-write", "pipeline", "renombramiento", "superscalar", "tomasulo"]
claves: ["register renaming", "out-of-order write", "ROB", "reservation stations", "speculative execution"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[out-of-order]] · [[out-of-order-write]] · [[pipeline]] · [[renombramiento]] · [[superscalar]] · [[tomasulo]]

Con renombramiento ilimitado: eliminados peligros WAR/WAW (cada write usa registro físico nuevo). Escritura fuera de orden: instrucción escribe resultado en registro físico tan pronto termina ejecución (commit/retire puede ser en orden vía ROB, pero writeback físico es OoO). Decode: renombra registros destino → tags físicos. Execute: cuando operandos listos (tags resueltos) y unidad libre. Writeback: resultado en CDB → actualiza RS y registros físicos. Commit: en orden, vacía ROB. Máximo paralelismo: I1-I4 decode c1, exec c2 (si 5 UFs), write c3; I5-I7 decode c2, exec c3, write c4. Hazards solo RAW verdaderos y estructurales.

> c) Ejecución fuera de orden con renombramiento (suponiendo que hay suficientes registros para hacerlo) y escritura fuera de orden
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`

Relacionado: [[diagrama-pipeline-superscalar-grado-4-ejecucion-en-orden-y-e]] · [[diagrama-pipeline-superscalar-ejecucion-fuera-de-orden-sin-r]] · [[diferencias-clave-entre-los-tres-modelos-de-ejecucion-supers]]
