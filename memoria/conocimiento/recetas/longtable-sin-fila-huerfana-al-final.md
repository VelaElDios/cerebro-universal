---
tipo: "receta"
titulo: "Evitar fila huérfana al final en longtable (LaTeX)"
temas: ["latex", "longtable", "memoria", "tablas", "tfg"]
claves: ["longtable", "bottomrule", "fila huérfana", "\\\\*", "Total", "nopagebreak"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-21"
---

Temas: [[latex]] · [[longtable]] · [[memoria]] · [[tablas]] · [[tfg]]

Temas: [[latex]] · [[longtable]] · [[tablas]]

**Técnica principal**  
Para que la última fila (p. ej. un total) y la `\bottomrule` no queden solas en la página siguiente, termina las **últimas 2-3 filas del cuerpo de la tabla con `\\*`** (doble barra + asterisco). `\\*` prohíbe el salto de página inmediatamente después de esa fila, manteniendo juntas las últimas filas.

**Detalles clave**
- **No uses `\addlinespace`** en esas filas finales: deja un hueco por donde LaTeX *sí* puede partir.
- Si aun así la fila queda huérfana, reduce el aire entre filas de esa tabla con `\addlinespace[1pt]`.

**Ejemplo completo**
```latex
\texttt{health.test.js}      & 1  & /api/health            \\*
\texttt{api.database.test.js} & CI & Recorrido completo     \\*
\midrule
\textbf{Total}               & \textbf{140} & Pruebas de la base SaaS \\*
\bottomrule
```
> Las tablas largas van en `longtable` y su última fila (por ejemplo, el Total) no se queda sola en otra página  
> — `memoria/reglas-tfg.md`

**Ampliación (2026-11-16)**  
La regla de las «últimas 2-3 filas con `\\*`» se aplica justo antes de `\bottomrule` (p. ej. `... \\* \hline \\* \bottomrule` o `... \\* \midrule \\* \bottomrule` según la estructura).

Relacionado:   · [[longtable-sin-fila-huerfana-al-final-regla-7-javier]]
[[como-anadir-en-longtables-para-evitar-filas-huerfanas]] · [[longtable-sin-fila-huerfana-al-final]] · [[tablas-largas-en-longtable-con-ultima-fila-acompanada]] · [[como-evitar-paginas-casi-vacias-tras-una-longtable]] · [[tablas-de-latex-que-no-se-pisan-columnas-p-y-addlinespace]] · [[reglas-de-maquetacion-de-tablas-alineacion-anchos-longtable]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]

> Las tablas largas van en `longtable` y su última fila (por ejemplo, el Total) no se queda sola en otra página: usa `\\*` en las últimas filas.
> — `memoria/reglas-tfg.md`
> Las tablas largas van en `longtable` y su última fila (por ejemplo, el Total) no se queda sola en otra página
> — `memoria/reglas-tfg.md`

Fusionada con: Que la última fila de una longtable no se quede sola en otra página

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
