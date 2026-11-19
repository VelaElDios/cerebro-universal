---
tipo: "receta"
titulo: "Títulos en negro y negrita en la plantilla ESIIAB-UCLM"
temas: ["latex", "plantilla", "tfg", "memoria"]
claves: ["definecolor", "tema", "bfseries", "titleformat", "hidelinks"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md", "../../memoria/reglas-tfg.md"]
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

## Ampliación (2026-11-16, )
Los títulos de sección y subsección deben ser negros (`\definecolor{tema}{RGB}{0,0,0}`) y en negrita (`\bfseries`). Además, los enlaces hipertexto no llevan recuadros de color: se configura `\hypersetup{hidelinks}`. Esto anula el estilo por defecto de la plantilla que usa azul para títulos y enlaces.

Relacionado: [[como-se-pone-la-portada-oficial-del-tfg-esiiab-uclm]] · [[quitar-las-paginas-en-blanco-entre-capitulos]] · [[resumen-y-abstract-en-elements-preambulo-tex-con-formato-ofi]] · [[formato-de-titulos-y-enlaces-en-la-memoria]] · [[portada-oficial-unica-y-elementos-fijos-de-la-plantilla]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
