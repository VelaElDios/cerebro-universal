---
tipo: "decision"
titulo: "Longtables deben terminar con \\\\* antes de \\bottomrule (regla 7 Javier)"
temas: ["latex", "longtable", "maquetacion", "reglas-javier"]
claves: ["\\\\*", "\\bottomrule", "longtable", "fila huérfana", "regla 7"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[longtable]] · [[maquetacion]] · [[reglas-javier]]

En cada `longtable`, la penúltima y última fila de datos (incluyendo la fila de totales si existe) deben terminar con `\\*` en lugar de `\\` para evitar que la última fila quede huérfana en la página siguiente. El constructor debe revisar TODAS las longtables del documento (capítulos y anexos) y añadir `\\*` en las 2-3 últimas filas. Verificar en el PDF compilado que no hay filas solas al inicio de página.

> Las tablas largas van en longtable y su última fila (por ejemplo, el Total) no se queda sola en otra página: usa \\* en las últimas filas.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Relacionado: [[tablas-largas-en-longtable-con-ultima-fila-acompanada]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
