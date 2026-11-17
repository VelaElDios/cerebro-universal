---
tipo: "concepto"
titulo: "Relación ILP y CPI en procesadores segmentados"
temas: ["ac", "cpi", "ilp", "paralelismo-instruccion"]
claves: ["Instruction Level Parallelism", "Cycles per instruction", "bloque básico"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[cpi]] · [[ilp]] · [[paralelismo-instruccion]]

Definición formal y relación causal: mayor ILP implica menos dependencias, menos riesgos, menos detenciones y, por tanto, CPI menor. La explotación del ILP requiere identificar qué instrucciones pueden ejecutarse en paralelo (independencia). El CPIideal se alcanza cuando no hay detenciones; el ILP real determina cuánto se acerca el CPI real al ideal.

> Paralelismo a nivel de instrucción o ILP:   Posibilidad de solapamiento en las secuencias de instrucciones   Depende del grado de dependencia entre las instrucciones  ILP ↑ → pocos conflictos → pocas detenciones → CPI ↓  Dos instrucciones son independientes si se pueden ejecutar simultáneamente sin que existan conflictos entre ellas
> — `repo:datos/temarios/AC/Tema2-Paralelismo a nivel de instruccion/Tema2-2026-2027.pdf`

Relacionado: [[tecnicas-avanzadas-estaticas-y-dinamicas-para-reducir-detenc]]
