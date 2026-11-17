---
tipo: "concepto"
titulo: "Definición y propósito de la segmentación (pipeline)"
temas: ["ac", "pipeline", "segmentacion"]
claves: ["solapar ejecución", "etapas", "latencia vs productividad", "etapa más lenta", "ciclo máquina"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[pipeline]] · [[segmentacion]]

La segmentación (pipeline) solapa la ejecución de múltiples instrucciones dividiendo el cauce en etapas que usan recursos distintos. No reduce la latencia de una instrucción individual, pero aumenta el throughput (productividad). La frecuencia de reloj viene determinada por la etapa más lenta. Es transparente para el programador.

> La segmentación consiste en solapar la ejecución de instrucciones de forma que utilicen recursos distintos • El cauce de ejecución está dividido en varias etapas o segmentos • No se disminuye la latencia de una tarea, sino que se aumenta la productividad • La segmentación está limitada por la etapa más lenta que determina el ciclo máquina • La segmentación no es visible al programador
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf` (cita sin comprobar)
