---
tipo: "receta"
titulo: "Funcionamiento y actualización de la BTAC (Branch Target Address Cache)"
temas: ["ac", "arquitectura", "btac", "prediccion-saltos"]
claves: ["BTAC", "actualización", "salto tomado", "salto no tomado", "tag", "dirección destino"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[btac]] · [[prediccion-saltos]]

Acceso: en fase de captura, se indexa la BTAC con la dirección del salto. Hit + predicción "tomado" → se usa la dirección destino guardada. Actualización en ejecución: si salto fue tomado y no estaba en BTAC → se inserta (tag + dirección destino + bit tomado=1); si ya estaba → se actualiza dirección destino. Si salto fue no tomado y estaba en BTAC → se elimina la entrada. La BTAC solo guarda saltos tomados.

> Cuando se accede a una instrucción de salto se accede simultáneamente a la BTAC usando la dirección de la instrucción de salto si la instrucción está en la BTAC y el salto se predice como tomado, la dirección destino del salto se obtiene de la BTAC Se actualiza cuando se ejecuta la instrucción de salto y se conoce si el salto fue tomado o no y la dirección destino del salto
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[implementacion-de-btb-generica-ampliacion-de-btac-con-bits-d]] · [[comportamiento-de-la-btb-en-caso-de-acierto-test-ac-q14]]
