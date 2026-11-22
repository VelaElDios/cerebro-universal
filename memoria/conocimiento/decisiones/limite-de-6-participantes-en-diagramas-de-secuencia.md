---
tipo: "decision"
titulo: "Límite de 6 participantes en diagramas de secuencia"
temas: ["diagramas", "latex", "memoria", "tfg"]
claves: ["sequence diagram", "participantes", "6", "resizebox", "pdflscape"]
proyectos: []
fuentes: ["../../memoria/reglas-tfg.md"]
confianza: "verificado"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[diagramas]] · [[latex]] · [[memoria]] · [[tfg]]

Los diagramas de secuencia no deben tener más de 6 participantes (lifelines). Si el sistema tiene más, hay dos opciones válidas:
1. Agrupar participantes relacionados (ej. «Vista + api.js» → «Frontend»).
2. Dividir en dos diagramas (lado cliente / lado servidor).
Está prohibido usar `\resizebox` para forzar más de 6 participantes en el ancho de página; eso reduce el texto a tamaño ilegible. Como último recurso, se puede usar `pdflscape` para página horizontal.

> Diagramas de secuencia: **como mucho 6 participantes**. Si hay más, se agrupan (por ejemplo, «Vista + api.js» → «Frontend») o se parte en dos diagramas (lo que pasa en el navegador / lo que pasa en el servidor). `\resizebox` solo para encoger un poco, no para meter 9 columnas en el ancho de la página.
> — `../../memoria/reglas-tfg.md`

Relacionado: [[diagramas-de-secuencia-max-6-participantes-agrupar-o-partir]] · [[limites-y-calidad-de-diagramas-participantes-legibilidad-rou]] · [[como-corregir-diagramas-de-secuencia-pgf-umlsd-para-pasar-re]]
