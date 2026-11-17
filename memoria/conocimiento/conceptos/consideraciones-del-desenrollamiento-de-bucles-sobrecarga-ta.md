---
tipo: "concepto"
titulo: "Consideraciones del desenrollamiento de bucles: sobrecarga, tamaño de código y presión de registros"
temas: ["ac", "loop-unrolling", "planificacion-estatica", "tradeoffs"]
claves: ["sobrecarga", "tamano-codigo", "fallos-cache", "escasez-registros", "prediccion-saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[loop-unrolling]] · [[planificacion-estatica]] · [[tradeoffs]]

Tres limitaciones principales: (1) Reducción de sobrecarga: más iteraciones desenrolladas amortizan el overhead del bucle, pero existe un límite práctico. (2) Incremento del tamaño de código: código más grande aumenta la tasa de fallos en caché de instrucciones. (3) Limitaciones del compilador / presión de registros: planificación agresiva requiere muchos registros (el ejemplo 4x usa 8 registros FP), pudiendo causar spilling. Alternativa mencionada: predicción de saltos (Tema 4) para reducir impacto de saltos sin desenrollar.

> Con un mayor número de iteraciones consideradas en el proceso de desenrollamiento se amortiza la sobrecarga, pero hay un límite en el número de iteraciones
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[desenrollamiento-de-bucles-4x-con-planificacion-para-elimina]]
