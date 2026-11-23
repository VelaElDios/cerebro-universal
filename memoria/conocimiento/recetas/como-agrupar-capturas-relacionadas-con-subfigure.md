---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure"
temas: ["latex", "memoria-procesos", "subcaption"]
claves: ["subfigure", "subcaption", "agrupación", "capturas"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[memoria-procesos]] · [[subcaption]]

Para evitar cadenas de «La figura X muestra…», agrupar capturas relacionadas en una figura con `subfigure` (de `subcaption`, ya cargado; dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura. Cada subfigura debe tener su `\label` y ser citada con `\ref` en la prosa que explica el flujo de usuario.

> \begin{subfigure}{0.48\textwidth} ... \subcaption{...} \label{fig:...} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
