---
tipo: "receta"
titulo: "Cómo se agrupan capturas con subfigure"
temas: ["figura", "latex", "subcaption"]
claves: ["subfigure", "subcaption", "agrupación", "caption general"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[figura]] · [[latex]] · [[subcaption]]

Para agrupar capturas relacionadas y evitar la cadena «La figura X muestra…», se usa el entorno `subfigure` (paquete `subcaption`). Dos por fila con ancho `0.48\textwidth`. Cada subfigura tiene su `\subcaption` y `\label`. La figura general tiene su `\caption` y `\label`. En el texto se cita la figura general o la subfigura según necesidad. Esto cumple la regla 13 de Javier: prosa que explica qué hace el usuario y por qué la aplicación responde así, citando las figuras dentro de esa explicación.

> \begin{figure}[htbp]\centering\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}\subcaption{Página de inicio sin sesión.}\label{fig:app-inicio}\end{subfigure}\hfill\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}\subcaption{Validación en cliente: email y contraseña con errores.}\label{fig:app-registro}\end{subfigure}\caption{Inicio y registro: página pública y validación del formulario.}\label{fig:app-inicio-registro}\end{figure}
> — `chapters/04-descripcion.tex` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
