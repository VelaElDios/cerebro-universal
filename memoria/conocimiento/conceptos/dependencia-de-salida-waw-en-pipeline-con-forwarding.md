---
tipo: "concepto"
titulo: "Dependencia de salida (WAW) en pipeline con forwarding"
temas: ["ac", "dependencias", "forwarding", "pipeline", "waw"]
claves: ["WAW", "dependencia de salida", "forwarding", "registro destino"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2020.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[forwarding]] · [[pipeline]] · [[waw]]

I1 y I2 escriben en F4 → dependencia de salida (WAW, Write After Write). Con forwarding y unidad FP de 2 ciclos, I1 escribe en WB tras 2 ciclos EX; I2 entra en EX en ciclo siguiente a I1 (si no hay parada). Como ambas escriben F4, hay WAW. El forwarding resuelve RAW, no WAW. En pipeline básico in-order, WAW se evita porque las escrituras ocurren en orden en WB; pero si la latencia difiere, puede haber conflicto. La opción correcta es b).

> ADD.S F4, F4, F0 ;I1 ADD.S F4, F2, F2 ;I2 SD.S F4, 0(R2) ;I3 The FP addition functional unit employs 2 cycles. We can say that: a) There is a stall between I1 and I2 through F4 b) There is an output dependence between I1 and I2 through F4 c) There is an output dependence between I2 and I3 through F4 d) None of the above
> — `repo:datos/temarios/AC/examenes/January2020.pdf`

Relacionado: [[dependencias-en-fragmento-de-codigo-fp-mips-l-d-add-s-add-s]] · [[dependencia-de-salida-waw-y-antidependencia-war-definiciones]] · [[analisis-de-dependencias-entre-instrucciones-de-punto-flotan]]
