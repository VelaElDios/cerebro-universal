---
tipo: "decision"
titulo: "Desenrollado de bucles: replicar mientras se reduzcan detenciones (stalls)"
temas: ["ac", "desenrollado", "ilp", "optimizacion"]
claves: ["desenrollado", "bucle", "replicar", "detenciones", "stalls", "límite"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[desenrollado]] · [[ilp]] · [[optimizacion]]

No hay un número fijo (como el contador del bucle) ni se desenrolla indefinidamente. El criterio óptimo es replicar el cuerpo del bucle tantas veces como reduzca los ciclos de parada (stalls) por hazards de control y datos, hasta que el overhead de código y presión de registros supere el beneficio.

> En la técnica de desenrollamiento de bucles, ¿cuántas veces debe replicarse el cuerpo del bucle? Mientras se siga reduciendo el número de detenciones
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf` (cita sin comprobar)

Relacionado: [[analisis-de-dependencias-en-bucle-con-add-d-y-s-d-misma-iter]] · [[bucle-vectorial-de-referencia-para-desenrollado-y-planificac]]
