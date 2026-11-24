---
tipo: "receta"
titulo: "Cómo evitar overfull hbox en tablas anchas con longtable"
temas: ["latex", "longtable", "tablas", "memoria-procesos"]
claves: ["@{}L{...}@{}", "\\allowbreak", "\\small", "\\emergencystretch"]
proyectos: ["memoria-procesos"]
fuentes: ["include/extra.tex y chapters/a4-trazabilidad.tex", "memoria/chapters/a4-trazabilidad.tex (corrección aplicada)"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[longtable]] · [[tablas]]

(1) Usar @{} al inicio y final del preámbulo tabular para eliminar padding lateral; (2) Definir anchos de columna que sumen ≤ \linewidth (≈15.5 cm en esta plantilla); (3) Poner \allowbreak dentro de \texttt{} en identificadores largos (p.ej. \texttt{T1--T82\allowbreak}); (4) Usar \small en longtable (ya configurado); (5) Aumentar \emergencystretch si hace falta (ya 3em).

> \newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}p{#1}} y \AtBeginEnvironment{longtable}{\small} y \setlength{\emergencystretch}{3em}
> — `include/extra.tex y chapters/a4-trazabilidad.tex` (cita sin comprobar)

## Ampliación (2026-11-23, memoria-procesos)
|
  1. Usar columnas `p{}` (alineadas arriba) en lugar de `m{}`.
  2. Sumar anchos de columnas + separadores (2\tabcolsep por columna) ≤ \linewidth.
  3. En celdas con texto largo sin espacios (rutas, rangos T1--T82), insertar `\allowbreak` en puntos naturales: `\texttt{T1\allowbreak--\allowbreak T82}`.
  4. Añadir `\setlength{\emergencystretch}{3em}` en preámbulo.
  5. `\AtBeginEnvironment{longtable}{\small}` para reducir tamaño de fuente.

Relacionado: [[tablas-anchas-en-latex-usar-y-anchos-que-sumen-linewidth]] · [[como-evitar-overfull-hbox-con-texttt-largo-en-longtable]] · [[como-evitar-overfull-hbox-en-rutas-y-diagramas]] · [[corregir-overfull-hbox-en-longtable-con-urls-largas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
