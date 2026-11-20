---
tipo: "receta"
titulo: "Cómo añadir \\\\* en longtables para evitar filas huérfanas"
temas: ["latex", "longtable", "maquetacion"]
claves: ["\\\\bottomrule", "\\\\*", "longtable", "page break", "fila huérfana"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md (regla 7)"]
confianza: "verificado"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[longtable]] · [[maquetacion]]

En toda longtable, la última fila de datos antes de \bottomrule debe terminar con \\* en lugar de \\. Esto prohíbe el corte de página tras esa fila, evitando que la línea de \bottomrule o la fila de totales quede sola en la página siguiente. Aplicar sistemáticamente en todas las longtables del documento (capítulos y anexos).

> Las tablas largas van en longtable y su última fila (por ejemplo, el Total) no se queda sola en otra página: usa \\* en las últimas filas.
> — `memoria/reglas-tfg.md (regla 7)`

Relacionado: [[longtable-sin-fila-huerfana-al-final]] · [[longtables-deben-terminar-con-antes-de-bottomrule-regla-7-ja]] · [[que-la-ultima-fila-de-una-longtable-no-se-quede-sola-en-otra]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
