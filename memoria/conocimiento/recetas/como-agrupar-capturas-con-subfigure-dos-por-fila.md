---
tipo: "receta"
titulo: "Cómo agrupar capturas con subfigure (dos por fila)"
temas: ["capturas", "latex", "subcaption"]
claves: ["subfigure", "0.48\\textwidth", "caption general", "caption individual"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[capturas]] · [[latex]] · [[subcaption]]

|
  Patrón estándar para dos capturas horizontales relacionadas:
  ```latex
  \begin{figure}[htbp]
  \centering
  \begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/carpeta/imagen1}
  \subcaption{Descripción breve}
  \label{fig:sub1}
  \end{subfigure}
  \hfill
  \begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/carpeta/imagen2}
  \subcaption{Descripción breve}
  \label{fig:sub2}
  \end{subfigure}
  \caption{Caption general que une las dos.}
  \label{fig:general}
  \end{figure}
  ```
  - Verticales (móvil): `width=0.35\textwidth`; horizontales: `width=0.9\textwidth` máx.
  - Siempre `height=0.42\textheight,keepaspectratio` (regla 8: ninguna página con una sola imagen).
  - Citar en prosa con `\ref{fig:sub1}` y `\ref{fig:sub2}`, nunca «La figura X muestra…».

> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta} \subcaption{Texto} \label{fig:sub} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex` (cita sin comprobar)

Relacionado: [[prosa-de-tfg-sin-listas-de-capturas-regla-13-javier]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
