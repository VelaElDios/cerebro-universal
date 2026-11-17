---
tipo: "concepto"
titulo: "Impacto de la frecuencia de saltos en el ILP y tamaño de bloque básico"
temas: ["ac", "bloque básico", "ilp", "rendimiento"]
claves: ["Reducen el ILP", "tamaño bloque básico", "detenciones en el cauce"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bloque básico]] · [[ilp]] · [[rendimiento]]

Los saltos limitan el paralelismo a nivel de instrucción (ILP) porque definen los **bloques básicos** (secuencias de instrucciones sin saltos internos). Cuanto más frecuentes son los saltos, más cortos son los bloques básicos y menos instrucciones pueden emitirse/ejecutarse en paralelo. Además, cada salto no resuelto a tiempo provoca **detenciones (stalls)** en el pipeline, reduciendo el throughput real frente al ideal (CPI=1). El ejemplo del texto cuantifica esto: con 1 salto tomado cada 6 instrucciones y 2 ciclos de retardo, el CPI real pasa a 1,33 (rendimiento 0,75 inst/ciclo, -25%).

> Los saltos representan una fracción significativa de las instrucciones a ejecutar en un programa. Reducen el ILP  tamaño bloque básico. Pueden provocar detenciones en el cauce
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf` (cita sin comprobar)

Relacionado: [[estadisticas-de-frecuencia-y-tipos-de-saltos-en-programas-ti]] · [[calculo-de-penalizacion-de-salto-condicional-en-pipeline-de]]
