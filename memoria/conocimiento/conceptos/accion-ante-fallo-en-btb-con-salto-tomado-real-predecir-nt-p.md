---
tipo: "concepto"
titulo: "Acción ante fallo en BTB con salto tomado real: predecir NT, penalizar y actualizar"
temas: ["ac", "btb", "fallo-btb", "prediccion-saltos"]
claves: ["BTB", "fallo", "miss", "salto tomado", "actualización BTB", "penalización"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2026.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[btb]] · [[fallo-btb]] · [[prediccion-saltos]]

Si la instrucción no está en la BTB (miss), no hay predicción de dirección ni de taken/NT. La política por defecto es predecir "No Tomado" (secuencial). Cuando el salto se resuelve y resulta tomado, se incurre en penalización (flush pipeline) y se inserta la entrada en la BTB con la dirección objetivo y predicción taken.

> ¿Qué acción realiza el procesador si se utiliza una BTB (Branch Target Buffer) y se produce un "fallo" en la BTB y la instrucción es realmente un salto que resulta TOMADO? b. Se predice el salto como No Tomado, se detecta el error posteriormente, se penaliza y se actualiza la BTB añadiendo la instrucción.
> — `repo:datos/temarios/AC/examenes/Enero2026.pdf` (cita sin comprobar)

Relacionado: [[btb-branch-target-buffer-fusion-de-btac-y-bits-de-prediccion]] · [[actualizacion-de-la-btb-tras-ejecutar-el-salto]]
