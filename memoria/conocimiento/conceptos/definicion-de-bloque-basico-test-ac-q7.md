---
tipo: "concepto"
titulo: "Definición de bloque básico (test AC Q7)"
temas: ["ac", "compiladores", "optimizacion"]
claves: ["bloque-basico", "basic-block", "salto", "control-flow"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2025.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[compiladores]] · [[optimizacion]]

Un **bloque básico** (basic block) es una secuencia de instrucciones consecutivas que tiene:
- Un único punto de entrada (la primera instrucción).
- Un único punto de salida (la última instrucción, que es un salto o la siguiente instrucción es un salto).
- No hay saltos hacia el interior del bloque.
Es la unidad fundamental para análisis de flujo de control y optimizaciones de compilador.

> ¿Cómo se le llama a la secuencia de instrucciones entre instrucciones de salto?
> — `repo:datos/temarios/AC/examenes/Enero2025.pdf`
