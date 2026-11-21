---
tipo: "receta"
titulo: "Cómo escribir un diagrama de entidad-relación en TikZ legible"
temas: ["er", "latex", "tikz"]
claves: ["entity", "relationship", "node distance", "arrow", "label positioning"]
proyectos: ["memoria-procesos"]
fuentes: ["chapters/04-descripcion.tex (fig:modelo-datos)"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[er]] · [[latex]] · [[tikz]]

Para diagramas ER en TikZ: (1) Usar `node distance` suficiente (vertical ≥2.5cm, horizontal ≥4.0cm). (2) Dibujar relaciones con codos: `\draw[arrow] (A.east) -- ++(1.5,0) |- node[near start, above, font=\footnotesize] {etiqueta} (B.west);` para horizontal, y `\draw[arrow] (A.south) -- ++(0,-1.5) -| node[near start, left, font=\footnotesize] {etiqueta} (B.west);` para vertical. (3) Asegurar que la etiqueta está fuera de la línea (usar `near start` o `midway` con `above/left/right`). (4) No dibujar flechas que atraviesen cajas intermedias. (5) Usar `adjustbox{max width=\linewidth, max totalheight=0.6\textheight}` para escalar sin que las letras queden <8pt.

> La línea que une 'users' con 'juego_records' tiene la etiqueta 'tiene su mejor partida' atravesando la propia línea y chocando/cruzar con la caja de 'juego_records'.
> — `chapters/04-descripcion.tex (fig:modelo-datos)` (cita sin comprobar)

Relacionado: [[como-evitar-cruces-en-diagramas-tikz-pgf-umlsd]] · [[diagramas-ninguna-linea-flecha-atraviesa-cajas-codos-y-dista]] · [[diagrama-tikz-ancho-reducir-text-width-y-offsets-para-caber]] · [[como-corregir-diagramas-de-entidad-relacion-en-tikz-para-que]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
