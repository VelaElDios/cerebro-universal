---
tipo: "receta"
titulo: "Limitar altura de capturas para evitar páginas con una sola imagen"
temas: ["figuras", "latex", "maquetacion", "adjustbox", "capturas"]
claves: ["adjustbox", "max totalheight", "0.42\\textheight", "regla 8"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[figuras]] · [[latex]] · [[maquetacion]]

Para capturas altas (gráficas de DoneTonic, capturas de CI/CD), envolver en `adjustbox{max totalheight=0.42\textheight,width=...}` en lugar de solo `height=0.42\textheight,keepaspectratio`. Esto permite que la figura comparta página con texto. Para diagramas TikZ/pgfplots grandes, usar `\begin{adjustbox}{max width=\linewidth,max totalheight=0.6\textheight}...\end{adjustbox}`. Relajar parámetros de flotantes: `\renewcommand{\topfraction}{0.85}`, `\renewcommand{\textfraction}{0.12}`, `\setcounter{totalnumber}{4}`.

> capturas como mucho a `height=0.42\textheight`; diagramas grandes con `max totalheight`; figuras `[htbp]` con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

## Ampliación (2026-11-19, memoria-procesos)
|
  **Regla 8**: Ninguna página del PDF debe tener una sola imagen ocupando toda la página.
  
  **Para capturas (archivos PNG):**
  - Verticales (móvil): `\includegraphics[width=0.35\textwidth,height=0.42\textheight,keepaspectratio]{...}`
  - Horizontales: `\includegraphics[width=0.9\textwidth,height=0.42\textheight,keepaspectratio]{...}`
  - En `subfigure`: `width=\linewidth,height=0.35\textheight,keepaspectratio`
  - Si aun así la figura (o grupo subfigure) queda muy alta y se queda sola en página: envolver en `\adjustbox{max totalheight=0.42\textheight,width=...}{\includegraphics{...}}`
  
  **Para diagramas TikZ/pgf-umlsd grandes:**
  - Envolver en `\begin{adjustbox}{max width=\linewidth, max totalheight=0.6\textheight} ... \end{adjustbox}`
  - Dentro, usar `\resizebox{\textwidth}{!}{...}` solo si es necesario
  - Si las letras quedan < 8pt tras escalar, rediseñar el diagrama (menos participantes, más espacio, dividir en dos)
  
  **Parámetros de flotantes relajados** (ya en include/extra.tex):
  ```latex
  \renewcommand{\topfraction}{0.85}
  \renewcommand{\bottomfraction}{0.6}
  \renewcommand{\textfraction}{0.12}
  \renewcommand{\floatpagefraction}{0.8}
  \setcounter{topnumber}{3}
  \setcounter{totalnumber}{4}
  ```
  
  **Capturas identificadas que necesitan adjustbox:**
  - `figs/capturas/donetonic/06-graficas-sprint2.png` (en a1-desarrollo.tex, Figura~\ref{fig:donetonic-s2-graficas})
  - `figs/capturas/produccion/02-actions-verde.png` (en 05-evaluacion.tex, Figura~\ref{fig:actions-verde})

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
