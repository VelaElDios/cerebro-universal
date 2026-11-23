---
tipo: "decision"
titulo: "Diagramas de secuencia: límite de 6 participantes (agrupar o partir)"
temas: ["diagramas", "latex", "memoria", "plantuml", "tfg"]
claves: ["diagrama secuencia", "6 participantes", "agrupar", "partir", "resizebox", "sequence diagram", "participantes", "6", "pdflscape"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-23"
---

Temas: [[diagramas]] · [[latex]] · [[memoria]] · [[plantuml]] · [[tfg]]

Temas: [[diagramas]] · [[latex]] · [[memoria]] · [[plantuml]] · [[tfg]]

**Regla:** Los diagramas de secuencia no deben tener más de **6 participantes (lifelines)**.

**Si el sistema tiene más de 6 participantes, hay dos opciones válidas:**
1. **Agrupar** participantes relacionados bajo un mismo nombre (ej. «Vista + api.js + store» → «Frontend»).
2. **Dividir** en dos diagramas (p. ej., lado cliente / lado servidor).

**Sobre `\resizebox`:**  
- Solo se permite para **ajustes menores** (pequeños encogimientos).  
- **Está prohibido** usarlo para forzar más de 6 participantes en el ancho de página; eso reduce el texto a tamaño ilegible.  
- Como **último recurso**, se puede usar `pdflscape` para página horizontal.

> Diagramas de secuencia: **como mucho 6 participantes**. Si hay más, se agrupan (por ejemplo, «Vista + api.js» → «Frontend») o se parte en dos diagramas (lo que pasa en el navegador / lo que pasa en el servidor). `\resizebox` solo para encoger un poco, no para meter 9 columnas en el ancho de la página.
> — `../../memoria/reglas-tfg.md`

Relacionado:   · [[como-corregir-un-diagrama-de-secuencia-pgf-umlsd-que-falla-e]]
[[diagramas-ninguna-linea-flecha-atraviesa-cajas-codos-y-dista]] ·  
[[diagramas-de-secuencia-con-pgf-umlsd-sequencediagram]] ·  
[[arreglo-de-diagramas-segun-reglas-16-18-de-javier-feedback-1]] ·  
[[limites-y-calidad-de-diagramas-participantes-legibilidad-rou]] ·  
[[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re]] ·  
[[diagramas-de-secuencia-max-6-participantes-agrupar-o-partir]] ·  
[[diagramas-de-secuencia-max-6-participantes-agrupar-o-partir]]

> Diagramas de secuencia: **como mucho 6 participantes**. Si hay más, se agrupan (por ejemplo, «Vista + api.js» → «Frontend») o se parte en dos diagramas (lo que pasa en el navegador / lo que pasa en el servidor). `\resizebox` solo para encoger un poco, no para meter 9 columnas en el ancho de la página.
> — `../../memoria/reglas-tfg.md`

Fusionada con: Límite de 6 participantes en diagramas de secuencia
