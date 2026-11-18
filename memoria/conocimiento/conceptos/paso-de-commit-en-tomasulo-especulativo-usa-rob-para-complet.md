---
tipo: "concepto"
titulo: "Paso de commit en Tomasulo especulativo usa ROB para completación en orden de programa"
temas: ["ac", "commit", "rob", "tomasulo"]
claves: ["commit", "ROB", "orden programa", "Tomasulo especulativo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[commit]] · [[rob]] · [[tomasulo]]

En la versión especulativa de Tomasulo, el Reorder Buffer (ROB) garantiza que las instrucciones se completen (commit) en el orden original del programa. En el paso de commit, si la instrucción es un salto, se actualiza el registro destino o memoria; si es una instrucción normal, se confirma el resultado. Las excepciones se manejan en commit.

> In the commit step of the speculative version of Tomasulo… The ROB is employed to complete the execution of instructions according to the program order
> — `repo:datos/temarios/AC/examenes/January2022.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffer-de-carga-en-tomasulo-especulativo]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]]
