---
tipo: "receta"
titulo: "Títulos en negro y negrita en la plantilla ESIIAB-UCLM"
temas: ["latex", "plantilla", "tfg"]
claves: ["definecolor", "tema", "bfseries", "titleformat", "hidelinks"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[latex]] · [[plantilla]] · [[tfg]]

La plantilla pinta los títulos en azul con el color `tema`. Javier los quiere en negro y en negrita:

- En `include/colores.tex`: `\definecolor{tema}{RGB}{0,0,0}`.
- En `include/configuracion.tex`, en el `\titleformat` de section y subsection: `{\vspace{5pt} \bfseries \Large \color{tema}}` y `{\bfseries \large \color{tema}}`.
- Enlaces sin recuadros de color: `\hypersetup{hidelinks}` en `include/extra.tex`.

> Títulos en negro y en negrita, sin azul
> — `memoria/reglas-tfg.md`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
