---
tipo: "receta"
titulo: "BibTeX: autores corporativos con doble llave y year en todas las entradas"
temas: ["bibliografia", "bibtex", "latex", "apalike", "autores corporativos", "bibliografía"]
claves: ["autor corporativo", "doble llave", "year", "s.f.", "apalike"]
proyectos: ["memoria-procesos"]
fuentes: ["bib/ref.bib", "memoria/lecciones.md", "lecciones del cerebro (memoria-procesos)"]
confianza: "verificado"
fecha: "2026-11-17"
actualizado: "2026-11-21"
---

Temas: [[bibliografia]] · [[bibtex]] · [[latex]]

Los autores que son organizaciones van con doble llave (`author = {{GitHub}}`). Todas las entradas llevan `year`; si la fuente no da fecha, `year = {s.f.}` (sin fecha). Esto evita que BibTeX separe mal el nombre y que apalike deje la cita vacía.

> @misc{express, author = {{Express}}, title = {Express, Node.js web application framework}, year = {s.f.}, howpublished = {\url{https://expressjs.com/}} }
> — `bib/ref.bib`

## Ampliación (2026-11-17, memoria-procesos)
En bib/ref.bib, todas las entradas deben tener year. Autores corporativos (GitHub, Google Cloud, Express, Node.js, PostgreSQL, DoneTonic, Universidad de Castilla-La Mancha) van con doble llave: author = {{GitHub}}. Si no hay fecha, year = {s.f.}. Esto evita citas como "[de Castilla-La Mancha, ]" o "[Neon, ]" sin año.

Relacionado: [[bibliografia-gestionada-con-bibtex-en-la-memoria-tfg]] · [[figuras-flotando-dentro-de-la-bibliografia-floatbarrier-ante]] · [[enquote-necesita-el-paquete-csquotes]] · [[bibliografia-bibtex-con-autores-corporativos-en-doble-llave]] · [[bibliografia-bibtex-apalike-autores-corporativos-con-doble-l]]

## Ampliación (2026-11-21, memoria-procesos)
Los autores que son organizaciones van con doble llave (author = {{GitHub}}). Todas las entradas llevan year; si la fuente no da fecha, year = {s.f.} (sin fecha). Ejemplo: @misc{neonlimits, author = {{Neon}}, title = {What are the limits and quotas for Neon's Free plan?}, year = {s.f.}, howpublished = {\url{https://neon.com/faqs/free-plan-limits-and-quotas}} }

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
