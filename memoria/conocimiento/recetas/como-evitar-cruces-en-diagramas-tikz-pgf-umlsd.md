---
tipo: "receta"
titulo: "Cómo evitar cruces en diagramas TikZ/pgf-umlsd"
temas: ["diagramas", "latex", "pgf-umlsd", "tikz"]
claves: ["cruces", "flechas", "etiquetas", "node distance", "codos", "reglas 16-18"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-19"
actualizado: "2026-11-20"
---

Temas: [[diagramas]] · [[latex]] · [[pgf-umlsd]] · [[tikz]]

Para evitar cruces en diagramas: (1) Aumentar `node distance` (vertical: 0.8-1.0cm, horizontal: 5-6cm entre columnas). (2) Usar codos en flechas horizontales: `\draw[arrow] (origen.east) -- ++(1.2,0) |- node[near start, above] {etiqueta} (destino.west);`. (3) Añadir `\mess{}{}` vacíos entre bloques `sdblock` para crear espacio vertical. (4) Mover etiquetas con `near start/end`, `above/below`, `left/right`. (5) Reducir `text width` de nodos si es necesario (3.2cm normal, 4.5cm ancho). (6) Máximo 6 participantes por diagrama; si hay más, agrupar o partir en dos. (7) Verificar en PDF compilado, no solo en código.

> Ninguna línea ni flecha atraviesa una caja o un texto, y ninguna caja pisa a otra. Las flechas van de una caja a la siguiente (A → B, B → C), nunca de A a C pasando por encima de B; si hay que rodear, con codos (`|-`, `-|`) y separando bien las cajas (`node distance` suficiente). Las etiquetas de las flechas no se montan sobre las cajas.
> — `memoria/reglas-tfg.md`

Relacionado: [[diagramas-ninguna-linea-flecha-atraviesa-cajas-codos-y-dista]] · [[verificacion-visual-de-diagramas-tikz-y-pgf-umlsd-segun-regl]] · [[limites-y-calidad-de-diagramas-participantes-legibilidad-rou]] · [[diagramas-pgf-umlsd-sin-escalar-y-legibles-reglas-16-18]] · [[como-corregir-diagramas-de-entidad-relacion-en-tikz-para-que]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
