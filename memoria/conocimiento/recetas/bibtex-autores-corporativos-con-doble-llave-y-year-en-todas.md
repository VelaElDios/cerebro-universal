---
tipo: "receta"
titulo: "BibTeX: autores corporativos con doble llave y year en todas las entradas"
temas: ["bibliografia", "bibtex", "latex", "apalike", "autores corporativos"]
claves: ["autor corporativo", "doble llave", "year", "s.f.", "apalike"]
proyectos: ["memoria-procesos"]
fuentes: ["bib/ref.bib", "memoria/lecciones.md"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-17"
---

Temas: [[bibliografia]] · [[bibtex]] · [[latex]]

Los autores que son organizaciones van con doble llave (`author = {{GitHub}}`). Todas las entradas llevan `year`; si la fuente no da fecha, `year = {s.f.}` (sin fecha). Esto evita que BibTeX separe mal el nombre y que apalike deje la cita vacía.

> @misc{express, author = {{Express}}, title = {Express, Node.js web application framework}, year = {s.f.}, howpublished = {\url{https://expressjs.com/}} }
> — `bib/ref.bib`

## Ampliación (2026-11-17, memoria-procesos)
En bib/ref.bib, todas las entradas deben tener year. Autores corporativos (GitHub, Google Cloud, Express, Node.js, PostgreSQL, DoneTonic, Universidad de Castilla-La Mancha) van con doble llave: author = {{GitHub}}. Si no hay fecha, year = {s.f.}. Esto evita citas como "[de Castilla-La Mancha, ]" o "[Neon, ]" sin año.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
