---
tipo: "receta"
titulo: "Cómo agrupar capturas con subfigure (dos por fila)"
temas: ["capturas", "latex", "subcaption", "figuras"]
claves: ["subfigure", "0.48\\textwidth", "caption general", "caption individual"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex", "memoria/reglas-tfg.md"]
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

## Ampliación (2026-11-23, memoria-procesos)
```latex
\begin{figure}[htbp]
\centering
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}
\subcaption{Página de inicio sin sesión.}
\label{fig:app-inicio}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}
\subcaption{Validación en cliente: email y contraseña con errores.}
\label{fig:app-registro}
\end{subfigure}
\caption{Inicio y registro: página pública y validación del formulario.}
\label{fig:app-inicio-registro}
\end{figure}
```
- Verticales (móvil): `width=0.35\textwidth`; el resto `width=0.9\textwidth` máx., siempre `height=0.42\textheight,keepaspectratio`.
- Regla 8: ninguna página con una sola imagen; si una figura queda sola, reducir height o agrupar.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
