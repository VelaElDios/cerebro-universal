---
tipo: "concepto"
titulo: "Salto retardado (delayed branch) en planificación estática"
temas: ["ac", "compilador", "delayed-branch", "planificacion-estatica"]
claves: ["salto retardado", "delayed branch", "etapa ID", "slot de retardo", "compilador"]
proyectos: []
fuentes: ["repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[ac]] · [[compilador]] · [[delayed-branch]] · [[planificacion-estatica]]

En arquitecturas con salto retardado (p.ej. MIPS clásico), la instrucción inmediatamente posterior al branch (delay slot) se ejecuta siempre, independientemente de si el salto se toma. El compilador debe rellenar ese slot con una instrucción útil e inocua (que no rompa semántica si el salto no se toma). Si no hay instrucción útil, se pone NOP. La resolución en etapa ID limita el slot a una instrucción. Técnica puramente estática: el hardware no decide, el compilador sí.

> Las instrucciones emitidas después del salto terminarán de ejecutarse tanto si se toma el salto como si no. Suponiendo que el salto se resuelve completamente en la etapa ID, tan sólo sería la instrucción siguiente al salto
> — `repo:datos/temarios/AC/Tema3-Planificacion de instrucciones/Tema3.pdf` (cita sin comprobar)
