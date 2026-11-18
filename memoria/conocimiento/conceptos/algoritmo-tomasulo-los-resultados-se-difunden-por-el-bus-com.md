---
tipo: "concepto"
titulo: "Algoritmo Tomasulo: los resultados se difunden por el Bus Común de Datos (CDB)"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["Tomasulo", "CDB", "bus común de datos", "estaciones de reserva"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2013.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

En el algoritmo de Tomasulo, las unidades funcionales escriben sus resultados en el Bus Común de Datos (CDB). Las estaciones de reserva que esperan esos operandos (identificados por sus etiquetas Qj/Qk) capturan el valor del CDB cuando la etiqueta coincide, permitiendo el reenvío directo sin pasar por el banco de registros.

> En Tomasulo... a. Los resultados de las unidades funcionales pasan a las instrucciones que están a la espera a través del CDB
> — `repo:datos/temarios/AC/examenes/Junio2013.pdf`

Relacionado: [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]] · [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]]
