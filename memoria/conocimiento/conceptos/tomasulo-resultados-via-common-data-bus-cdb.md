---
tipo: "concepto"
titulo: "Tomasulo: resultados via Common Data Bus (CDB)"
temas: ["ac", "cdb", "tomasulo", "unidad funcional"]
claves: ["Tomasulo", "CDB", "bus de datos común", "resultados", "estaciones de reserva"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2014.pdf", "repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[cdb]] · [[tomasulo]] · [[unidad funcional]]

En el algoritmo de Tomasulo, el Common Data Bus (CDB) difunde los resultados de las unidades funcionales a todas las estaciones de reserva y al registro de estado, permitiendo que las instrucciones en espera capturen sus operandos (forwarding). La opción a) es correcta.

> En Tomasulo... Los resultados de las unidades funcionales pasan a las instrucciones que están a la espera a través del CDB
> — `repo:datos/temarios/AC/examenes/Enero2014.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[contenido-de-una-estacion-de-reserva-en-tomasulo]] · [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]] · [[bus-comun-de-datos-cdb-en-tomasulo-difunde-resultados-de-uf]]

## Ampliación (2026-11-18, )
En el algoritmo de Tomasulo, cuando una unidad funcional termina su ejecución, coloca el resultado en el Common Data Bus (CDB). Todas las estaciones de reserva y buffers de carga que esperan ese resultado (identificados por etiqueta/Q) lo capturan simultáneamente del CDB. Esto permite el bypassing/forwarding sin escribir en el banco de registros. Respuesta correcta: a) CDB.
