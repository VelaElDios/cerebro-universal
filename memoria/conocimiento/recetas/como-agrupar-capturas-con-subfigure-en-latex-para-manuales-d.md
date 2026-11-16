---
tipo: "receta"
titulo: "Cómo agrupar capturas con subfigure en LaTeX para manuales de usuario"
temas: ["latex", "maquetacion", "subcaption"]
claves: ["subfigure", "height=0.42\\textheight", "caption general", "subcaption"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex (cambios aplicados en este paso)"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[maquetacion]] · [[subcaption]]

Para evitar páginas con una sola imagen (Regla 8) y cadenas de «La figura X muestra…» (Regla 12), agrupar capturas relacionadas en una figura con `subfigure` (paquete `subcaption`, ya cargado). Usar dos por fila con `\begin{subfigure}{0.48\textwidth}`, altura máxima `0.42\textheight` y `keepaspectratio`. Poner un `\caption` general en la figura y un `\subcaption` por subfigura. Escribir el texto como prosa explicativa que integre las referencias a las subfiguras (ej. «Al acceder a la aplicación sin sesión, el usuario encuentra la página de inicio (Figura~\ref{fig:app-inicio-registro}a)...»). Eliminar todas las figuras sueltas y sus frases introductorias.

> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.42\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png} \subcaption{Página de inicio sin sesión.} \label{fig:app-inicio} \end{subfigure}
> — `chapters/04-descripcion.tex (cambios aplicados en este paso)`

Relacionado: [[cada-imagen-aparece-una-sola-vez-en-el-capitulo-canonico]] · [[corregir-paginas-con-una-sola-imagen-regla-8]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
