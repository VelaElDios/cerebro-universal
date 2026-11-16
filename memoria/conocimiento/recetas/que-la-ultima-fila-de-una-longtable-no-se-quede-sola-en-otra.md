---
tipo: "receta"
titulo: "Que la última fila de una longtable no se quede sola en otra página"
temas: ["latex", "longtable", "tablas"]
claves: ["longtable", "\\\\*", "Total", "nopagebreak"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
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

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
