---
tipo: "receta"
titulo: "Cómo se agrupan capturas con subfigure"
temas: ["figura", "latex", "subcaption", "subfigure", "figuras"]
claves: ["subfigure", "subcaption", "agrupación", "caption general"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex", "memoria/chapters/04-descripcion.tex"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-23"
---

Temas: [[figura]] · [[latex]] · [[subcaption]]

Para agrupar capturas relacionadas y evitar la cadena «La figura X muestra…», se usa el entorno `subfigure` (paquete `subcaption`). Dos por fila con ancho `0.48\textwidth`. Cada subfigura tiene su `\subcaption` y `\label`. La figura general tiene su `\caption` y `\label`. En el texto se cita la figura general o la subfigura según necesidad. Esto cumple la regla 13 de Javier: prosa que explica qué hace el usuario y por qué la aplicación responde así, citando las figuras dentro de esa explicación.

> \begin{figure}[htbp]\centering\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}\subcaption{Página de inicio sin sesión.}\label{fig:app-inicio}\end{subfigure}\hfill\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}\subcaption{Validación en cliente: email y contraseña con errores.}\label{fig:app-registro}\end{subfigure}\caption{Inicio y registro: página pública y validación del formulario.}\label{fig:app-inicio-registro}\end{figure}
> — `chapters/04-descripcion.tex` (cita sin comprobar)

Relacionado: [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[agrupar-capturas-con-subfigure]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[reescribir-frases-la-figura-x-muestra-como-prosa-integrada]] · [[agrupar-capturas-relacionadas-en-subfiguras-con-prosa-integr]] · [[como-agrupar-capturas-relacionadas-con-subfigure]] · [[como-agrupar-capturas-con-subfigure-dos-por-fila]]

## Ampliación (2026-11-20, memoria-procesos)
Para evitar cadenas de «La figura X muestra…», agrupar capturas relacionadas en una figura con `subfigure` (de `subcaption`, ya cargado; dos por fila, `\begin{subfigure}{0.48\textwidth}`), con un caption general y uno por subfigura. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así.

## Ampliación (2026-11-23, memoria-procesos)
Para agrupar capturas relacionadas en una figura con caption general y subcaptions:
1. Usar entorno `figure` con `[htbp]`.
2. Dentro, dos `subfigure` con `{0.48\textwidth}` separados por `\hfill` (o `\\` para filas).
3. Cada `subfigure` lleva su `\includegraphics` con `width=\linewidth,height=0.35\textheight,keepaspectratio` (móvil) o `width=0.9\textwidth,height=0.42\textheight,keepaspectratio` (escritorio).
4. `\subcaption{...}` y `\label{fig:...}` por subfigura.
5. `\caption{...}` y `\label{fig:...}` general al final del entorno `figure`.
6. Citar en texto con `\ref{fig:general}` o `\ref{fig:sub}`.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
