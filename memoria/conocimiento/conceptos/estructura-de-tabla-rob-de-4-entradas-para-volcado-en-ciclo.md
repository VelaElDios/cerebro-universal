---
tipo: "concepto"
titulo: "Estructura de tabla ROB de 4 entradas para volcado en ciclo concreto (examen AC)"
temas: ["ac", "rob", "tomasulo"]
claves: ["Reorder Buffer", "ROB", "commit", "especulación", "estado"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[rob]] · [[tomasulo]]

Formato exacto de la tabla ROB que hay que rellenar en el examen (4 entradas, índices 0-3):
Columnas: Entry (0-3), Busy (yes/no), Instruction (texto completo), Status (ej. Issue, Execute, Write, Commit), Destination (registro destino, ej. F4, F6, F0...), Value (valor o tag, ej. #F4, M[10+R2], etc.).
Momento de captura: **el ciclo en que termina la ejecución del primer L.D. (instrucción 3)**. En ese ciclo, la instrucción 3 ya ha escrito resultado (o está en Write result), y las anteriores pueden estar en distintos estados. Las entradas posteriores a la 3 aún no han hecho issue (ROB de 4 entradas, así que la 4ª instrucción DIV.D puede haber hecho issue o no según ciclos).

> Complete the table below to display the contents of the ROB (which has only 4 entries), just in the same cycle in which the first L.D. instruction ends. Entry Busy Instruction Status Destination Value
> — `repo:datos/temarios/AC/examenes/January2022.pdf` (cita sin comprobar)

Relacionado: [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[algoritmo-tomasulo-origen-y-objetivo-cpi1]]
