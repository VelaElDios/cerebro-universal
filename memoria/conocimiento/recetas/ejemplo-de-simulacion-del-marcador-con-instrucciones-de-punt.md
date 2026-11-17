---
tipo: "receta"
titulo: "Ejemplo de simulación del Marcador con instrucciones de punto flotante"
temas: ["ac", "arquitectura-computadores", "ejemplo", "scoreboard", "simulacion"]
claves: ["fld", "fmul.d", "fsub.d", "fdiv.d", "fadd.d", "ciclos", "latencias"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura-computadores]] · [[ejemplo]] · [[scoreboard]] · [[simulacion]]

Ejemplo con instrucciones: fld f6,34(x2); fld f2,45(x3); fmul.d f0,f2,f4; fsub.d f8,f6,f2; fdiv.d f10,f0,f6; fadd.d f6,f8,f2. Latencias: fadd.d/fsub.d = 2 ciclos, fmul.d = 10 ciclos, fdiv.d = 40 ciclos. El ejemplo muestra la evolución ciclo a ciclo de las tres tablas del marcador. En ciclo 1 se emiten las dos cargas y fmul.d (Mult1 ocupada). En ciclo 2 la segunda carga se bloquea por riesgo estructural (solo 1 unidad entera). Las tablas muestran cómo Qj/Qk apuntan a las UF productoras y Rj/Rk indican disponibilidad de operandos.

> fadd.d y fsub.d 2 ciclos, fmul.d 10 ciclos, fdiv.d 40 ciclos
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[pasos-de-ejecucion-en-el-algoritmo-del-marcador-scoreboard]] · [[estructuras-de-datos-del-marcador-scoreboard]]
