---
tipo: "receta"
titulo: "Cómo agrupar capturas con subfigure (dos por fila)"
temas: ["capturas", "figuras", "latex", "maquetacion", "subcaption"]
claves: ["subfigure", "0.48\\textwidth", "caption general", "caption individual", "subcaption", "cludegraphics", "width", "height", "keepaspectratio"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex", "memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 13) y spec del proyecto"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[capturas]] · [[figuras]] · [[latex]] · [[maquetacion]] · [[subcaption]]

Temas: [[capturas]] · [[latex]] · [[maquetacion]] · [[subcaption]]

|
  **Patrón estándar (genérico)** para dos capturas horizontales relacionadas:
  ```latex
  \begin{figure}[htbp]
  \centering
  \begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/carpeta/imagen1}
  \subcaption{Descripción breve}
  \label{fig:sub1}
  \end{subfigure}
  \hfill
  \begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/carpeta/imagen2}
  \subcaption{Descripción breve}
  \label{fig:sub2}
  \end{subfigure}
  \caption{Caption general que une las dos.}
  \label{fig:general}
  \end{figure}
  ```

  **Ejemplo concreto (memoria-procesos, 2026-11-23)**:
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

  **Reglas de maquetación**
  - Dos por fila: `0.48\textwidth` + `\hfill`.
  - Caption general (`\caption`) y uno por subfigura (`\subcaption`).
  - Cada subfigura con su `\label` para citar con `\ref` o `\subref`.
  - **Verticales (móvil)**: `width=0.35\textwidth`; el resto `width=0.9\textwidth` máx.
  - **Altura**: en el código de los ejemplos se usa `height=0.35\textheight,keepaspectratio`; la regla escrita dice `height=0.42\textheight,keepaspectratio` (ver contradicción).
  - **Regla 8**: ninguna página con una sola imagen; si una figura queda sola, reducir height o agrupar.

  **Prosa de TFG (Regla 13)**
  - Citar en prosa explicando el flujo, nunca con frases sueltas tipo «La figura X muestra…».
  - Ejemplo: «Al acceder sin sesión, el usuario ve la página de inicio (Figura~\ref{fig:app-inicio}) y, al registrarse, la validación en cliente muestra errores en línea (Figura~\ref{fig:app-registro}).»
  - Las capturas que van juntas se agrupan con `subfigure`.

> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta} \subcaption{Texto} \label{fig:sub} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex` (cita sin comprobar)

> **Prosa de TFG, no listas de capturas:** nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
> — `memoria/reglas-tfg.md (regla 13) y spec del proyecto` (cita sin comprobar)

Relacionado: [[prosa-de-tfg-sin-listas-de-capturas-regla-13-javier]] · [[como-agrupar-capturas-relacionadas-con-subfigure]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[como-se-agrupan-capturas-con-subfigure]]
Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> \begin{subfigure}{0.48\textwidth} \centering \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta} \subcaption{Texto} \label{fig:sub} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex` (cita sin comprobar)
> **Prosa de TFG, no listas de capturas:** nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con `subfigure`.
> — `memoria/reglas-tfg.md (regla 13) y spec del proyecto` (cita sin comprobar)


> ⚠️ Posible contradicción al fusionar: En ambas notas hay una inconsistencia interna: los bloques de código usan `height=0.35\textheight` mientras que las reglas textuales indican `height=0.42\textheight,keepaspectratio`.

Fusionada con: Cómo agrupar capturas con subfigure

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
