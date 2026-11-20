---
tipo: "receta"
titulo: "Longtable sin fila huérfana al final"
temas: ["latex", "longtable", "tablas"]
claves: ["longtable", "bottomrule", "fila huérfana", "\\\\*"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[longtable]] · [[tablas]]

Para evitar que la última fila de una longtable (incluyendo `\bottomrule`) quede sola en la siguiente página, usar `\\*` en lugar de `\\` en las últimas 2-3 filas antes de `\bottomrule`. Esto prohíbe el salto de página entre esas filas. Ejemplo: `\hline \\* \bottomrule` o en las filas de datos finales: `... \\* \hline \\* \bottomrule`.

> Las tablas largas van en `longtable` y su última fila (por ejemplo, el Total) no se queda sola en otra página: usa `\\*` en las últimas filas.
> — `memoria/reglas-tfg.md`

Relacionado: [[como-anadir-en-longtables-para-evitar-filas-huerfanas]] · [[que-la-ultima-fila-de-una-longtable-no-se-quede-sola-en-otra]] · [[tablas-largas-en-longtable-con-ultima-fila-acompanada]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
