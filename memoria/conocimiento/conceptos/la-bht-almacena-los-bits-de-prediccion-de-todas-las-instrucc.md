---
tipo: "concepto"
titulo: "La BHT almacena los bits de predicción de todas las instrucciones de salto condicional"
temas: ["ac", "bht", "prediccion-saltos", "tabla-historial"]
claves: ["BHT", "bits de predicción", "salto condicional", "tabla"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bht]] · [[prediccion-saltos]] · [[tabla-historial]]

Branch History Table (BHT) es una tabla indexada por la dirección del salto (o parte de ella) que guarda contadores de saturación (p.ej. 2 bits) para predecir tomado/no tomado. No guarda direcciones destino (eso hace la BTB).

> La BHT almacena b) Los bits de predicción de todas las instrucciones de salto condicional
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf` (cita sin comprobar)

Relacionado: [[bht-branch-history-table-tabla-separada-para-bits-de-predicc]] · [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[implementacion-de-la-bht-en-predictor-dinamico-de-2-bits]] · [[seleccion-de-entrada-en-bht-branch-history-table]] · [[implementacion-bht-para-predictor-de-2-bits-4k-entradas-80-9]]
