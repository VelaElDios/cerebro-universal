---
tipo: "decision"
titulo: "Longtable sin fila huérfana al final (regla 7 Javier)"
temas: ["latex", "longtable", "maquetacion", "tablas"]
claves: ["\\\\*", "\\bottomrule", "fila huérfana", "longtable"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-19"
actualizado: "2026-11-19"
---

Temas: [[latex]] · [[longtable]] · [[maquetacion]]

|
  En todas las `longtable`, las dos últimas filas antes de `\bottomrule` deben terminar con `\\*` en lugar de `\\` para evitar que la última fila (o la línea de totales) quede sola en la página siguiente.
  
  Ejemplo:
  ```latex
  \begin{longtable}{@{}L{3cm} L{10cm}@{}}
  \caption{Tabla larga.}\label{tab:ejemplo}\\
  \toprule
  \textbf{Col1} & \textbf{Col2} \\ \midrule \endfirsthead
  \toprule
  \textbf{Col1} & \textbf{Col2} \\ \midrule \endhead
  Dato 1 & Descripción 1 \\
  Dato 2 & Descripción 2 \\*
  Dato 3 & Descripción 3 \\*
  \bottomrule
  \end{longtable}
  ```
  
  Aplicar en: chapters/04-descripcion.tex (tablas RF, RJ, RNF, módulos, API), chapters/04b-juego.tex (sistemas, logros, fases), chapters/05-evaluacion.tex (pruebas, workflows, métricas), chapters/a1-desarrollo.tex (backlogs, trazabilidad, problemas, evolución), chapters/a4-trazabilidad.tex (tabla completa).

> Las tablas largas van en longtable y su última fila (por ejemplo, el Total) no se queda sola en otra página: usa \\* en las últimas filas.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

## Ampliación (2026-11-19, memoria-procesos)
|
  En cada `longtable`, añadir `\\*` antes de `\bottomrule` (o antes de la última fila de datos) para evitar que la última fila quede sola en la siguiente página.
  Ejemplo:
  ```latex
  \begin{longtable}{...}
  \caption{...}\label{...}\\
  \toprule
  ... \\
  \midrule
  ... \\*   % penúltima fila
  ... \\*   % última fila
  \bottomrule
  \end{longtable}
  ```

## Ampliación (2026-11-19, memoria-procesos)
Para evitar que la última fila de una `longtable` quede sola en la siguiente página, usar `\\*` (que prohíbe salto de página) en las 2-3 últimas filas antes de `\bottomrule`:
```latex
\begin{longtable}{@{}L{3cm} L{5cm} L{4cm}@{}}
\caption{Tabla larga.}\label{tab:ejemplo}\\
\toprule
\textbf{Col1} & \textbf{Col2} & \textbf{Col3} \\ \midrule \endfirsthead
\toprule
\textbf{Col1} & \textbf{Col2} & \textbf{Col3} \\ \midrule \endhead
Fila 1 & Dato & Dato \\
Fila 2 & Dato & Dato \\*
Fila 3 & Dato & Dato \\*
\bottomrule
\end{longtable}
```
Aplicar a TODAS las longtables de la memoria (capítulos 4, 4b, 5, anexos A1, A4).

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
