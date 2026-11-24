---
tipo: "receta"
titulo: "Diagramas de secuencia legibles: máx. 6 participantes, flechas caja-a-caja, sin palabras partidas"
temas: ["latex", "memoria", "pgf-umlsd", "tfg"]
claves: ["sequence diagram", "participantes", "resizebox", "pdflscape", "node distance", "text width", "flechas", "codos"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[latex]] · [[memoria]] · [[pgf-umlsd]] · [[tfg]]

- Límite duro: 6 participantes (lifelines) por diagrama de secuencia.
- Si hay más: agrupar (ej. «Vista + api.js» → «Frontend») o dividir en dos diagramas (frontend / backend).
- `\resizebox` solo para reducciones menores; NO para forzar 9 columnas en ancho de página.
- Último recurso: página horizontal con `pdflscape`.
- Flechas de caja en caja (A→B, B→C), nunca saltando cajas (A→C por encima de B).
- Usar codos (`|-`, `-|`) y `node distance` suficiente para rodear cajas.
- Etiquetas de flechas sin montarse sobre cajas.
- Dentro de cajas: sin partir palabras/rutas (`sr-c/services`). Soluciones: `text width` más ancho, `\\` manual, o abreviar.
- Letras del dibujo ≥ 8-9 pt (tamaño pie de figura) una vez escalado; si no, replantear diagrama.

> Diagramas de secuencia: como mucho 6 participantes. Si hay más, se agrupan (por ejemplo, «Vista + api.js» → «Frontend») o se parte en dos diagramas (lo que pasa en el navegador / lo que pasa en el servidor). `\resizebox` solo para encoger un poco, no para meter 9 columnas en el ancho de la página.
> — `../../memoria/reglas-tfg.md`

Relacionado: Diagramas de secuencia pgf-umlsd — sintaxis válida y errores comunes · [[numeros-en-diagramas-de-secuencia-deben-coincidir-con-la-esp]] · [[limites-y-calidad-de-diagramas-participantes-legibilidad-rou]] · [[diagramas-de-secuencia-max-6-participantes-agrupar-o-partir]] · [[diagramas-de-secuencia-pgf-umlsd-reglas-para-pasar-revisar-m]]
