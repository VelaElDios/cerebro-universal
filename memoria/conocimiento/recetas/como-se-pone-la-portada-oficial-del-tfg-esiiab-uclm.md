---
tipo: "receta"
titulo: "Cómo se pone la portada oficial del TFG (ESIIAB-UCLM)"
temas: ["latex", "plantilla", "tfg", "memoria"]
claves: ["portada.tex", "preambulo.tex", "Segunda portada", "textblock"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "../../memoria/reglas-tfg.md"]
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

## Ampliación (2026-11-16, )
La portada es única y obligatoria: se usa exclusivamente `elements/portada.tex` que incluye escudo, universidad, escuela, tipo de trabajo, título, autor y fecha, todo centrado. En `Memoria.tex` se hace `\input{elements/portada}`. No se añade ninguna otra portada, incluida la «segunda portada» con logos UCLM/ESII de `elements/preambulo.tex`. Esta regla es inquebrantable y la comprueba el script de maquetación.

Relacionado: [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]] · [[comprobar-la-maquetacion-de-un-tfg-automaticamente]] · [[estructura-de-8-capitulos-para-la-memoria-tfg-esiiab-uclm]] · [[paso-1-completado-preambulo-tex-ya-cumple-regla-1-una-sola-p]] · [[resumen-y-abstract-en-elements-preambulo-tex-con-formato-ofi]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
