---
tipo: "receta"
titulo: "Cálculo de ciclos de penalización por salto tomado en pipeline 5 etapas con condición en EX y dirección en MEM"
temas: ["ac", "penalizacion-salto", "pipeline", "prediccion-saltos"]
claves: ["branch penalty", "EX stage", "MEM stage", "branch taken", "pipeline flush"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/June2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[penalizacion-salto]] · [[pipeline]] · [[prediccion-saltos]]

Pipeline clásico: IF, ID, EX, MEM, WB. Si condición en EX y dirección en MEM, el salto se resuelve al final de MEM. Instrucciones en IF, ID, EX siguientes al salto son erróneas → 3 ciclos de penalización (se vacían 3 etapas). Respuesta: c. 3 cycles.

> In a 5-stage pipeline, if the branch condition is checked at the EX stage and the branch target address is computed at the MEM stage, how many penalty cycles are introduced per jump taken?
> — `repo:datos/temarios/AC/examenes/June2025.pdf`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]] · [[actualizacion-de-la-btb-tras-ejecutar-el-salto]]
