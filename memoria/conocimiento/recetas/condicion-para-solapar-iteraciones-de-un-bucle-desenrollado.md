---
tipo: "receta"
titulo: "Condición para solapar iteraciones de un bucle (desenrollado / software pipelining)"
temas: ["ac", "bucles", "ilp", "planificacion"]
claves: ["dependencias entre iteraciones", "loop-carried", "desenrollado", "software pipelining"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/examenes/Enero2011.pdf"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[bucles]] · [[ilp]] · [[planificacion]]

Para solapar ejecución de iteraciones distintas (vía desenrollado o segmentación software) es necesario que no existan dependencias *entre* iteraciones (loop-carried dependencies). Las dependencias dentro de la misma iteración se gestionan con adelantamiento o reordenación.

> No presenta dependencias entre iteraciones
> — `repo:datos/temarios/AC/examenes/Enero2011.pdf`

Relacionado: [[se-pueden-solapar-iteraciones-de-un-bucle-si-no-hay-dependen]] · [[condicion-para-solapar-iteraciones-de-un-bucle-software-pipe]] · [[desenrollamiento-de-bucles-requiere-ausencia-de-dependencias]]
