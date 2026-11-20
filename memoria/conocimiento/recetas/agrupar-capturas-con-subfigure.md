---
tipo: "receta"
titulo: "Agrupar capturas con subfigure"
temas: ["figuras", "latex", "tfg", "memoria"]
claves: ["subfigure", "subcaption", "subfig"]
proyectos: ["memoria-procesos"]
fuentes: ["proyectos/memoria-procesos/spec.md", "../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[figuras]] · [[latex]] · [[tfg]]

Una frase «La figura X muestra…» por cada captura queda poco profesional. Las capturas de un mismo flujo van juntas y se explican en un párrafo que las cita. `subcaption` ya viene cargado en la plantilla:

```latex
\begin{figure}[htbp]
\centering
\begin{subfigure}{0.48\textwidth}
  \includegraphics[width=\linewidth,height=0.32\textheight,keepaspectratio]{figs/capturas/app/02-registro-validacion}
  \caption{Errores de validación en el registro.}
  \label{fig:registro-validacion}
\end{subfigure}\hfill
\begin{subfigure}{0.48\textwidth}
  \includegraphics[width=\linewidth,height=0.32\textheight,keepaspectratio]{figs/capturas/app/03-entrar-error}
  \caption{Credenciales incorrectas al entrar.}
  \label{fig:entrar-error}
\end{subfigure}
\caption{Errores de validación en el registro y en el inicio de sesión.}
\label{fig:errores-cuenta}
\end{figure}
```

> Las capturas relacionadas van juntas en una figura con subfigure
> — `proyectos/memoria-procesos/spec.md`

Relacionado: [[figuras-que-comparten-pagina-con-el-texto-parametros-de-flot]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]] · [[como-se-agrupan-capturas-con-subfigure]] · [[arreglar-pagina-con-una-sola-imagen-regla-8-agrupando-en-sub]] · [[agrupar-capturas-relacionadas-en-subfiguras-con-prosa-integr]]

## Ampliación (2026-11-16, )
Cuando varias capturas o diagramas están relacionados y se explican en el mismo párrafo, se agrupan en un único entorno `figure` usando `subfigure` (paquete `subcaption`). Cada subfigura lleva su propio `\subcaption` y etiqueta (`\label{fig:subX}`), y el conjunto tiene un `\caption` general y `\label{fig:principal}`. Esto evita páginas con una sola imagen y mejora la narrativa.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
