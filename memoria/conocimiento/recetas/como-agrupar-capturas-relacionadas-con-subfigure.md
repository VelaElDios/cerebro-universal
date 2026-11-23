---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure"
temas: ["latex", "memoria-procesos", "subcaption", "figuras"]
claves: ["subfigure", "subcaption", "agrupación", "capturas"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex", "chapters/04-descripcion.tex (ejemplo real compilado)", "memoria/chapters/04-descripcion.tex (fig:app-inicio-registro, fig:app-errores-acceso, fig:app-perfil-baja, fig:app-admin-full, fig:app-responsive, fig:app-estados-especiales, fig:hito4-flujo, fig:hito4-estados-privacidad)"]
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

## Ampliación (2026-11-23, memoria-procesos)
Para agrupar capturas relacionadas (móvil: width=0.35\textwidth; resto: width=0.9\textwidth máx., siempre height=0.42\textheight,keepaspectratio): usar entorno figure con dos subfigure de 0.48\textwidth cada una, separadas por \hfill; caption general en la figure y subcaption en cada subfigure; cada subfigure con su \label para citar con \ref. Las capturas verticales (móvil) usan height=0.35\textheight; el resto height=0.42\textheight. Nunca una página con una sola imagen (regla 8).

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
