---
tipo: "receta"
titulo: "Que la última fila de una longtable no se quede sola en otra página"
temas: ["latex", "longtable", "tablas", "memoria", "tfg"]
claves: ["longtable", "\\\\*", "Total", "nopagebreak"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[longtable]] · [[tablas]]

Las últimas filas se terminan con `\\*` (prohíbe el salto de página ahí) y sin `\addlinespace`, que deja un hueco por donde sí puede partir:

```latex
\texttt{health.test.js} & 1 & /api/health \\*
\texttt{api.database.test.js} & CI & Recorrido completo \\*
\midrule
\textbf{Total} & \textbf{140} & Pruebas de la base SaaS \\
\bottomrule
```

Si aun así se queda sola, se reduce el aire entre filas de esa tabla (`\addlinespace[1pt]`).

> Las tablas largas van en `longtable` y su última fila (por ejemplo, el Total) no se queda sola en otra página
> — `memoria/reglas-tfg.md`

## Ampliación (2026-11-16, )
En tablas `longtable`, para evitar que la última fila (p. ej. una fila de «Total») quede sola en la página siguiente, se debe usar `\\*` (doble barra asterisco) en las últimas 2-3 filas del cuerpo de la tabla. `\\*` prohíbe el salto de página después de esa fila, manteniendo juntas las últimas filas.

Relacionado: [[tablas-largas-en-longtable-con-ultima-fila-acompanada]] · [[como-evitar-paginas-casi-vacias-tras-una-longtable]] · [[tablas-de-latex-que-no-se-pisan-columnas-p-y-addlinespace]] · [[reglas-de-maquetacion-de-tablas-alineacion-anchos-longtable]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
