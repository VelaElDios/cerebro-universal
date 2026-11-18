---
tipo: "concepto"
titulo: "Bus Común de Datos (CDB) en Tomasulo difunde resultados de UF y memoria"
temas: ["ac", "bus comun datos", "cdb", "tomasulo"]
claves: ["CDB", "bus común datos", "Tomasulo", "resultados", "unidades funcionales", "memoria"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2014.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[bus comun datos]] · [[cdb]] · [[tomasulo]]

El CDB es un bus de broadcast: cuando una unidad funcional termina o una carga accede a memoria, el resultado (valor + etiqueta de estación de reserva/ROB) se pone en el CDB. Todas las estaciones de reserva y el ROB escuchan (snooping) para capturar operandos que esperan (coincidencia de etiqueta).

> El bus común de datos (CDB) usado en la técnica de Tomasulo... Es el bus donde se depositan los resultados de las unidades funcionales y de los accesos a memoria
> — `repo:datos/temarios/AC/examenes/Junio2014.pdf` (cita sin comprobar)

Relacionado: [[algoritmo-tomasulo-los-resultados-se-difunden-por-el-bus-com]] · [[buffer-de-carga-en-tomasulo-especulativo]]
