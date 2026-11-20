---
tipo: "receta"
titulo: "Limitar altura de capturas para evitar páginas con una sola imagen"
temas: ["figuras", "latex", "maquetacion", "adjustbox", "capturas"]
claves: ["adjustbox", "max totalheight", "0.42\\textheight", "regla 8"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-20"
---

Temas: [[figuras]] · [[latex]] · [[maquetacion]]

Para capturas altas (gráficas de DoneTonic, capturas de CI/CD), envolver en `adjustbox{max totalheight=0.42\textheight,width=...}` en lugar de solo `height=0.42\textheight,keepaspectratio`. Esto permite que la figura comparta página con texto. Para diagramas TikZ/pgfplots grandes, usar `\begin{adjustbox}{max width=\linewidth,max totalheight=0.6\textheight}...\end{adjustbox}`. Relajar parámetros de flotantes: `\renewcommand{\topfraction}{0.85}`, `\renewcommand{\textfraction}{0.12}`, `\setcounter{totalnumber}{4}`.

> - capturas como mucho a `height=0.42\textheight`; - diagramas grandes con `max totalheight`; - figuras `[htbp]` con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
> — `memoria/reglas-tfg.md`

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

## Ampliación (2026-11-19, memoria-procesos)
|
  Para capturas altas (p.ej. gráficas de DoneTonic, CI/CD):
  ```latex
  \begin{figure}[htbp]
  \centering
  \adjustbox{max totalheight=0.42\textheight,width=0.85\textwidth}{\includegraphics{...}}
  \caption{...}\label{...}
  \end{figure}
  ```
  Para capturas móviles (verticales): `width=0.35\textwidth` + `height=0.42\textheight,keepaspectratio`.
  Siempre usar `[htbp]` y parámetros de flotantes relajados (ya en include/extra.tex).

## Ampliación (2026-11-19, memoria-procesos)
Para capturas altas (gráficas DoneTonic, GitHub Actions) que ocupan casi una página entera, envolver en `adjustbox` con `max totalheight=0.42\textheight` y `width=0.85\textwidth` (o similar) para que compartan página con texto:
```latex
\begin{figure}[htbp]
\centering
\adjustbox{max totalheight=0.42\textheight,width=0.85\textwidth}{\includegraphics{figs/capturas/donetonic/06-graficas-sprint2.png}}
\caption{Gráficas del Sprint 2 en recta.}
\label{fig:donetonic-s2-graficas}
\end{figure}
```
Si aun así queda sola, reducir a `0.35\textheight` o agrupar con otra captura relacionada en `subfigure`. Los parámetros de flotantes en `include/extra.tex` ya están relajados (`\topfraction=0.85`, `\bottomfraction=0.6`, `\textfraction=0.12`, `\floatpagefraction=0.8`, `topnumber=3`, `totalnumber=4`).

Relacionado: [[corregir-paginas-con-una-sola-imagen-regla-8]] · [[figuras-que-comparten-pagina-con-el-texto-parametros-de-flot]] · [[figuras-ninguna-pagina-con-una-sola-imagen-limites-de-altura]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
