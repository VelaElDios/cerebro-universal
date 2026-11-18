---
tipo: "concepto"
titulo: "Antidependencia entre iteraciones en bucle con store y actualización de puntero"
temas: ["ac", "bucles", "dependencias", "pipeline"]
claves: ["antidependencia", "WAR", "bucle", "store", "puntero", "iteraciones"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2019.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bucles]] · [[dependencias]] · [[pipeline]]

S.D usa R1 (lee) para la dirección de almacenamiento; DADDUI escribe R1 (actualiza puntero). En la misma iteración S.D lee antes de que DADDUI escriba → no hay hazard. Entre iteraciones: DADDUI de iteración i escribe R1, y S.D de iteración i+1 lee R1 → antidependencia (WAR) entre iteraciones. Respuesta correcta: c.

> Between the S.D and the DADDUI instructions... a) There is a data dependence in the same iteration b) There is an output dependence in the same iteration c) There is an antidependence between iterations d) None of the above
> — `repo:datos/temarios/AC/examenes/June2019.pdf`

Relacionado: [[clasificacion-de-dependencias-en-bucle-antidependencia-war-e]]
