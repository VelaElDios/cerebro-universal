---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure en LaTeX"
temas: ["capturas", "latex", "manual-usuario", "subcaption", "subfigure", "figuras", "memoria"]
claves: ["subfigure", "0.48\\textwidth", "\\subcaption", "\\caption", "\\label", "fig:app-inicio-registro", "fig:juego-menu-vestuario"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex, chapters/04b-juego.tex", "chapters/04-descripcion.tex (sección 6) y chapters/04b-juego.tex (sección 2)", "memoria/proyectos/memoria-procesos/chapters/04-descripcion.tex"]
confianza: "propuesto"
fecha: "2026-11-25"
actualizado: "2026-11-25"
---

Temas: [[capturas]] · [[latex]] · [[manual-usuario]] · [[subcaption]] · [[subfigure]]

Para agrupar capturas relacionadas (p. ej., dos pantallas del mismo flujo): 1. Usar `\begin{figure}[htbp]` contenedor. 2. Dentro, dos `\begin{subfigure}{0.48\textwidth}` con `\centering`. 3. Cada subfigura lleva su `\includegraphics` (verticales móvil: `width=0.35\textwidth` o `height=0.35\textheight,keepaspectratio`; resto: `width=0.9\textwidth` máx. y `height=0.42\textheight,keepaspectratio`). 4. Cada subfigura tiene su `\subcaption{...}` y `\label{fig:sub...}`. 5. La figura contenedor tiene su `\caption{...}` general y `\label{fig:...}`. 6. En el texto, explicar la interacción usuario–app citando las subfiguras con `\ref{fig:sub...}` y la figura general con `\ref{fig:...}`. 7. No escribir frases sueltas «La figura X muestra…».

> \begin{figure}[htbp]\centering\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}\subcaption{Página de inicio sin sesión.}\label{fig:app-inicio}\end{subfigure}\hfill\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion.png}\subcaption{Validación en cliente: email y contraseña con errores.}\label{fig:app-registro}\end{subfigure}\caption{Inicio y registro: página pública y validación del formulario.}\label{fig:app-inicio-registro}\end{figure}
> — `chapters/04-descripcion.tex, chapters/04b-juego.tex` (cita sin comprobar)

Relacionado: [[prosa-de-tfg-sin-cadenas-la-figura-x-muestra-regla-13-javier]]

## Ampliación (2026-11-25, memoria-procesos)
Pasos para agrupar dos capturas relacionadas en una figura con `subfigure` (paquete `subcaption` ya cargado):
1. Usar `\begin{figure}[htbp]\centering`.
2. Primera subfigura: `\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta/imagen1}\subcaption{Texto descriptivo.}\label{fig:etiqueta1}\end{subfigure}`.
3. Separador horizontal: `\hfill`.
4. Segunda subfigura: `\begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta/imagen2}\subcaption{Texto descriptivo.}\label{fig:etiqueta2}\end{subfigure}`.
5. Caption general: `\caption{Texto que explica el conjunto.}\label{fig:etiqueta-general}`.
6. Cerrar `\end{figure}`.
7. En el texto, referirse a la figura general con `\ref{fig:etiqueta-general}` o a una subfigura con `\subref{fig:etiqueta1}` (requiere `subcaption`).
8. Para capturas verticales (móvil) usar `width=0.35\textwidth`; para el resto `width=0.9\textwidth` máx., siempre con `height=0.42\textheight,keepaspectratio`.

## Ampliación (2026-11-25, memoria-procesos)
Para evitar listas de capturas sueltas, agrupar capturas relacionadas en una figura con `subfigure` (paquete `subcaption`). Cada subfigura usa `width=\linewidth` (o `0.48\textwidth` para dos por fila), `height=0.35\textheight,keepaspectratio` para móviles o `0.42\textheight` para escritorio. La figura principal tiene `\caption` general y `\label{fig:...}`; cada subfigura tiene `\subcaption` y `\label{fig:...}`. En el texto se cita la figura general o las subfiguras individuales con `\ref`.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
