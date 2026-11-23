---
tipo: "decision"
titulo: "Cadenas \"La figura X muestra...\" prohibidas — prosa integrada con subfigure"
temas: ["figuras", "latex", "redaccion", "subcaption"]
claves: ["La figura X muestra", "subfigure", "prosa TFG", "regla 13 Javier"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md regla 13 y spec versión 4"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[figuras]] · [[latex]] · [[redaccion]] · [[subcaption]]

**Regla**: Cada captura debe estar integrada en un párrafo que explique la acción del usuario y la respuesta del sistema. No frases sueltas tipo "La figura 3.1 muestra el panel de administración."
**Patrón correcto**:
```latex
El panel de administración (Figura~\ref{fig:app-admin-full}) muestra contadores totales, un buscador por email y una tabla con email, rol, estado, fecha de alta y acciones. En móvil, la tabla se convierte en tarjetas (subfigura~\ref{fig:app-admin-movil}) y el menú se pliega (subfigura~\ref{fig:app-perfil-movil}).
\begin{figure}[htbp]
\centering
\begin{subfigure}{0.48\textwidth}
\includegraphics{...}\subcaption{Panel: tabla y buscador.}\label{fig:app-admin}
\end{subfigure}
\hfill
\begin{subfigure}{0.48\textwidth}
\includegraphics{...}\subcaption{Búsqueda filtrada.}\label{fig:app-admin-busqueda}
\end{subfigure}
\caption{Panel de administración: vista completa y búsqueda.}
\label{fig:app-admin-full}
\end{figure}
```
**Aplicado en**: 04-descripcion.tex (§ La aplicación) y 04b-juego.tex (§ Cómo se juega) — capturas agrupadas en `subfigure` 2 por fila (`0.48\textwidth`), caption general + subcaption por imagen, referenciadas desde la prosa.
**Pendiente**: Revisar capítulos 01, 03, 05, 06 y anexos para eliminar restos de "La figura X muestra...".

> Prosa de TFG, no listas de capturas: nada de una frase suelta «La figura X muestra…» por cada imagen. Las capturas se explican dentro de párrafos que cuentan qué hace el usuario y por qué la aplicación responde así. Las que van juntas se agrupan con subfigure.
> — `memoria/reglas-tfg.md regla 13 y spec versión 4` (cita sin comprobar)

Relacionado: [[prosa-de-tfg-vs-lista-de-capturas]] · [[como-escribir-prosa-de-tfg-integrando-capturas-sin-la-figura]] · [[prosa-de-tfg-sin-cadenas-la-figura-x-muestra-regla-13-javier]] · [[reescribir-frases-la-figura-x-muestra-como-prosa-integrada]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
