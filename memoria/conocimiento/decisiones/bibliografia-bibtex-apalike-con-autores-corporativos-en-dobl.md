---
tipo: "decision"
titulo: "Bibliografía BibTeX apalike con autores corporativos en doble llave"
temas: ["bibliografia", "bibtex", "latex"]
claves: ["apalike", "double braces", "corporate author", "year"]
proyectos: ["memoria-procesos"]
fuentes: ["bib/ref.bib"]
confianza: "verificado"
fecha: "2026-11-25"
actualizado: "2026-11-25"
---

Temas: [[bibliografia]] · [[bibtex]] · [[latex]]

En la memoria se usa BibTeX con estilo `apalike` (archivo `bib/ref.bib`). Reglas:
- Autores que son organizaciones (corporativos) se escriben con doble llave: `author = {{Express}}`.
- Todas las entradas deben tener `year` (usar `{s.f.}` si no hay fecha).
- URLs solo si están en las fuentes; usar `\url{...}` en `howpublished`.
- Todas las referencias deben ser citadas en el texto con `\cite{clave}`.
- Ejemplos en `bib/ref.bib`: express, githubflow, nodejs, postgresql, cloudrun, githubactions, scrumguide, enunciado, rfc6749, bcrypt, vampiresurvivors, donetonic.

> @misc{express, author = {{Express}}, title = {Express, Node.js web application framework}, year = {s.f.}, howpublished = {\url{https://expressjs.com/}}}
> — `bib/ref.bib`

Relacionado: [[bibliografia-bibtex-apalike-autores-corporativos-con-doble-l]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
