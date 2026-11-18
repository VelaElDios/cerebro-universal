---
tipo: "concepto"
titulo: "Problemas del marcador (scoreboard) en planificación dinámica"
temas: ["ac", "arquitectura", "marcador", "planificacion-dinamica"]
claves: ["window size", "riesgos estructurales", "riesgos WAR", "riesgos WAW", "buses registros"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[marcador]] · [[planificacion-dinamica]]

El marcador (scoreboard) presenta cinco limitaciones principales: (1) su rendimiento depende del ILP disponible; (2) tiene un número reducido de entradas (window size), lo que limita cuántas instrucciones pueden emitirse simultáneamente; (3) sufre riesgos estructurales por necesitar muchas unidades funcionales; (4) requiere un número elevado de buses hacia el banco de registros; (5) no elimina los riesgos WAR (Write After Read) ni WAW (Write After Write), lo que frena el paralelismo.

> Problemas: Rendimiento en función del paralelismo a nivel de instrucción; Número reducido de entradas en el marcador (window size) – emisión de pocas instrucciones a la vez; Problemas con riesgos estructurales – necesidad de un gran número de unidades funcionales; Número de buses a registros elevado; Presencia de riesgos WAR y WAW
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[tecnica-de-marcador-scoreboard-riesgos-war-waw-obligan-a-det]] · [[estructura-del-marcador-scoreboard-en-arquitectura-de-comput]] · [[pasos-de-ejecucion-en-el-algoritmo-del-marcador-scoreboard]]
