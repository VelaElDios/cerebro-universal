---
tipo: "decision"
titulo: "Bibliografía BibTeX apalike: autores corporativos con doble llave y year en todas las entradas"
temas: ["apalike", "bibliografia", "bibtex", "latex"]
claves: ["author", "double braces", "year", "s.f.", "apalike"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/memoria/bibliografia.bib", "bib/ref.bib"]
confianza: "propuesto"
fecha: "2026-11-20"
actualizado: "2026-11-20"
---

Temas: [[apalike]] · [[bibliografia]] · [[bibtex]] · [[latex]]

|
  Ejemplos correctos en bib/ref.bib:
  @misc{express, author = {{Express}}, title = {Express, Node.js web application framework}, year = {s.f.}, howpublished = {\url{https://expressjs.com/}} }
  @misc{scrumguide, author = {Schwaber, K. and Sutherland, J.}, title = {The Scrum Guide}, year = {2020}, howpublished = {\url{https://scrumguides.org/scrum-guide.html}} }
  @misc{rfc6749, author = {Hardt, D. (ed.)}, title = {The OAuth 2.0 Authorization Framework}, year = {2012}, howpublished = {RFC 6749, Internet Engineering Task Force (IETF), \url{https://www.rfc-editor.org/rfc/rfc6749}} }
  @misc{bcrypt, author = {Provos, N. and Mazières, D.}, title = {A Future-Adaptable Password Scheme}, year = {1999}, howpublished = {Proceedings of the FREENIX Track, 1999 USENIX Annual Technical Conference, \url{https://www.usenix.org/legacy/events/usenix99/provos/provos.pdf}} }
  @misc{vampiresurvivors, author = {{poncle}}, title = {Vampire Survivors [videojuego]}, year = {2022}, howpublished = {Acceso anticipado 17/12/2021; versión 1.0 20/10/2022, \url{https://store.steampowered.com/app/1794680/Vampire_Survivors/}} }
  @misc{donetonic, author = {{DoneTonic}}, title = {Herramienta de gestión de proyectos ágiles usada para el backlog}, year = {s.f.}, howpublished = {\url{https://app.donetonic.com}} }
  @misc{enunciado, author = {{Universidad de Castilla-La Mancha}}, title = {Especificación del Proyecto. Procesos de Ingeniería del Software, curso 2026-2027 (Sprint 1)}, year = {2026} }

> author = {{GitHub}}, year = {s.f.}
problema: Sin doble llave, BibTeX trata «GitHub» como apellido «Hub»; sin year, apalike deja «[GitHub, ]».
solucion: Autores que son organizaciones → `author = {{Organización}}`. Todas las entradas llevan `year`; si no hay fecha → `year = {s.f.}`.
> — `repo:saas/memoria/bibliografia.bib` (cita sin comprobar)

## Ampliación (2026-11-20, memoria-procesos)
Aplicado en bib/ref.bib: express, githubflow, nodejs, postgresql, cloudrun, githubactions, donetonic tienen author = {{...}} y year = {s.f.}; rfc6749, bcrypt, vampiresurvivors tienen autores personales y year numérico; enunciado tiene author = {{Universidad de Castilla-La Mancha}} y year = {2026}.

Relacionado: [[bibliografia-bibtex-con-autores-corporativos-en-doble-llave]] · [[bibtex-autores-corporativos-con-doble-llave-y-year-en-todas]] · [[bibliografia-gestionada-con-bibtex-en-la-memoria-tfg]] · [[bibliografia-bibtex-con-apalike-y-referencias-obligatorias]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
