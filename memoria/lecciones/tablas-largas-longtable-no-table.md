---
titulo: "Tablas largas: longtable, no table"
temas: ["latex", "tablas"]
claves: ["Float too large", "no cabe en la página", "longtable"]
estado: "confirmada"
veces: 1
fecha: "2026-10-13"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[tablas]]

## Problema
Una tabla dentro de `\begin{table}` no puede partirse entre páginas. Si es más alta que la página (p. ej. 26 filas de trazabilidad), el log avisa «Float too large for page by … pt» y la tabla se corta por abajo.

## Solución
Para tablas de más de media página, `\usepackage{longtable}` y el entorno `longtable` (sin `table` alrededor), con `\endfirsthead` / `\endhead` para repetir la cabecera. El `\caption` y el `\label` van dentro del longtable.

## Ejemplo
```latex
\begin{longtable}{@{}L{1.2cm} L{1.2cm} L{7cm} L{2cm}@{}}
\caption{Trazabilidad tarea → PR.}\label{tab:traza}\\
\toprule PBI & Tarea & Descripción & PR \\ \midrule \endfirsthead
\toprule PBI & Tarea & Descripción & PR \\ \midrule \endhead
P1 & T1 & Crear repositorio & \#1 \\
\bottomrule
\end{longtable}
```

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
