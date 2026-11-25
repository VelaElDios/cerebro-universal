---
tipo: "receta"
titulo: "Citas con autor largo que se salen del margen: usar breakcites"
temas: ["bibliografía", "bibtex", "latex"]
claves: ["breakcites", "overfull", "hbox", "cita", "autor corporativo"]
proyectos: ["memoria-procesos"]
fuentes: ["lecciones del cerebro (memoria-procesos)"]
confianza: "propuesto"
fecha: "2026-11-21"
actualizado: "2026-11-21"
---

Temas: [[bibliografía]] · [[bibtex]] · [[latex]]

Cargar breakcites (después de hyperref), que deja partir las citas entre líneas. Para encontrar el culpable, leer las líneas del log justo después del aviso «Overfull»: muestran el texto que se sale. Ejemplo: \usepackage{breakcites}

> Una cita con autor largo se sale del margen: breakcites. LaTeX mete cada cita en una caja que no se puede partir. Con autores largos («[Universidad de Castilla-La Mancha, 2026]») la cita no cabe al final de una línea y se sale del margen.
> — `lecciones del cerebro (memoria-procesos)` (cita sin comprobar)

Relacionado: [[como-evitar-overfull-hbox-en-rutas-y-diagramas]] · [[como-evitar-overfull-hbox-con-texttt-largo]] · [[bibliografia-gestionada-con-bibtex-en-la-memoria-tfg]] · [[bibliografia-bibtex-apalike-con-autores-corporativos-en-dobl]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
