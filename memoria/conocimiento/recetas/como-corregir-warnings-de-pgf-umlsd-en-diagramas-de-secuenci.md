---
tipo: "receta"
titulo: "Cómo corregir warnings de pgf-umlsd en diagramas de secuencia"
temas: ["latex", "pgf-umlsd", "tikz"]
claves: ["\\mess", "\\call", "node center warning", "sdblock"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[pgf-umlsd]] · [[tikz]]

Los warnings "Returning node center instead of a point on node border" en pgf-umlsd indican que el comando \mess no encuentra los nodos origen/destino. Causas típicas: (1) El texto del mensaje contiene caracteres prohibidos (#, &, _, $, %, {, }, \, paréntesis, comandos LaTeX). (2) Se usa \mess para una llamada que debería ser \call (con respuesta vacía). (3) Los participantes no están declarados con \newthread/\newinst. Solución: Reemplazar \mess por \call{origen}{mensaje}{destino}{} para mensajes simples, asegurar que el mensaje es texto plano sin caracteres especiales, y declarar todos los participantes. Usar sdblock para alternativas.

> Package pgf Warning: Returning node center instead of a point on node border. Did you specify a point identical to the center of node ``mess from''?
> — `chapters/04-descripcion.tex` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
