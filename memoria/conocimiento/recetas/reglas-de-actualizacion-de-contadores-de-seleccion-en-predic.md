---
tipo: "receta"
titulo: "Reglas de actualización de contadores de selección en predictor híbrido de dos predictores locales"
temas: ["ac", "prediccion-saltos"]
claves: ["contador saturado 2 bits", "actualización selector", "predictor 1 bit", "predictor 3 bits"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[prediccion-saltos]]

Tabla de actualización del contador de 2 bits (selector) tras cada predicción de salto: si ambos predictores aciertan o ambos fallan → contador invariante; si Predictor 1 acierta y Predictor 2 falla → incrementar (+1, favorece Predictor 1); si Predictor 1 falla y Predictor 2 acierta → decrementar (-1, favorece Predictor 2). El contador es de saturación de 2 bits (valores 00,01,10,11). MSB=1 selecciona Predictor 1; MSB=0 selecciona Predictor 2.

> Tras cada predicción, además de actualizar ambos predictores, el contador correspondiente debe ser actualizado según la tabla siguiente: Comportamiento del Predictor 1 / Comportamiento del Predictor 2 / Acción sobre el contador: Acierto/Acierto → El contador no cambia; Acierto/Fallo → Incrementar el contador (+1); Fallo/Acierto → Decrementar el contador (-1); Fallo/Fallo → El contador no cambia.
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf` (cita sin comprobar)

Relacionado: [[bht-con-contadores-de-saturacion-de-2-bits-pregunta-17]] · [[predictor-hibrido-de-saltos-con-selectores-de-2-bits-entre-p]]
