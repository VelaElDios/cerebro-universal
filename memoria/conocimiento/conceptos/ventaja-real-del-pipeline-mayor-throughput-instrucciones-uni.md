---
tipo: "concepto"
titulo: "Ventaja real del pipeline: mayor throughput (instrucciones/unidad tiempo)"
temas: ["ac", "pipeline", "segmentación"]
claves: ["pipeline", "cauce segmentado", "throughput", "instrucciones por ciclo", "IPC"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[pipeline]] · [[segmentación]]

El pipeline no reduce la latencia de una instrucción individual (a veces la aumenta por overhead de registros de etapa), pero solapa etapas de distintas instrucciones, aumentando el ancho de banda (throughput) y reduciendo el CPI medio ideal a 1.

> Frente al cauce no segmentado de un procesador, el cauce segmentado siempre: b) Aumenta el número de instrucciones ejecutadas por unidad de tiempo
> — `repo:datos/temarios/AC/examenes/Enero2012.pdf` (cita sin comprobar)

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[definicion-y-proposito-de-la-segmentacion-pipeline]] · [[speedup-ideal-vs-real-en-pipeline-y-formula-con-detenciones]] · [[funcionamiento-y-limites-de-la-segmentacion-pipelining-en-si]]
