---
tipo: "decision"
titulo: "Diagramas: ninguna línea/flecha atraviesa cajas, codos y distancia suficiente"
temas: ["diagramas", "latex", "memoria", "plantuml", "tfg", "tikz"]
claves: ["flechas atraviesan cajas", "codos", "|-", "-|", "node distance"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[diagramas]] · [[latex]] · [[memoria]] · [[plantuml]] · [[tfg]] · [[tikz]]

Reglas de layout para diagramas (TikZ, PlantUML, Mermaid, etc.): 1) Flechas conectan cajas adyacentes (A→B, B→C), no saltan cajas intermedias. 2) Si la ruta directa choca, usar codos ortogonales (`|-` = vertical luego horizontal; `-|` = horizontal luego vertical). 3) Aumentar `node distance` (o `ranksep`/`nodesep` en GraphViz) para que haya espacio. 4) Etiquetas de flechas (`edge labels`) colocadas fuera de cajas.

> Ninguna línea ni flecha atraviesa una caja o un texto, y ninguna caja pisa a otra. Las flechas van de una caja a la siguiente (A → B, B → C), nunca de A a C pasando por encima de B; si hay que rodear, con codos (`|-`, `-|`) y separando bien las cajas (`node distance` suficiente). Las etiquetas de las flechas no se montan sobre las cajas.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[dentro-de-cajas-no-se-parten-palabras-ni-rutas-text-width-ma]] · [[diagramas-de-secuencia-max-6-participantes-agrupar-o-partir]] · [[arreglo-de-diagramas-segun-reglas-16-18-de-javier-feedback-1]] · [[limites-y-calidad-de-diagramas-participantes-legibilidad-rou]] · [[como-evitar-cruces-en-diagramas-tikz-pgf-umlsd]]
