---
tipo: "concepto"
titulo: "Dependencia de datos no siempre causa hazard; depende de distancia en pipeline"
temas: ["ac", "dependencias", "hazards", "pipeline"]
claves: ["dependencia datos", "hazard", "riesgo", "pipeline", "segmentado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Noviembre2014B.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[dependencias]] · [[hazards]] · [[pipeline]]

Una dependencia (RAW, WAR, WAW) solo genera hazard (riesgo) si las instrucciones están lo suficientemente cerca en el pipeline para que sus etapas se solapen en conflicto. Si hay suficiente distancia (instrucciones intermedias), el forwarding o el orden natural resuelven sin parada.

> La existencia de una dependencia de datos entre dos instrucciones ejecutadas en un procesador segmentado: b) Puede provocar un riesgo de datos si las instrucciones están suficientemente cerca
> — `repo:datos/temarios/AC/examenes/Noviembre2014B.pdf` (cita sin comprobar)

Relacionado: [[antidependencia-siempre-genera-hazard-war-en-pipeline-in-ord]]
