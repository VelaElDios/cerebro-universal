---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure en LaTeX"
temas: ["capturas", "latex", "manual-usuario", "subcaption", "subfigure"]
claves: ["subfigure", "0.48\\textwidth", "\\subcaption", "\\caption", "\\label", "fig:app-inicio-registro", "fig:juego-menu-vestuario"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex, chapters/04b-juego.tex"]
confianza: "propuesto"
fecha: "2026-11-25"
actualizado: "2026-11-25"
---

Temas: [[capturas]] · [[latex]] · [[manual-usuario]] · [[subcaption]] · [[subfigure]]

Para agrupar capturas relacionadas (p. ej., dos pantallas del mismo flujo): 1. Usar `\begin{figure}[htbp]` contenedor. 2. Dentro, dos `\begin{subfigure}{0.48\textwidth}` con `\centering`. 3. Cada subfigura lleva su `\includegraphics` (verticales móvil: `width=0.35\textwidth` o `height=0.35\textheight,keepaspectratio`; resto: `width=0.9\textwidth` máx. y `height=0.42\textheight,keepaspectratio`). 4. Cada subfigura tiene su `\subcaption{...}` y `\label{fig:sub...}`. 5. La figura contenedor tiene su `\caption{...}` general y `\label{fig:...}`. 6. En el texto, explicar la interacción usuario–app citando las subfiguras con `\ref{fig:sub...}` y la figura general con `\ref{fig:...}`. 7. No escribir frases sueltas «La figura X muestra…».

> \begin{figure}[htbp]\centering\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}\subcaption{Página de inicio sin sesión.}\label{fig:app-inicio}\end{subfigure}\hfill\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}\subcaption{Validación en cliente: email y contraseña con errores.}\label{fig:app-registro}\end{subfigure}\caption{Inicio y registro: página pública y validación del formulario.}\label{fig:app-inicio-registro}\end{figure}
> — `chapters/04-descripcion.tex, chapters/04b-juego.tex` (cita sin comprobar)

Relacionado: [[prosa-de-tfg-sin-cadenas-la-figura-x-muestra-regla-13-javier]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
