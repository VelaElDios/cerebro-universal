---
tipo: "concepto"
titulo: "En Tomasulo sin especulación la emisión se detiene ante riesgo WAW"
temas: ["ac", "emision", "tomasulo", "waw"]
claves: ["Tomasulo", "emisión", "WAW", "riesgo", "estación de reserva"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[emision]] · [[tomasulo]] · [[waw]]

Tomasulo evita riesgos RAW y WAR mediante renombrado implícito (estaciones de reserva y CDB). Sin embargo, los riesgos WAW (dos escrituras al mismo registro) requieren que la segunda instrucción espere a que la primera haya escrito su resultado (o se le asigne una estación de reserva distinta) para mantener el orden de escritura. Por eso la emisión se frena ante WAW.

> En la técnica de Tomasulo (sin especulación): c) La emisión de instrucciones se detiene si existe un riesgo WAW
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[buffers-de-carga-y-almacenamiento-en-tomasulo]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]]
