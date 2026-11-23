---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure (2 por fila)"
temas: ["figuras", "latex", "maquetacion", "memoria-procesos", "subcaption"]
claves: ["subfigure", "subcaption", "agrupación", "capturas", "0.48\\textwidth", "caption general"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/chapters/04-descripcion.tex", "chapters/04-descripcion.tex (ejemplo real compilado)", "memoria/chapters/04-descripcion.tex (fig:app-inicio-registro, fig:app-errores-acceso, fig:app-perfil-baja, fig:app-admin-full, fig:app-responsive, fig:app-estados-especiales, fig:hito4-flujo, fig:hito4-estados-privacidad)", "spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[figuras]] · [[latex]] · [[maquetacion]] · [[memoria-procesos]] · [[subcaption]]

Temas: [[latex]] · [[memoria-procesos]] · [[subcaption]] · [[figuras]] · [[maquetacion]]

**Propósito**  
Evitar cadenas de «La figura X muestra…» agrupando capturas relacionadas en una sola figura con `subfigure` (paquete `subcaption`, ya cargado), dos por fila, con un `\caption` general y un `\subcaption` por subfigura. Cada subfigura lleva su `\label` y se cita con `\ref` en la prosa que explica el flujo de usuario.

---

### Plantilla obligatoria (2 capturas relacionadas, disposición horizontal)
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

**En la prosa**  
Referenciar la figura general (`Figura~\ref{fig:etiqueta-general}`) y/o las subfiguras (`subfigura~\ref{fig:etiqueta1}`) dentro de la explicación del flujo.

---

### Parámetros de imagen (resumen consolidado)

| Contexto | `width` en `\includegraphics` | `height` en `\includegraphics` | Notas |
|---|---|---|---|
| **Verticales (móvil)** | `0.35\textwidth` | **Ver contradicciones** | En `subfigure` usar `width=\linewidth` (respeta el `0.48\textwidth` del contenedor). |
| **Horizontales (resto)** | `0.9\textwidth` máx. | `0.42\textheight` | **Siempre** `keepaspectratio`. Regla 8: ninguna página con una sola imagen. |

> **Detalle de las fuentes**  
> - *Nota A (1ª ampliación)*: móvil `height=0.15\textheight`.  
> - *Nota A (2ª ampliación)*: «siempre `height=0.42\textheight,keepaspectratio`» en el resumen inicial, pero luego especifica: «capturas verticales (móvil) usan `height=0.35\textheight`; el resto `height=0.42\textheight`».  
> - *Nota B*: para horizontales «siempre `height=0.42\textheight,keepaspectratio`»; para verticales (móvil) solo fija `width=0.35\textwidth` y remarca que en `subfigure` el `width=\linewidth` equivale a `0.48\textwidth`.

---

### Ejemplos aplicados (memoria-procesos)
**04-descripcion.tex**:  
`fig:app-inicio-registro`, `fig:app-errores-acceso`, `fig:app-perfil-baja`, `fig:app-admin-full`, `fig:app-responsive`, `fig:app-estados-especiales`, `fig:hito4-flujo`, `fig:hito4-estados-privacidad`

**04b-juego.tex**:  
`fig:juego-menu-vestuario`, `fig:juego-partida-mejora`, `fig:juego-jefe-ambiente`, `fig:juego-fin-pausa`, `fig:juego-club-pantallas-a`, `fig:juego-club-pantallas-b`

---

### Referencias de origen
- `memoria/chapters/04-descripcion.tex` (cita sin comprobar) — *Nota A*  
- `spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos` (cita sin comprobar) — *Nota B*  
- Origen común: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> \begin{subfigure}{0.48\textwidth} ... \subcaption{...} \label{fig:...} \end{subfigure}
> — `memoria/chapters/04-descripcion.tex` (cita sin comprobar)
> Las capturas relacionadas van juntas en una figura con subfigure (de subcaption, ya cargado; dos por fila, \begin{subfigure}{0.48\textwidth}), con un caption general y uno por subfigura.
> — `spec versión 4 y 04-descripcion.tex / 04b-juego.tex corregidos` (cita sin comprobar)


> ⚠️ Posible contradicción al fusionar: Altura (`height`) para capturas verticales (móvil): Nota A (1ª ampliación) dice 0.15\textheight; Nota A (2ª ampliación) dice 0.35\textheight en el detalle pero «siempre 0.42\textheight» en el resumen; Nota B no fija height explícito para móvil, solo width=0.35\textwidth, y exige «siempre height=0.42\textheight» para horizontales.

Fusionada con: Cómo agrupar capturas relacionadas en subfigure (2 por fila)

Relacionado: [[como-agrupar-capturas-con-subfigure-dos-por-fila]] · [[como-se-agrupan-capturas-con-subfigure]] · [[como-agrupar-capturas-con-subfigure-en-latex-para-manuales-d]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
