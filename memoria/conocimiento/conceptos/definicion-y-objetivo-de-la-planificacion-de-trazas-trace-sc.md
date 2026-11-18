---
tipo: "concepto"
titulo: "Definición y objetivo de la planificación de trazas (trace scheduling)"
temas: ["ac", "ilp", "planificacion-estatica", "trazas"]
claves: ["trace scheduling", "bloques basicos", "prediccion saltos", "ilp"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Junio2017.pdf"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[ac]] · [[ilp]] · [[planificacion-estatica]] · [[trazas]]

La planificación de trazas (trace scheduling) es una técnica de planificación estática (compilador) que combina dos procesos: (1) selección de la secuencia más probable de bloques básicos (traza) usando perfilado o predicción estática, y (2) predicción de saltos para tratar las salidas de la traza. Permite mover instrucciones a través de saltos predichos para aumentar ILP, generando código de compensación (fix-up) para caminos no tomados. La opción correcta es la c.

> La técnica de selección de trazas: a) Ejecuta eficientemente cualquier código, aunque haya sido optimizado para otra unidad de instrucción segmentada b) Usa predicción dinámica de saltos para decidir qué bloques tienen mayor probabilidad de ejecutarse en la secuencia c) Combina los procesos de selección de la secuencia más probable de bloques básicos y predicción de saltos d) Ninguna es correcta
> — `repo:datos/temarios/AC/examenes/Junio2017.pdf`

Relacionado: [[alternativas-de-deteccion-de-instruccion-de-salto-en-pipelin]]
