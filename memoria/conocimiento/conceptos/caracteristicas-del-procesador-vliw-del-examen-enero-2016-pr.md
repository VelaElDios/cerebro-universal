---
tipo: "concepto"
titulo: "Características del procesador VLIW del examen Enero 2016 Problema 3"
temas: ["ac", "adelantamiento", "planificacion", "salto-retardado", "vliw"]
claves: ["4 operaciones por instrucción", "sin restricciones tipo ALU", "salto retardado", "adelantamiento", "desenrollado 4 veces"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2016.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[adelantamiento]] · [[planificacion]] · [[salto-retardado]] · [[vliw]]

Procesador VLIW (Very Long Instruction Word) que emite 4 operaciones por ciclo/instrucción larga. No hay restricciones de tipo de operación por ALU (cualquier ALU puede ejecutar cualquier operación). Dispone de salto retardado (delayed branch) y adelantamiento (forwarding/bypassing) para resolver dependencias de datos.

> Se ejecuta este código en un procesador VLIW con 4 operaciones por instrucción que no impone restricciones al tipo de operaciones que pueden ser emitidas por cada ALU, con salto retardado y adelantamiento
> — `repo:datos/temarios/AC/examenes/Enero2016.pdf`

Relacionado: [[benchmarks-sinteticos-dhrystone-y-whetstone-proposito-y-orig]]
