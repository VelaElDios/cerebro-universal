---
tipo: "receta"
titulo: "Planificación estática agresiva para VLIW 4-issue con renombrado y fuera de orden"
temas: ["ac", "fuera-de-orden", "planificacion-estatica", "renombrado", "vliw"]
claves: ["VLIW", "4 operaciones/ciclo", "sin restricciones tipo", "renombrado registros", "reordenamiento"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[fuera-de-orden]] · [[planificacion-estatica]] · [[renombrado]] · [[vliw]]

Pasos para Procesador B: 1) Desenrollar 8 veces (igual que A). 2) Aplicar renombrado de registros agresivo para eliminar dependencias de nombre (WAR/WAW). 3) Reordenar instrucciones globalmente (fuera de orden) para saturar las 4 ranuras por ciclo respetando solo dependencias verdaderas (RAW) y latencias. 4) Al no haber restricciones de tipo, cualquier ranura puede tomar cualquier operación (entera, FP, memoria, salto). 5) La rama BNE puede planificarse con su slot de retardo o predicción. 6) Resultado: tabla con Cycle, Operation 1-4 mostrando mayor compacidad que en A.

> For Processor B, schedule the unrolled code, assuming that the static scheduling is as aggressive and efficient as possible to optimize the resulting code to the maximum. Renaming and out-of-order scheduling can be used.
> — `repo:datos/temarios/AC/examenes/June 2024.pdf`

Relacionado: [[procesador-b-vliw-4-issue-sin-restricciones-de-tipo-con-plan]] · [[tabla-de-latencias-para-instrucciones-consecutivas-en-mips64]]
