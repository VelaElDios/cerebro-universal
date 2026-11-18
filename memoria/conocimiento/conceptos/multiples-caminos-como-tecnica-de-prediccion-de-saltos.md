---
tipo: "concepto"
titulo: "Múltiples caminos como técnica de predicción de saltos"
temas: ["ac", "arquitectura", "ejecucion-especulativa", "multiples-caminos", "prediccion-saltos"]
claves: ["múltiples caminos", "ejecutan varios caminos", "predicción saltos"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[arquitectura]] · [[ejecucion-especulativa]] · [[multiples-caminos]] · [[prediccion-saltos]]

Técnica donde el procesador ejecuta especulativamente varios caminos de un salto condicional simultáneamente (tanto el tomado como el no tomado), en lugar de predecir uno solo. Requiere recursos hardware duplicados (pipelines, unidades funcionales) y mecanismos para fusionar/descartar resultados según la resolución real del salto. Es una forma extrema de ejecución especulativa que elimina fallos de predicción a costa de mayor consumo de recursos y energía.

> Múltiples caminos: Se ejecutan varios caminos
> — `repo:datos/temarios/AC/Tema4-Tratamiento de los saltos/Tema4.pdf`

Relacionado: [[planteamiento-general-de-prediccion-de-saltos-con-ejecucion]] · [[definicion-de-ejecucion-multicamino-multipath-execution]] · [[ejecucion-multicamino-multi-path-execution-como-alternativa]] · [[ejecucion-multicamino-multi-path-execution-frente-a-predicci]]
