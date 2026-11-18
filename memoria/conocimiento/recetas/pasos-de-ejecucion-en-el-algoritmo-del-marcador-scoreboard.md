---
tipo: "receta"
titulo: "Pasos de ejecución en el algoritmo del Marcador (Scoreboard)"
temas: ["ac", "algoritmos", "arquitectura-computadores", "scoreboard"]
claves: ["Emisión", "Lectura operandos", "Ejecución", "Escritura resultado", "riesgos WAW", "RAW", "WAR"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[algoritmos]] · [[arquitectura-computadores]] · [[scoreboard]]

1) Emisión: se emite si hay UF libre y no hay riesgo WAW (ninguna instrucción activa con mismo registro destino). Si hay riesgo estructural o WAW, se detiene la emisión y no se emiten más instrucciones. 2) Lectura operandos: cuando operandos fuente están disponibles (ninguna instrucción activa los va a escribir), el marcador indica a la UF que lea operandos y comience ejecución. Si no, la instrucción se detiene y otras pueden seguir (fuera de orden). Resuelve dinámicamente riesgos RAW. No hay adelantamiento, operandos se leen siempre de registros. 3) Ejecución: la UF comienza ejecución y notifica al marcador cuando resultado está listo. 4) Escritura resultado: si no hay riesgo WAR, el marcador indica a la UF que almacene resultado en registro destino. No se escribe si hay instrucción anterior que no ha leído operandos y uno está en el mismo registro que el resultado.

> Emisión (Issue): el marcador facilita la instrucción a la unidad funcional y actualiza su estructura interna de datos si: una unidad funcional está libre, ninguna otra instrucción activa tiene el mismo registro destino
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[planificacion-dinamica-de-instrucciones-con-marcador-scorebo]] · [[algoritmo-de-marcador-scoreboard-pasos-de-simulacion-para-ej]] · [[estructura-del-marcador-scoreboard-en-arquitectura-de-comput]]
