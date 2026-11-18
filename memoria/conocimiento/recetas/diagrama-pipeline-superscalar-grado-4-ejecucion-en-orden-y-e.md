---
tipo: "receta"
titulo: "Diagrama pipeline superscalar grado 4: ejecución en orden y escritura en orden"
temas: ["ac", "diagrama-temporizacion", "in-order", "pipeline", "superscalar"]
claves: ["superscalar grado 4", "5 unidades funcionales", "in-order execution", "in-order write", "decode/execute/write"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[diagrama-temporizacion]] · [[in-order]] · [[pipeline]] · [[superscalar]]

Restricciones: max 4 instr/ciclo en Decode, max 5 en Execute, max 4 en Write. Resultado disponible para dependientes al ciclo siguiente de Write. En orden estricto: I1 decode c1, exec c2, write c3 → I2 decode c2 (si no hay hazard estructural), pero RAW I2 necesita R1 de I1 → I2 exec earliest c4 (write I1 c3, disponible c4). Hazards estructurales: solo 4 decoders, 5 ALUs, 4 write ports. Llenar tabla ciclo a ciclo respetando orden de programa en las 3 etapas.

> a) Ejecución en orden y escritura en orden.
> — `repo:datos/temarios/AC/examenes/Enero2022.pdf`
