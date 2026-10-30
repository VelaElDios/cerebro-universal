---
titulo: "Tablas longtable anchas: usar @{} y anchos que sumen ≤ \\linewidth"
temas: ["latex", "tablas", "longtable"]
claves: ["overfull hbox", "longtable", "L{...}", "margin"]
estado: "propuesta"
veces: 1
fecha: "2026-10-30"
proyectos: ["memoria-procesos"]
---

Temas: [[latex]] · [[tablas]] · [[longtable]]

## Problema
Las tablas con columnas `L{...}` sumaban más de \linewidth (≈15.5 cm en esta plantilla) y el padding lateral de `array` hacía que el contenido se saliera del margen (overfull hbox 30–93 pt). El test lo detecta como error.

## Solución
Usar `@{}L{...}@{}` en la definición de la tabla (o `@{}` al inicio y final del preámbulo tabular) para eliminar el padding lateral, y reducir anchos de columna para que la suma sea ≤ \linewidth (p.ej., 13–14 cm). Para celdas con listas largas (tareas, PRs), usar `\texttt` con guiones bajos escapados y permitir saltos de línea con `\seqsplit` o dividir en varias filas.

## Ejemplo
|
  \begin{longtable}{@{}L{1.3cm} L{0.9cm} L{0.9cm} L{5.2cm} L{2.8cm}@{}}
  \caption{...}\label{...}\\
  \toprule ... \endfirsthead
  ...
  P18 & P18 & T27 & Completar el README & \#25 \\
  \bottomrule
  \end{longtable}

Origen: [[proyectos/memoria-procesos/bitacora|memoria-procesos]]
