---
tipo: "concepto"
titulo: "Planificación estática vs dinámica de instrucciones en Arquitectura de Computadores"
temas: ["ac", "compilador", "hardware", "ilp", "planificacion-instrucciones"]
claves: ["planificación estática", "planificación dinámica", "ILP", "desenrollamiento bucles", "segmentación software", "planificación trazas", "saltos retardados", "Marcador", "Tomasulo"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[compilador]] · [[hardware]] · [[ilp]] · [[planificacion-instrucciones]]

La planificación de instrucciones busca aumentar el paralelismo a nivel de instrucción (ILP). Dos enfoques principales:
- **Planificación estática**: El compilador reordena/modifica el código (fuente → compilación → planificación → objeto). Ventajas: control hardware simple, software elimina riesgos, buen rendimiento en unidades segmentadas enteras. Desventaja: peor rendimiento en unidades de punto flotante. Técnicas: desenrollamiento de bucles, segmentación software, planificación de trazas, saltos retardados.
- **Planificación dinámica**: El hardware reordena en tiempo de ejecución. Técnicas: Marcador (Scoreboard) y algoritmo Tomasulo.

> El compilador reordena/modifica el código para aumentar el ILP, reduciendo las dependencias (y con ello sus posibles riesgos)
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf`

Relacionado: [[calculo-de-flops-por-ciclo-en-x86-con-avx2-fma]]
