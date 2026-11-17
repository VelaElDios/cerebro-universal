---
tipo: "concepto"
titulo: "Estructuras de datos del Marcador (Scoreboard)"
temas: ["ac", "arquitectura-computadores", "estructuras-datos", "scoreboard"]
claves: ["Estado instrucciones", "Estado unidades funcionales", "Estado registros resultado", "Bloque 1", "Bloque 2", "Bloque 3"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[estructuras-datos]] · [[scoreboard]]

Tres bloques de datos: 1) Estado de instrucciones: indica en cuál de los 4 pasos está cada instrucción (Emisión, Lectura Operandos, Ejecución completa, Escritura resultado). 2) Estado de unidades funcionales: para cada UF guarda: Nº UF, Nombre, Ocupada (SI/NO), Op (operación), Fi (registro destino), Fj/Fk (registros fuentes), Qj/Qk (UF que producen los registros fuentes), Rj/Rk (flags indicando si Fj/Fk están listos y no se han leído). 3) Estado de registros resultado: indica qué UF escribirá en cada registro si una instrucción activa tiene ese registro como destino.

> Estructuras de datos mantenidas por el marcador: Bloque 1: estado de las instrucciones, Bloque 2: estado de las unidades funcionales, Bloque 3: estado de registros resultado
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[pasos-de-ejecucion-en-el-algoritmo-del-marcador-scoreboard]]
