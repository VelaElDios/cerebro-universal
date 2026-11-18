---
tipo: "receta"
titulo: "Reglas de actualización del contador selector de 2 bits en predictor híbrido"
temas: ["ac", "prediccion-saltos"]
claves: ["actualización contador selector", "hit/miss predictor 1", "hit/miss predictor 2", "saturación 2 bits"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Tras cada predicción, se actualiza el contador de 2 bits (saturante) según la combinación de acierto/fallo (Hit/Miss) de Predictor 1 y Predictor 2:
- P1 Hit, P2 Hit → contador sin cambios
- P1 Hit, P2 Miss → incrementar (+1, saturando a 11)
- P1 Miss, P2 Hit → decrementar (-1, saturando a 00)
- P1 Miss, P2 Miss → contador sin cambios
Esto hace que el selector favorezca al predictor que acierta más a menudo.

> After each prediction, apart from updating both predictors, the corresponding counter must be updated according to the next table: Predictor 1 behavior       Predictor 2 behavior Action on the counter Hit                        Hit                       The counter value does not change Hit                        Miss                      Increment the counter (+1) Miss                       Hit                       Decrement the counter (-1) Miss                       Miss                      The counter value does not change
> — `repo:datos/temarios/AC/examenes/June2017.pdf`

Relacionado: [[predictor-hibrido-con-selector-de-2-bits-entre-predictor-de]] · [[reglas-de-actualizacion-de-contadores-de-seleccion-en-predic]] · [[tabla-de-actualizacion-de-contadores-de-2-bits-saturados-par]] · [[reglas-de-actualizacion-del-selector-hibrido-de-2-bits]]
