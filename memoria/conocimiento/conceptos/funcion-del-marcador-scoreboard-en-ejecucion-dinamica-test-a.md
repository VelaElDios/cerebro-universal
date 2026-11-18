---
tipo: "concepto"
titulo: "Función del Marcador (Scoreboard) en ejecución dinámica (test AC Q9)"
temas: ["ac", "ejecucion-dinamica", "scoreboard", "tomasulo"]
claves: ["marcador", "scoreboard", "riesgo-estructural", "riesgo-datos", "emision-orden"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ejecucion-dinamica]] · [[scoreboard]] · [[tomasulo]]

El **Marcador (Scoreboard)** (CDC 6600) permite **emisión en orden pero ejecución fuera de orden**. Su objetivo principal: **evitar que una instrucción detenida por un riesgo (estructural o de datos) bloquee a las siguientes instrucciones independientes**. Mantiene una tabla de estado de unidades funcionales y registros para saber cuándo los operandos están listos y la UF libre, y entonces emite la instrucción a ejecución. No renombra registros (no elimina WAR/WAW), solo evita paradas innecesarias.

> La técnica de Marcador se usa para… Evitar la detención de instrucciones que no dependen de una instrucción detenida
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf` (cita sin comprobar)
