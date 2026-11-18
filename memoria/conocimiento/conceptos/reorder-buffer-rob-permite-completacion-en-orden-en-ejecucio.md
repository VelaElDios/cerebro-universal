---
tipo: "concepto"
titulo: "Reorder Buffer (ROB): permite completación en orden en ejecución fuera de orden"
temas: ["ac", "especulacion", "rob", "tomasulo"]
claves: ["ROB", "Reorder Buffer", "completación en orden", "especulación"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2018.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulacion]] · [[rob]] · [[tomasulo]]

El ROB es una cola circular que mantiene las instrucciones en orden de programa. Almacena información de instrucciones en ejecución (estado, destino, valor, excepción) y fuerza la completación (commit) en orden de programa, permitiendo ejecución fuera de orden pero retire in-order. Esto da soporte a especulación y manejo preciso de excepciones. Respuesta correcta: b) Almacena información de las instrucciones en ejecución y permite que se completen en orden.

> El Reorder Buffer: a) Almacena los resultados de las instrucciones una vez que éstas dejan de ser especulativas b) Almacena información de las instrucciones en ejecución y permite que se completen en orden c) Almacena información de las instrucciones que se ejecutan en orden d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Junio2018.pdf`

Relacionado: [[buffer-de-reordenamiento-rob-en-tomasulo-con-especulacion-ca]] · [[bits-venenosos-en-especulacion-excepcion-no-recuperable-marc]]
