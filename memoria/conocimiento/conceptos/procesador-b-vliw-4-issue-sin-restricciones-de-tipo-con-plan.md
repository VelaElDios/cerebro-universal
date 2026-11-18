---
tipo: "concepto"
titulo: "Procesador B: VLIW 4-issue sin restricciones de tipo con planificación estática agresiva"
temas: ["ac", "planificacion-estatica", "vliw"]
claves: ["VLIW", "4-issue", "planificación estática", "renombrado", "fuera de orden"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[planificacion-estatica]] · [[vliw]]

Procesador VLIW (Very Long Instruction Word) que emite 4 operaciones por ciclo sin restricciones de tipo (cualquier mezcla de enteras, FP, memoria, salto). La planificación es estática (en tiempo de compilación) pero se permite renombrado de registros y planificación fuera de orden (out-of-order scheduling) para optimizar al máximo el código. El compilador reordena instrucciones del bucle desenrollado para minimizar stalls respetando dependencias y latencias.

> Processor B. VLIW that can issue four operations per instruction in each cycle and does not impose restrictions on the types of operations that can be issued.
> — `repo:datos/temarios/AC/examenes/June 2024.pdf`
