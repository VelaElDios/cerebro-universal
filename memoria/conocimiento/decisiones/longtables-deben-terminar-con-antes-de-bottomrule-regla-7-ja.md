---
tipo: "decision"
titulo: "Longtables deben terminar con \\\\* antes de \\bottomrule (regla 7 Javier)"
temas: ["latex", "longtable", "maquetacion", "reglas-javier", "tablas"]
claves: ["\\\\*", "\\bottomrule", "longtable", "fila huérfana", "regla 7"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "memoria/reglas-tfg.md (regla 7)"]
confianza: "verificado"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[longtable]] · [[maquetacion]] · [[reglas-javier]]

En cada `longtable`, la penúltima y última fila de datos (incluyendo la fila de totales si existe) deben terminar con `\\*` en lugar de `\\` para evitar que la última fila quede huérfana en la página siguiente. El constructor debe revisar TODAS las longtables del documento (capítulos y anexos) y añadir `\\*` en las 2-3 últimas filas. Verificar en el PDF compilado que no hay filas solas al inicio de página.

> Las tablas largas van en longtable y su última fila (por ejemplo, el Total) no se queda sola en otra página: usa \\* en las últimas filas.
> — `memoria/reglas-tfg.md`

Relacionado: [[tablas-largas-en-longtable-con-ultima-fila-acompanada]] · [[longtable-sin-fila-huerfana-al-final-regla-7-javier]] · [[como-anadir-en-longtables-para-evitar-filas-huerfanas]] · [[longtable-sin-fila-huerfana-al-final]]

## Ampliación (2026-11-20, memoria-procesos)
En cada longtable, las últimas 2-3 filas deben terminar con \\* en lugar de \\. Ejemplo: fila P18 \\*, fila P19 \\*, luego \bottomrule. Esto evita que LaTeX parta la tabla dejando la última fila sola en la siguiente página.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
