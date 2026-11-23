---
tipo: "decision"
titulo: "Bibliografía BibTeX con apalike y referencias obligatorias"
temas: ["bibliografia", "bibtex", "latex"]
claves: ["apalike", "bib/ref.bib", "RFC 6749", "bcrypt", "Vampire Survivors", "enunciado"]
proyectos: ["memoria-procesos"]
fuentes: ["spec del proyecto, fuentes/bibliografia-extra.md"]
confianza: "propuesto"
fecha: "2026-11-23"
actualizado: "2026-11-23"
---

Temas: [[bibliografia]] · [[bibtex]] · [[latex]]

|
  Referencias en bib/ref.bib (todas citadas en el texto):
  - express, githubflow, nodejs, postgresql, cloudrun, githubactions, scrumguide, enunciado (del repo)
  - rfc6749 (OAuth 2.0), bcrypt, vampiresurvivors, donetonic (de fuentes/bibliografia-extra.md)
  Formato: `@misc{clave, author = {{Organización}}, title = {...}, year = {s.f.}, howpublished = {\url{...}}}` para orgs; `@misc{clave, author = {Apellido, Nombre}, title = {...}, year = {YYYY}, howpublished = {...}}` para personas. Todas con `urldate` si es web.
  Estilo: `\bibliographystyle{apalike}`, `\bibliography{bib/ref}`.

> Bibliografía (bib/ref.bib, apalike): Scrum Guide, Express, Node.js, PostgreSQL, OAuth 2.0 (RFC 6749), bcrypt, GitHub Flow, GitHub Actions, Google Cloud Run, Vampire Survivors (género survivor) y el enunciado. Solo URLs que estén en las fuentes; todas con year ({s.f.} si no hay fecha); autores que son organizaciones con doble llave; todas citadas.
> — `spec del proyecto, fuentes/bibliografia-extra.md` (cita sin comprobar)

Relacionado: [[cifras-clave-del-proyecto-contrastadas-con-fuentes]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
