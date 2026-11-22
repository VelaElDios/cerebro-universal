---
tipo: "receta"
titulo: "Cómo escribir prosa de TFG integrando capturas (sin «La figura X muestra…»)"
temas: ["latex", "redaccion", "tfg"]
claves: ["subfigure", "caption", "ref", "prosa"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-22"
actualizado: "2026-11-22"
---

Temas: [[latex]] · [[redaccion]] · [[tfg]]

Patrón correcto:
1. **Agrupar capturas relacionadas** en una `figure` con `subfigure` (dos por fila, `0.48\textwidth`).
2. **Caption general** en la `figure` y **subcaption** en cada `subfigure`.
3. **En el párrafo anterior o posterior**, explicar qué hace el usuario y qué muestra la captura, citando con `\ref{fig:etiqueta}` o `\subref{fig:subetiqueta}`.
4. **No** escribir frases sueltas como "La Figura 3.1 muestra el panel de administración".

Ejemplo:
```latex
El panel de administración muestra contadores totales, un buscador por email y una tabla con email, rol, estado, fecha de alta y acciones (Figura~\ref{fig:app-admin-full}). La subfigura~\subref{fig:app-admin} presenta la vista completa y la subfigura~\subref{fig:app-admin-busqueda} el resultado de filtrar por «gmail».

\begin{figure}[htbp]
\centering
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/07-panel-admin.png}
\subcaption{Panel de administración: tabla y buscador.}
\label{fig:app-admin}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
\centering
\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/08-admin-busqueda.png}
\subcaption{Búsqueda filtrada por email.}
\label{fig:app-admin-busqueda}
\end{subfigure}
\caption{Panel de administración: vista completa y búsqueda.}
\label{fig:app-admin-full}
\end{figure}
```

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con subfigure.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[imagenes-repetidas-una-sola-aparicion-y-ref-en-el-resto]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
