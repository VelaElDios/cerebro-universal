---
tipo: "concepto"
titulo: "Algoritmo Tomasulo: origen y objetivo CPI≈1"
temas: ["ac", "arquitectura", "planificacion-dinamica", "tomasulo"]
claves: ["IBM 360/91", "1967", "CPI", "instrucción por ciclo", "punto flotante"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[planificacion-dinamica]] · [[tomasulo]]

Tomasulo nace en el IBM 360/91 (1967) para acelerar operaciones en punto flotante. Su meta es sostener una emisión de una instrucción por ciclo (CPI≈1) ejecutando instrucciones independientes en paralelo, detectando y gestionando dependencias, y permitiendo que instrucciones independientes adelanten a las que esperan operandos.

> Su origen hay que buscarlo en el IBM 360/91 (1967), donde se introdujo para aumentar el rendimiento de las operaciones en punto flotante. Procesar las instrucciones en los operadores a la misma velocidad con la que las suministra la etapa ID (una instrucción por ciclo) → CPI ≈ 1
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)

Relacionado: [[objetivo-del-algoritmo-tomasulo-test-ac-q10]] · [[como-se-traza-la-ejecucion-ciclo-a-ciclo-en-el-algoritmo-de]] · [[planificacion-dinamica-sin-especulacion-orden-de-ejecucion-d]]
