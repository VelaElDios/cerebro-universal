---
tipo: "decision"
titulo: "Límites y calidad de diagramas (participantes, legibilidad, routing)"
temas: ["diagramas", "latex", "memoria", "tfg", "tikz"]
claves: ["6 participantes", "node distance", "text width", "resizebox", "pdflscape", "codos", "|-", "-|"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-18"
actualizado: "2026-11-18"
---

Temas: [[diagramas]] · [[latex]] · [[memoria]] · [[tfg]] · [[tikz]]

1) Máx. 6 participantes en diagramas de secuencia; agrupar o dividir si hay más. 2) Letras del diagrama escalado ≥ 8-9 pt (tamaño pie de figura). 3) `\resizebox` solo para ajustes menores. 4) Último recurso: página horizontal con `pdflscape`. 5) No líneas/flechas atravesando cajas/texto; no cajas pisándose. 6) Flechas caja a caja (A→B, B→C), nunca saltando cajas; usar codos (`|-`, `-|`) y `node distance` suficiente. 7) Etiquetas de flechas no sobre cajas. 8) Dentro de cajas: no partir palabras/rutas; ampliar `text width`, saltos manuales `\\`, o abreviar.

> Diagramas de secuencia: **como mucho 6 participantes**. Si hay más, se agrupan (por ejemplo, «Vista + api.js» → «Frontend») o se parte en dos diagramas (lo que pasa en el navegador / lo que pasa en el servidor). `\resizebox` solo para encoger un poco, no para meter 9 columnas en el ancho de la página.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[diagramas-de-secuencia-max-6-participantes-agrupar-o-partir]] · [[diagramas-ninguna-linea-flecha-atraviesa-cajas-codos-y-dista]] · [[arreglo-de-diagramas-segun-reglas-16-18-de-javier-feedback-1]] · [[validacion-visual-de-diagramas-tikz-pgf-umlsd-en-pdf-reglas]] · [[limite-de-6-participantes-en-diagramas-de-secuencia]]
