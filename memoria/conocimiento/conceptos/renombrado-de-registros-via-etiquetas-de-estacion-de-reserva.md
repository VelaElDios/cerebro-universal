---
tipo: "concepto"
titulo: "Renombrado de registros vía etiquetas de estación de reserva elimina WAR y WAW"
temas: ["ac", "arquitectura", "planificacion-dinamica", "renombrado-registros", "tomasulo"]
claves: ["renombrado", "etiquetas", "WAR", "WAW", "estación de reserva"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[planificacion-dinamica]] · [[renombrado-registros]] · [[tomasulo]]

Cuando una instrucción se emite, sus registros destino y fuente se renombran al identificador de la estación de reserva que la aloja. Así, dos escrituras al mismo registro arquitectónico van a estaciones distintas (evita WAW) y una lectura antigua captura el valor de su estación antes de que una escritura nueva la sobrescriba (evita WAR). Los riesgos RAW se resuelven monitorizando el CDB.

> Los identificadores de registros de las instrucciones emitidas y pendientes de ejecución se renombran al de la estación de reserva, ¡eliminando así riesgos WAR y WAW!
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`
