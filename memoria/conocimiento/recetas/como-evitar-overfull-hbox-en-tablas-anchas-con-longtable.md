---
tipo: "receta"
titulo: "Cómo evitar overfull hbox en tablas anchas con longtable"
temas: ["latex", "longtable", "tablas"]
claves: ["@{}L{...}@{}", "\\allowbreak", "\\small", "\\emergencystretch"]
proyectos: ["memoria-procesos"]
fuentes: ["include/extra.tex y chapters/a4-trazabilidad.tex"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[longtable]] · [[tablas]]

(1) Usar @{} al inicio y final del preámbulo tabular para eliminar padding lateral; (2) Definir anchos de columna que sumen ≤ \linewidth (≈15.5 cm en esta plantilla); (3) Poner \allowbreak dentro de \texttt{} en identificadores largos (p.ej. \texttt{T1--T82\allowbreak}); (4) Usar \small en longtable (ya configurado); (5) Aumentar \emergencystretch si hace falta (ya 3em).

> \newcolumntype{L}[1]{>{\raggedright\let\newline\\\arraybackslash\hspace{0pt}}p{#1}} y \AtBeginEnvironment{longtable}{\small} y \setlength{\emergencystretch}{3em}
> — `include/extra.tex y chapters/a4-trazabilidad.tex` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
