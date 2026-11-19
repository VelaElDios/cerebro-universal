---
tipo: "receta"
titulo: "Cómo agrupar capturas relacionadas con subfigure en LaTeX"
temas: ["figuras", "latex", "subcaption", "capturas", "maquetacion", "subfigure"]
claves: ["subfigure", "subcaption", "agrupación", "capturas"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex", "memoria/reglas-tfg.md (regla 13) y chapters/04-descripcion.tex (ejemplos actuales)"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[figuras]] · [[latex]] · [[subcaption]]

Para agrupar capturas relacionadas en una figura con caption general y subcaptions individuales: usar el entorno `subfigure` del paquete `subcaption` (ya cargado). Cada subfigure ocupa 0.48\textwidth para dos por fila. Usar `\hfill` entre subfigures para separarlas. El caption general va fuera con `\caption{...}\label{fig:...}`. Las subcaptions con `\subcaption{...}\label{fig:...}`. Para capturas verticales (móvil): `width=\linewidth,height=0.35\textheight,keepaspectratio`; horizontales: `width=\linewidth,height=0.30\textheight,keepaspectratio`.

> \begin{subfigure}{0.48\textwidth}\centering\includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/app/01-inicio.png}\subcaption{Página de inicio sin sesión.}\label{fig:app-inicio}\end{subfigure}
> — `chapters/04-descripcion.tex` (cita sin comprobar)

## Ampliación (2026-11-19, memoria-procesos)
|
  **Paquete ya cargado**: `subcaption` (en include/configuracion.tex).
  
  **Estructura estándar (dos por fila):**
  ```latex
  \begin{figure}[htbp]
  \centering
  \begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/carpeta/imagen1.png}
  \subcaption{Descripción breve de la primera captura.}
  \label{fig:etiqueta1}
  \end{subfigure}
  \hfill
  \begin{subfigure}{0.48\textwidth}
  \centering
  \includegraphics[width=\linewidth,height=0.35\textheight,keepaspectratio]{figs/capturas/carpeta/imagen2.png}
  \subcaption{Descripción breve de la segunda captura.}
  \label{fig:etiqueta2}
  \end{subfigure}
  \caption{Caption general que explica el conjunto.}
  \label{fig:etiqueta-general}
  \end{figure}
  ```
  
  **En el texto:**
  - Referencia al conjunto: `Figura~\ref{fig:etiqueta-general}`
  - Referencia a subfigura concreta: `subfigura~\subref{fig:etiqueta1} de la Figura~\ref{fig:etiqueta-general}`
  
  **Alturas recomendadas:**
  - Capturas móviles (verticales): `height=0.35\textheight` en subfigure, `0.42\textheight` en figure simple
  - Capturas desktop (horizontales): `height=0.35\textheight` en subfigure, `0.42\textheight` en figure simple
  - Si el grupo subfigure queda muy alto: envolver toda la `figure` en `\adjustbox{max totalheight=0.42\textheight,width=\textwidth}{...}`
  
  **Ejemplos ya correctos en el borrador:**
  - Figura~\ref{fig:app-inicio-registro} (Cap 4, inicio+registro)
  - Figura~\ref{fig:app-errores-acceso} (Cap 4, error entrar + sin permiso)
  - Figura~\ref{fig:app-perfil-baja} (Cap 4, perfil + baja)
  - Figura~\ref{fig:app-admin-full} (Cap 4, admin tabla + búsqueda)
  - Figura~\ref{fig:app-responsive} (Cap 4, admin móvil + perfil móvil)
  - Figura~\ref{fig:app-estados-especiales} (Cap 4, búsqueda vacía + 404)
  - Figura~\ref{fig:hito4-flujo} (Cap 4, 6 subfiguras en 3 filas)
  - Figura~\ref{fig:hito4-admin-estados-privacidad} (Cap 4, admin estados + privacidad)
  - Figura~\ref{fig:juego-menu-vestuario} (Cap 4b, menú + vestuario)
  - Figura~\ref{fig:juego-partida-mejora} (Cap 4b, partida + mejora)
  - Figura~\ref{fig:juego-jefe-ambiente} (Cap 4b, jefe + ambiente)
  - Figura~\ref{fig:juego-fin-pausa} (Cap 4b, fin + pausa)
  - Figura~\ref{fig:juego-club-pantallas-a} (Cap 4b, 4 pantallas club)
  - Figura~\ref{fig:juego-club-pantallas-b} (Cap 4b, 4 pantallas club)
  - Figura~\ref{fig:prueba-tecnica} (Cap 5, permitido + rechazado)
  - Figura~\ref{fig:produccion-verificacion} (Cap 5, correo + Google)
  - Figura~\ref{fig:donetonic-s2-capturas} (Anexo A1, gráficas + tablero S2)
  - Figura~\ref{fig:donetonic-s2-detalle} (Anexo A1, PBI detalle + tareas)
  
  **Pendientes de agrupar/reescribir:**
  - Cap 4 §6: varias figuras sueltas que deberían ir en subfigure (ya hecho en gran parte, revisar)
  - Cap 4b §2: lo mismo, ya agrupado en subfigures pero la prosa sigue siendo "La figura X muestra..."

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
