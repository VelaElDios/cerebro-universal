---
tipo: "receta"
titulo: "Figuras flotando dentro de la bibliografía: \\FloatBarrier antes"
temas: ["bibliografia", "figuras", "floatbarrier", "latex", "placeins"]
claves: ["FloatBarrier", "placeins", "bibliografia", "figura flotante"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/lecciones.md"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[bibliografia]] · [[figuras]] · [[floatbarrier]] · [[latex]] · [[placeins]]

Una figura flotante pendiente acaba colocándose en medio de la bibliografía. Solución: \usepackage{placeins} (ya en include/extra.tex) y \FloatBarrier antes de \printbibliography o \bibliography. En Memoria.tex ya está \cleardoublepage antes de la bibliografía, pero añadir \FloatBarrier asegura que no quede ninguna figura flotando después.

> Cargar placeins y poner \FloatBarrier justo antes de la bibliografía: obliga a colocar antes todas las figuras pendientes.
> — `memoria/lecciones.md` (cita sin comprobar)

Relacionado: [[bibliografia-gestionada-con-bibtex-en-la-memoria-tfg]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
