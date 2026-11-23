---
tipo: "dato"
titulo: "Gemini 404 en revisar_figuras no bloquea, pero la revisión a ojo del PDF sigue siendo obligatoria"
temas: ["latex", "reglas-javier", "revisar-figuras", "revision"]
claves: ["404 NOT_FOUND", "gemini-flash-lite-latest", "no pude revisar Figura", "no bloqueo"]
proyectos: ["memoria-procesos"]
fuentes: ["salida de revisar_maquetacion.py en este paso"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[reglas-javier]] · [[revisar-figuras]] · [[revision]]

Cuando el modelo de revisión visual devuelve 404, el script marca el diagrama como «no pude revisar» pero no falla la prueba. Aun así, las reglas 16–19 de Javier exigen que alguien mire el PDF: letras ≥ 7,5 pt, sin flechas que crucen cajas ni palabras partidas. Hay que revisar esos diagramas a ojo en el PDF antes de marcar TERMINADO.

> ⚠️ Figuras: no pude revisar Figura 3.1 (fig:capas): 404 NOT_FOUND … (no bloqueo).» y «✅ Figuras: 13 diagramas medidos en el PDF, sin fallos.
> — `salida de revisar_maquetacion.py en este paso` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
