---
tipo: "concepto"
titulo: "Planificación dinámica de instrucciones con Marcador (Scoreboard)"
temas: ["ac", "arquitectura-computadores", "planificacion-dinamica", "scoreboard"]
claves: ["Marcador", "Scoreboard", "emisión", "lectura operandos", "ejecución", "escritura resultado", "CDC6600", "fuera de orden"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[planificacion-dinamica]] · [[scoreboard]]

La planificación dinámica permite que las instrucciones se ejecuten fuera de orden siempre que el resultado final sea correcto. La etapa ID se divide en dos: Emisión (decodificar, comprobar riesgos estructurales) y Lectura de operandos (esperar hasta que no haya riesgos, leer operandos). Si una instrucción no puede avanzar, se detiene y dejan fluir a las siguientes. Las instrucciones se buscan en orden (IF) pero pueden ejecutarse fuera de orden.

> Comenzar a ejecutar una instrucción cuando los operandos estén disponibles
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[estructura-del-marcador-scoreboard-en-arquitectura-de-comput]] · [[pasos-de-ejecucion-en-el-algoritmo-del-marcador-scoreboard]] · [[planificacion-dinamica-orden-de-ejecucion-por-disponibilidad]]
