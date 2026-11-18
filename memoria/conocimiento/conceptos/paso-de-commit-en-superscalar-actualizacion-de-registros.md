---
tipo: "concepto"
titulo: "Paso de commit en superscalar: actualización de registros"
temas: ["ac", "commit", "pipeline", "superscalar"]
claves: ["commit", "superscalar", "actualizacion registros", "paso commit"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/January2019.pdf"]
confianza: "propuesto"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[commit]] · [[pipeline]] · [[superscalar]]

En el paso de commit (también llamado writeback o retirement en algunos diseños) la instrucción, ya completada y sin excepciones pendientes, escribe su resultado en el archivo de registros arquitectónico (o en memoria para stores), liberando recursos y haciendo el efecto permanente. No ocurre renombrado (eso es en dispatch/issue), ni pre-decode, ni predicción de saltos.

> Which of the following actions takes place at the commit step in a superscalar processor? c) Register updating
> — `repo:datos/temarios/AC/examenes/January2019.pdf` (cita sin comprobar)
