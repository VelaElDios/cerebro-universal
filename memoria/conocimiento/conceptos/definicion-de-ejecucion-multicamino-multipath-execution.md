---
tipo: "concepto"
titulo: "Definición de ejecución multicamino (multipath execution)"
temas: ["ac", "especulación", "prediccion-saltos"]
claves: ["multipath execution", "ambos caminos", "sin predicción"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2022.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[especulación]] · [[prediccion-saltos]]

La ejecución multicamino ejecuta simultáneamente ambos caminos de un salto condicional sin predecir cuál se tomará. Los resultados del camino incorrecto se descartan cuando se resuelve la condición. No usa predicción, sino recursos redundantes.

> Both paths of a conditional branch are executed, without using prediction
> — `repo:datos/temarios/AC/examenes/January2022.pdf`

Relacionado: [[ejecucion-multicamino-multi-path-execution-como-alternativa]] · [[ejecucion-multicamino-multi-path-execution-frente-a-predicci]] · [[multiples-caminos-como-tecnica-de-prediccion-de-saltos]]
