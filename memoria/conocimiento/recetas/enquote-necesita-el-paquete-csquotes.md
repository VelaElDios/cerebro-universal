---
tipo: "receta"
titulo: "\\enquote necesita el paquete csquotes"
temas: ["comillas", "csquotes", "enquote", "latex"]
claves: ["csquotes", "enquote", "undefined control sequence"]
proyectos: ["memoria-procesos"]
fuentes: ["memoria/lecciones.md"]
confianza: "propuesto"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[comillas]] · [[csquotes]] · [[enquote]] · [[latex]]

\enquote{...} da "Undefined control sequence" si el documento no carga csquotes. La plantilla principal ya lo carga en include/extra.tex, pero si se compilan archivos sueltos (anexos, diapositivas) hay que añadirlo en cada uno.

> Añadir \usepackage{csquotes}. Cada documento con su propio preámbulo (anexo, diapositivas...) lo necesita por separado.
> — `memoria/lecciones.md` (cita sin comprobar)

Relacionado: [[bibliografia-gestionada-con-bibtex-en-la-memoria-tfg]] · [[figuras-flotando-dentro-de-la-bibliografia-floatbarrier-ante]] · [[como-referenciar-capturas-de-pantalla-en-la-memoria-sin-copi]] · [[bibliografia-bibtex-apalike-con-autores-corporativos-en-dobl]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
