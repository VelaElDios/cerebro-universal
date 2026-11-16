---
tipo: "receta"
titulo: "Cómo agrupar capturas con subfigure en LaTeX"
temas: ["latex", "maquetacion", "subcaption"]
claves: ["subfigure", "subcaption", "agrupación capturas"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[maquetacion]] · [[subcaption]]

Para agrupar capturas relacionadas en una sola figura con subfiguras:
1. Usar el entorno `figure` con `[htbp]`.
2. Dentro, usar `\begin{subfigure}{0.48\textwidth}` para cada captura (dos por fila).
3. Cada subfigura lleva su `\includegraphics` y su `\caption{...}`.
4. La figura principal lleva un `\caption{...}` general y un `\label{fig:...}`.
5. En el texto, referenciar la figura general con `\ref{fig:...}` y, si hace falta, una subfigura concreta con `\subref{fig:sub...}` (requiere `subcaption` con opción `subrefformat=parens`).
Ejemplo:
```latex
\begin{figure}[htbp]
\centering
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth]{figs/capturas/app/01-inicio}
\caption{Página de inicio sin sesión.}
\label{fig:app-inicio}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth]{figs/capturas/app/02-registro-validacion}
\caption{Registro con validación de campos.}
\label{fig:app-registro}
\end{subfigure}
\caption{Pantallas de acceso: inicio y registro.}
\label{fig:app-acceso}
\end{figure}
```

> Las capturas relacionadas van juntas en una figura con `subfigure` (de `subcaption`, ya cargado; dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
