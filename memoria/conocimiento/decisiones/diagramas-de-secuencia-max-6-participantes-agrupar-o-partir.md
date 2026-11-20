---
tipo: "decision"
titulo: "Diagramas de secuencia: máx. 6 participantes (agrupar o partir)"
temas: ["diagramas", "latex", "memoria", "plantuml", "tfg"]
claves: ["diagrama secuencia", "6 participantes", "agrupar", "partir", "resizebox"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[diagramas]] · [[latex]] · [[memoria]] · [[plantuml]] · [[tfg]]

Límite duro: 6 «lifelines»/participantes por diagrama de secuencia. Si el sistema tiene más, agrupar relacionados bajo un mismo nombre (p. ej., «Frontend» = Vista + api.js + store) o dividir en dos diagramas (lado cliente / lado servidor). `\resizebox` solo para ajustes menores, nunca para forzar 9+ columnas.

> Diagramas de secuencia: **como mucho 6 participantes**. Si hay más, se agrupan (por ejemplo, «Vista + api.js» → «Frontend») o se parte en dos diagramas (lo que pasa en el navegador / lo que pasa en el servidor). `\resizebox` solo para encoger un poco, no para meter 9 columnas en el ancho de la página.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[diagramas-ninguna-linea-flecha-atraviesa-cajas-codos-y-dista]] · [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[arreglo-de-diagramas-segun-reglas-16-18-de-javier-feedback-1]] · [[limites-y-calidad-de-diagramas-participantes-legibilidad-rou]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re]]
