---
tipo: "concepto"
titulo: "Reorder buffer en Tomasulo (pregunta 19)"
temas: ["ac", "completacion-orden", "reorder-buffer", "tomasulo"]
claves: ["reorder buffer", "ROB", "resultados especulativos", "completación en orden", "información instrucciones ejecución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2021.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[completacion-orden]] · [[reorder-buffer]] · [[tomasulo]]

Respuesta correcta: b) Stores information related to the instructions in execution, and allows in-order completion. El ROB mantiene estado de instrucciones en vuelo (PC, destino, valor, estado) y garantiza confirmación en orden programa, permitiendo recuperación ante excepciones o fallos de predicción.

> The reorder buffer: a) Stores instruction results once they cease to be speculative. b) Stores information related to the instructions in execution, and allows in-order completion. c) Stores information related to the instructions that are completed in order. d) None of the above.
> — `repo:datos/temarios/AC/examenes/June2021.pdf`

Relacionado: [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[buffer-de-carga-en-tomasulo-especulativo-pregunta-18]] · [[reorder-buffer-rob-permite-completacion-en-orden-en-ejecucio]] · [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]]
