---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure en LaTeX"
temas: ["figuras", "latex", "subcaption"]
claves: ["subfigure", "subcaption", "agrupación", "capturas"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[figuras]] · [[latex]] · [[subcaption]]

Para agrupar capturas relacionadas en una figura con caption general y subcaptions individuales: usar el entorno `subfigure` del paquete `subcaption` (ya cargado). Cada subfigure ocupa 0.48\textwidth para dos por fila. Usar `\hfill` entre subfigures para separarlas. El caption general va fuera con `\caption{...}\label{fig:...}`. Las subcaptions con `\subcaption{...}\label{fig:...}`. Para capturas verticales (móvil): `width=\linewidth,height=0.35\textheight,keepaspectratio`; horizontales: `width=\linewidth,height=0.30\textheight,keepaspectratio`.

> \begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}\subcaption{Página de inicio sin sesión.}\label{fig:app-inicio}\end{subfigure}
> — `chapters/04-descripcion.tex` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
