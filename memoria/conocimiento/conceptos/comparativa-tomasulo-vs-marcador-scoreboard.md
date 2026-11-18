---
tipo: "concepto"
titulo: "Comparativa Tomasulo vs Marcador (Scoreboard)"
temas: ["ac", "marcador", "planificacion-dinamica", "tomasulo"]
claves: ["unidades funcionales segmentadas", "ventana instrucciones", "riesgo estructural", "WAR", "WAW", "resultados a unidades funcionales", "escribe lee registros", "control estacion reserva", "control central marcador"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[marcador]] · [[planificacion-dinamica]] · [[tomasulo]]

Tabla comparativa entre Tomasulo y el algoritmo Marcador (Scoreboard) del CDC 6600:
- Unidades funcionales: Tomasulo usa unidades segmentadas (pipelined) con mayor cantidad (6 load, 3 store, 3 suma, 2 mult/div); Marcador usa unidades no segmentadas y menos (1 load/store, 1 suma, 2 mult, 1 div).
- Ventana de instrucciones: Tomasulo 14 entradas; Marcador 5.
- Riesgo estructural: ambos no lanzan instrucción si hay riesgo estructural.
- Riesgos WAR/WAW: Tomasulo los evita mediante renombrado de registros (estaciones de reserva); Marcador los detecta y espera (stall).
- Comunicación de resultados: Tomasulo usa CDB (broadcast a estaciones de reserva); Marcador escribe/lee directamente en el banco de registros.
- Control: Tomasulo descentralizado en cada estación de reserva; Marcador centralizado en el marcador (scoreboard).
- Flujo: ambos emiten en orden, ejecutan y finalizan fuera de orden.

> • Unidades funcionales segmentadas     • Múltiples unidades funcionales      6 loads, 3 stores, 3 +, 2 */        1 load/store, 1 +, 2 *, 1 / •    Ventana de instrucciones 14       • Ventana de instrucciones 5 •    No lanza con riesgo estructural   • No lanza con riesgo estructural •    WAR evita renombre                • WAR para •    WAW evita renombre                • WAW para •    Resultados a unidades funcionales • Escribe / lee registros •    Control estación de reserva       • Control central marcador
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[algoritmo-tomasulo-origen-y-objetivo-cpi1]] · [[diferencias-clave-entre-las-tres-tablas-de-planificacion-ped]] · [[scoreboard-escribe-resultados-a-traves-del-banco-de-registro]] · [[tecnica-de-marcador-scoreboard-riesgos-war-waw-obligan-a-det]]
