---
tipo: "concepto"
titulo: "Restricción de CDB en Tomasulo: no escritura e inicio simultáneos"
temas: ["ac", "pipeline", "tomasulo"]
claves: ["CDB", "bus datos común", "restricción ciclo", "escritura e inicio ejecución"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2012.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[pipeline]] · [[tomasulo]]

Restricción importante de temporización en el CDB: cuando un resultado se escribe en el bus (broadcast), las estaciones de reserva que esperan ese dato (Qj/Qk coincidente) no pueden comenzar su ejecución en ese mismo ciclo. Deben esperar al ciclo siguiente. Esto añade 1 ciclo de latencia efectiva en las dependencias RAW resueltas vía forwarding por CDB frente al modelo ideal donde escritura e inicio son simultáneos.

> se supone que en el mismo ciclo de reloj no se puede escribir un dato en este bus e iniciar la ejecución de una operación que estuviera esperando ese dato
> — `repo:datos/temarios/AC/examenes/Junio2012.pdf`

Relacionado: [[bus-comun-de-datos-cdb-en-el-algoritmo-de-tomasulo]] · [[campos-qj-y-qk-en-estaciones-de-reserva-de-tomasulo]]
