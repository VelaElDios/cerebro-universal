---
tipo: "concepto"
titulo: "Contador saturante de 3 bits en estado 111 indica tres tomas reales consecutivas"
temas: ["ac", "branch predictor", "predicción saltos", "saturating counter"]
claves: ["3-bit predictor", "saturating counter", "111", "taken", "not taken"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June 2024.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[branch predictor]] · [[predicción saltos]] · [[saturating counter]]

Un contador saturante de n bits representa la confianza en que el salto se toma. Estado 111 (máximo para 3 bits) significa "fuertemente tomado". Solo se llega a ese estado tras varias tomas reales consecutivas (cada taken incrementa el contador hasta saturarlo). Por tanto, 111 implica que las tres últimas ejecuciones reales del salto fueron TAKEN. No indica la predicción previa (opción b) ni comportamiento not taken (opción a).

> A 3-bit predictor is updated to 111 after predicting a branch instruction. Then, we can state that… c) The actual behavior of the three last branch instructions was TAKEN.
> — `repo:datos/temarios/AC/examenes/June 2024.pdf` (cita sin comprobar)

Relacionado: [[btb-con-predictores-de-4-bits-campos-de-cada-entrada]] · [[comportamiento-de-la-btb-en-caso-de-acierto-test-ac-q14]]
