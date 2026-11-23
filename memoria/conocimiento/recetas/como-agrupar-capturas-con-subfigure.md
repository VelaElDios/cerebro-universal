---
tipo: "receta"
titulo: "Cómo agrupar capturas con subfigure"
temas: ["latex", "maquetacion", "subcaption"]
claves: ["subfigure", "subcaption", "cludegraphics", "width", "height", "keepaspectratio"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (regla 13) y spec del proyecto"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[maquetacion]] · [[subcaption]]

|
  Patrón correcto:
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
  - Dos por fila (`0.48\textwidth` + `\hfill`).
  - Caption general (`\caption`) y uno por subfigura (`\subcaption`).
  - Cada subfigura con su `\label` para citar con `\ref` o `\subref`.
  - En el texto: prosa que explica el flujo citando las figuras: «Al acceder sin sesión, el usuario ve la página de inicio (Figura~\ref{fig:app-inicio}) y, al registrarse, la validación en cliente muestra errores en línea (Figura~\ref{fig:app-registro}).»
  - Verticales (móvil): `width=0.35\textwidth`; el resto, `width=0.9\textwidth` máx., siempre `height=0.42\textheight,keepaspectratio`.

> **Prosa de TFG, no listas de capturas:** nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
> — `memoria/reglas-tfg.md (regla 13) y spec del proyecto` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
