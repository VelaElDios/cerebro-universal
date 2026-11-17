---
tipo: "concepto"
titulo: "Definición de latencia e intervalo de iniciación en pipeline"
temas: ["ac", "segmentacion", "terminologia"]
claves: ["latencia", "intervalo de iniciación", "initiation interval"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[segmentacion]] · [[terminologia]]

Dos métricas clave para caracterizar unidades funcionales segmentadas. La latencia mide el retardo real de dato (productor→consumidor); el intervalo de iniciación mide el throughput máximo (cada cuántos ciclos se puede lanzar una nueva operación). En unidades totalmente segmentadas, intervalo = 1; en el divisor FP, intervalo (25) > latencia (24) porque no está segmentada.

> •    Latencia: número de ciclos entre la instrucción que produce un resultado y una instrucción que lo usa   •    Tiempo de iniciación: número de ciclos que deben pasar entre la emisión de dos operaciones del mismo tipo
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf`

Relacionado: [[tabla-de-latencia-e-intervalo-de-iniciacion-por-unidad-funci]]
