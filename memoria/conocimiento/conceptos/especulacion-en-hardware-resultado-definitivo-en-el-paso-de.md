---
tipo: "concepto"
titulo: "Especulación en hardware: resultado definitivo en el paso de commit"
temas: ["ac", "commit", "especulacion-hardware", "rob"]
claves: ["especulacion hardware", "ROB", "commit", "resultado definitivo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[commit]] · [[especulacion-hardware]] · [[rob]]

En especulación con hardware (p. ej., reorder buffer ROB), las instrucciones ejecutan fuera de orden y escriben resultados temporales en el ROB; solo al llegar al head del ROB y hacer commit (en orden de programa) el resultado se vuelve arquitectónicamente visible (se escribe en registro/memoria). Antes del commit, una mala predicción permite descartar resultados simplemente vaciando entradas del ROB.

> In hardware speculation: c) The result of an instruction is definitive when the instruction reaches its commit step
> — `repo:datos/temarios/AC/examenes/January2019.pdf` (cita sin comprobar)

Relacionado: [[actualizacion-de-la-btb-tras-ejecutar-el-salto]] · [[excepcion-en-especulacion-hardware-atendida-solo-en-etapa-co]] · [[paso-de-commit-en-tomasulo-especulativo-usa-rob-para-complet]] · [[como-rellenar-la-tabla-de-estado-en-tomasulo-con-especulacio]]
