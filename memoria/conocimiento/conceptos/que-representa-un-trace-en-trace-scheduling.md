---
tipo: "concepto"
titulo: "Qué representa un trace en trace scheduling"
temas: ["ac", "pipeline", "vliw"]
claves: ["trace scheduling", "trace", "VLIW", "bloque básico"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2024.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[vliw]]

En trace scheduling, un trace representa la secuencia más probable de instrucciones a ejecutar (most likely sequence). Se usa en compiladores para VLIW/EPIC: se selecciona un camino frecuente en el grafo de flujo de control, se programa como si fuera secuencial y se añaden instrucciones de compensación en las entradas/salidas laterales.

> In the trace scheduling technique, what does a trace represent? a) Most likely sequence of instructions to execute b) Sequence of instructions to execute in a loop iteration c) Basic block within a loop d) All are false
> — `repo:datos/temarios/AC/examenes/January2024.pdf`

Relacionado: [[criterio-de-desenrollamiento-de-bucles-loop-unrolling]] · [[configuracion-vliw-de-6-unidades-funcionales-con-latencias-a]]
