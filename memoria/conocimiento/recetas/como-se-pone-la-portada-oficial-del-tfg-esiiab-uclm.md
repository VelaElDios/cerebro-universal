---
tipo: "receta"
titulo: "Cómo se pone la portada oficial del TFG (ESIIAB-UCLM)"
temas: ["latex", "plantilla", "tfg"]
claves: ["portada.tex", "preambulo.tex", "Segunda portada", "textblock"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[plantilla]] · [[tfg]]

La plantilla trae dos portadas y solo vale una: la de `elements/portada.tex` (escudo, UCLM y ESII, tipo de trabajo, título, autor y fecha, centrado).

- `Memoria.tex` hace `\input{elements/portada}` antes de `\frontmatter`.
- En `elements/preambulo.tex` se borra el bloque «Segunda portada» (los `textblock` con `logouclm`, `logoesii` y `euroinf`, el título y el autor). Lo demás se queda: declaración de autoría, Resumen y Abstract.
- La declaración empieza en una página nueva con `\cleardoublepage` y `\setcounter{page}{1}`.

> Una sola portada: la oficial del TFG
> — `memoria/reglas-tfg.md`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
