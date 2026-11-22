---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas en subfigure (2 por fila)"
temas: ["figuras", "latex", "maquetacion", "subcaption"]
claves: ["subfigure", "0.48\\textwidth", "caption general", "subcaption"]
proyectos: ["memoria-procesos"]
fuentes: ["spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[figuras]] · [[latex]] · [[maquetacion]] · [[subcaption]]

**Plantilla obligatoria** para 2 capturas relacionadas (horizontal):
```latex
\begin{figure}[htbp]
\centering
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/carpeta/imagen1}
\subcaption{Descripción corta imagen 1.}
\label{fig:etiqueta1}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/carpeta/imagen2}
\subcaption{Descripción corta imagen 2.}
\label{fig:etiqueta2}
\end{subfigure}
\caption{Caption general que une las dos imágenes.}
\label{fig:etiqueta-general}
\end{figure}
```
**En la prosa**: referenciar la figura general (`Figura~\ref{fig:etiqueta-general}`) y/o subfiguras (`subfigura~\ref{fig:etiqueta1}`) dentro de la explicación.
**Parámetros de imagen**:
- Verticales (móvil): `width=0.35\textwidth` (en subfigure usar `\linewidth` que es 0.48\textwidth).
- Horizontales: `width=0.9\textwidth` máx, **siempre** `height=0.42\textheight,keepaspectratio` (regla 8: ninguna página con una sola imagen).
- En `subfigure`, el `width=\linewidth` respeta el 0.48\textwidth del contenedor.
**Ejemplos aplicados**: 04-descripcion.tex (fig:app-inicio-registro, fig:app-errores-acceso, fig:app-perfil-baja, fig:app-admin-full, fig:app-responsive, fig:app-estados-especiales, fig:hito4-flujo, fig:hito4-estados-privacidad) y 04b-juego.tex (fig:juego-menu-vestuario, fig:juego-partida-mejora, fig:juego-jefe-ambiente, fig:juego-fin-pausa, fig:juego-club-pantallas-a, fig:juego-club-pantallas-b).

> Las capturas relacionadas van juntas en una figura con subfigure (de subcaption, ya cargado; dos por fila, \begin{subfigure}{0.48\textwidth}), con un caption general y uno por subfigura.
> — `spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
