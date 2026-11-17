---
tipo: "receta"
titulo: "BibTeX: autores corporativos con doble llave y year en todas las entradas"
temas: ["bibliografia", "bibtex", "latex"]
claves: ["autor corporativo", "doble llave", "year", "s.f.", "apalike"]
proyectos: ["memoria-procesos"]
fuentes: ["bib/ref.bib"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[bibliografia]] · [[bibtex]] · [[latex]]

Los autores que son organizaciones van con doble llave (`author = {{GitHub}}`). Todas las entradas llevan `year`; si la fuente no da fecha, `year = {s.f.}` (sin fecha). Esto evita que BibTeX separe mal el nombre y que apalike deje la cita vacía.

> @misc{express, author = {{Express}}, title = {Express, Node.js web application framework}, year = {s.f.}, howpublished = {\url{https://expressjs.com/}} }
> — `bib/ref.bib`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
