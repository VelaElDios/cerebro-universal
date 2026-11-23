---
tipo: "receta"
titulo: "Burndown real con pgfplots (fig:burndown-s1 y fig:burndown-s2)"
temas: ["burndown", "latex", "pgfplots", "anexo desarrollo"]
claves: ["pgfplots", "axis", "coordinates", "addplot", "legend"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/a1-desarrollo.tex", "repo:saas/docs/sprint-1.md, repo:saas/docs/sprint-2.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[burndown]] · [[latex]] · [[pgfplots]]

|
  Requisitos para que pase revisión visual (reglas 16-18):
  1. Fuentes ≥8pt en ejes, leyendas y marcas (`tick label style={font=\footnotesize}`, `label style={font=\small}`, `legend style={font=\footnotesize}`).
  2. `width=0.9\textwidth` (no más), `height=7cm`.
  3. `xticklabels` con fechas cortas (ej. `23/10`, `24/10`).
  4. `ymin=0`, `ymax` con margen (ej. 16 para S1, 30 para S2).
  5. Sin `adjustbox` que escale; el gráfico debe caber a tamaño real.
  6. Etiquetas de ejes claras: `xlabel={Momento del sprint}`, `ylabel={PBIs pendientes}`.
  7. Leyenda legible: `legend pos=north east`, `legend style={font=\footnotesize}`.
  8. Si el gráfico no cabe, reducir `width` a `0.8\textwidth` o usar `pdflscape` (último recurso).

  Ejemplo Sprint 1 (corregido):
  ```latex
  \begin{figure}[htbp]
  \centering
  \begin{tikzpicture}
  \begin{axis}[
      width=0.9\textwidth, height=7cm,
      xlabel={Momento del sprint}, ylabel={PBIs pendientes},
      xtick={1,2,3,4,5,6},
      xticklabels={Inicio, Hito 1, Hito 2, Hito 3, +P19, Cierre},
      ymin=0, ymax=16, grid=major,
      legend pos=north east, mark=*, thick,
      tick label style={font=\footnotesize},
      label style={font=\small},
      legend style={font=\footnotesize}
  ]
  \addplot coordinates {(1,15) (2,9) (3,5) (4,1) (5,2) (6,0)};
  \addlegendentry{PBIs pendientes}
  \end{axis}
  \end{tikzpicture}
  \caption{Burndown del Sprint 1...}
  \label{fig:burndown-s1}
  \end{figure}
  ```

> \begin{tikzpicture} \begin{axis}[width=0.9\textwidth, height=7cm, xlabel={...}, ylabel={...}, xtick={...}, xticklabels={...}, ymin=0, ymax=..., grid=major, legend pos=north east, mark=*, thick, tick label style={font=\footnotesize}, label style={font=\small}] \addplot coordinates {...}; \addlegendentry{...} \end{axis} \end{tikzpicture}
> — `memoria/chapters/a1-desarrollo.tex` (cita sin comprobar)

## Ampliación (2026-11-23, memoria-procesos)
Sprint 1 (fig:burndown-s1): datos de la Tabla Evolución del Sprint 1 (6 puntos: Inicio, Hito 1, Hito 2, Hito 3, +P19, Cierre). Eje Y: PBIs pendientes (0-16). Eje X: momentos. Usar `mark=*`, `thick`, `grid=major`, fuentes `\footnotesize` en ticks y labels.
Sprint 2 (fig:burndown-s2): datos de la Tabla Evolución real del Sprint 2 (7 puntos: 23/10 a 29/10). Eje Y: 0-30. Mismo estilo.
Evitar overfull: ancho `0.9\textwidth`, alto `7cm`. Si las etiquetas del eje X son largas, usar `xticklabels={23/10, 24/10,...}` y `tick label style={font=\footnotesize}`.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
