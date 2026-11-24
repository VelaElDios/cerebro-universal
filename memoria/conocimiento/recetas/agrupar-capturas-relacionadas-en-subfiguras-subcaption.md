---
tipo: "receta"
titulo: "Agrupar capturas relacionadas en subfiguras (subcaption)"
temas: ["figuras", "latex", "maquetación", "subcaption"]
claves: ["subfigure", "subcaption", "0.48\\textwidth", "caption general"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex, chapters/04b-juego.tex"]
confianza: "propuesto"
fecha: "2026-11-24"
actualizado: "2026-11-24"
---

Temas: [[figuras]] · [[latex]] · [[maquetación]] · [[subcaption]]

Para evitar cadenas «La figura X muestra…»:
1. Agrupar capturas relacionadas (mismo flujo, misma pantalla) en UNA figura con `subfigure` (paquete `subcaption` ya cargado).
2. Usar `\begin{subfigure}{0.48\textwidth}` para dos por fila, `\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{ruta}`.
3. Cada subfigura con `\subcaption{...}` y `\label{fig:sub-...}`.
4. Figura general con `\caption{...}` y `\label{fig:general}`.
5. En el texto, explicar en prosa qué hace el usuario y citar subfiguras: «Al registrarse, el formulario valida email y contraseña en cliente (subfigura~\ref{fig:app-registro}) y el servidor responde 409 si el email existe (subfigura~\ref{fig:app-entrar})».
6. Móviles (verticales): `width=0.35\textwidth`; resto `width=0.9\textwidth` máx, siempre `height=0.42\textheight,keepaspectratio`.

> begin{subfigure}{0.48\textwidth} ... subcaption{...} ... end{subfigure} hfill ... caption{...} label{fig:...}
> — `chapters/04-descripcion.tex, chapters/04b-juego.tex` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
