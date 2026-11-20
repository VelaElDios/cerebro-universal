---
tipo: "receta"
titulo: "Cómo evitar páginas con una sola imagen (Regla 8 de Javier)"
temas: ["latex", "maquetacion", "tfg"]
claves: ["regla 8", "height", "textheight", "flotante", "subfigure"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/reglas-tfg.md"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[latex]] · [[maquetacion]] · [[tfg]]

Cuando una figura (o subfiguras) queda sola en una página con poco texto, reducir el parámetro `height` en `\includegraphics` a un valor inferior a 0.42\textheight (p. ej., 0.22\textheight o 0.18\textheight). También ayuda quitar el especificador `!` del flotante (`[htbp]` en lugar de `[htbp!]`) para que LaTeX pueda mover la figura a una página con más texto. Si el capítulo termina ahí, añadir un párrafo de transición después de la figura para dar más texto en la página. Verificar con `revisar_maquetacion.py` página a página.

> Ninguna página con una sola imagen: capturas como mucho a height=0.42\textheight; diagramas grandes con max totalheight; figuras [htbp] con los parámetros de flotantes relajados, para que compartan página con el texto u otra figura.
> — `memoria/reglas-tfg.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
