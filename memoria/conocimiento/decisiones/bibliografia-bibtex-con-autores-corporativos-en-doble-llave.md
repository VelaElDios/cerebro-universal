---
tipo: "decision"
titulo: "Bibliografía BibTeX con autores corporativos en doble llave y year obligatorio"
temas: ["bibliografia", "bibtex", "latex"]
claves: ["apalike", "double braces", "year", "s.f."]
proyectos: ["memoria-procesos"]
fuentes: ["fuentes/bibliografia-extra.md"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[bibliografia]] · [[bibtex]] · [[latex]]

En `bib/ref.bib`, cada entrada debe tener `year` (o `s.f.`). Autores corporativos: `author = {{Express}}`, `author = {{GitHub}}`, `author = {{OpenJS Foundation}}`, `author = {{The PostgreSQL Global Development Group}}`, `author = {{Google Cloud}}`, `author = {{Universidad de Castilla-La Mancha}}`. URLs solo si están en las fuentes. Estilo `apalike` con `\bibliographystyle{apalike}` y `\bibliography{bib/ref}`.

> Los autores que son organizaciones van con doble llave (`author = {{GitHub}}`). Todas las entradas llevan `year`; si la fuente no da fecha, `year = {s.f.}` (sin fecha).
> — `fuentes/bibliografia-extra.md` (cita sin comprobar)

Relacionado: [[bibtex-autores-corporativos-con-doble-llave-y-year-en-todas]] · [[bibliografia-gestionada-con-bibtex-en-la-memoria-tfg]] · [[figuras-flotando-dentro-de-la-bibliografia-floatbarrier-ante]] · [[bibliografia-bibtex-apalike-autores-corporativos-con-doble-l]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
