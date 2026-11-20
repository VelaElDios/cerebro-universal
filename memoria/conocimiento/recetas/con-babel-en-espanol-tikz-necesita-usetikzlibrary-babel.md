---
tipo: "receta"
titulo: "Con babel en español, TikZ necesita \\usetikzlibrary{babel}"
temas: ["babel", "flechas", "latex", "spanish", "tikz"]
claves: ["usetikzlibrary", "babel", "tikz", "flechas", ">=stealth"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/lecciones.md"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[babel]] · [[flechas]] · [[latex]] · [[spanish]] · [[tikz]]

Babel spanish vuelve activos los caracteres < y >. Entonces fallan >=stealth, las flechas -> y las comparaciones \ifdim ... > dentro de figuras TikZ y pgfplots. Solución: \usetikzlibrary{babel} en include/extra.tex (ya está). Esto permite usar flechas y comparaciones normales en diagramas TikZ/pgfplots con babel español.

> Cargar la librería babel de TikZ en el preámbulo.
> — `memoria/lecciones.md` (cita sin comprobar)

Relacionado: [[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] · [[diagramas-ninguna-linea-flecha-atraviesa-cajas-codos-y-dista]] · [[directlua-no-funciona-dentro-del-texto-de-un-node-usar-macro]] · [[flechas-reales-en-captions-y-texto-rightarrow-nunca]] · [[como-evitar-cruces-en-diagramas-tikz-pgf-umlsd]] · [[verificacion-visual-de-diagramas-tikz-y-pgf-umlsd-segun-regl]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
