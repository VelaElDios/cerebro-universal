---
tipo: "dato"
titulo: "Latencias y grado de segmentación de UF FP en Problema 1"
temas: ["ac", "pipeline", "punto-flotante", "unidad-funcional"]
claves: ["fmul.d 5 ciclos EX", "fadd.d 4 ciclos EX", "totalmente segmentadas", "II=1"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2026.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[punto-flotante]] · [[unidad-funcional]]

Para el Problema 1: multiplicación FP (fmul.d) latencia 5 ciclos en EX, suma FP (fadd.d) latencia 4 ciclos en EX. Ambas totalmente segmentadas (Initiation Interval = 1). UF enteros (addi, cálculo dir) latencia 1 ciclo EX, II=1.

> la UF de multiplicación FP tiene 5 ciclos de ejecución en EX, la UF de suma FP tiene 4 ciclos de ejecución en EX y todas está completamente segmentadas
> — `repo:datos/temarios/AC/examenes/Junio2026.pdf`

Relacionado: [[ancho-y-tamano-en-bits-de-un-btb-implicito-con-1024-entradas]]
