---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure"
temas: ["latex", "memoria-procesos", "subcaption", "figuras"]
claves: ["subfigure", "subcaption", "agrupación", "capturas"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex", "chapters/04-descripcion.tex (ejemplo real compilado)"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[memoria-procesos]] · [[subcaption]]

Para evitar cadenas de «La figura X muestra…», agrupar capturas relacionadas en una figura con `subfigure` (de `subcaption`, ya cargado; dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura. Cada subfigura debe tener su `\label` y ser citada con `\ref` en la prosa que explica el flujo de usuario.

> \begin{subfigure}{0.48\textwidth} ... \subcaption{...} \label{fig:...} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex` (cita sin comprobar)

## Ampliación (2026-11-23, memoria-procesos)
Para agrupar 2 capturas relacionadas: (1) entorno figure con [htbp]; (2) dos subfigure de 0.48\textwidth separados por \hfill; (3) cada subfigure con su \includegraphics (width=\linewidth, height=0.35\textheight, keepaspectratio) y su \subcaption + \label; (4) un \caption general al final del figure y un \label general. Para capturas verticales (móvil) usar height=0.15\textheight. Siempre citar ambas subfiguras en el texto con \ref{fig:sub-etiqueta}.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
