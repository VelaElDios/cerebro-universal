---
tipo: "dato"
titulo: "Migración 004 y endpoint PUT /api/juego/identidad para mote y avatar"
temas: ["api", "backend", "base-datos", "donetonic", "grada-colchonera", "perfil", "scrum"]
claves: ["migracion 004", "PUT /api/juego/identidad", "mote", "avatar", "409", "P37"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/gestion/README.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[api]] · [[backend]] · [[base-datos]] · [[donetonic]] · [[grada-colchonera]] · [[perfil]] · [[scrum]]

- Migración 004 añade a juego_perfiles: mote (varchar 16, unique CI/AI), avatar_tipo (enum: 'jugador'|'entrenador'), avatar_id (FK).
- PUT /api/juego/identidad (protegido requireAuth):
  - Body: { mote, avatar_tipo, avatar_id }.
  - Valida mote: 3-16 chars, normaliza (lowercase + remove diacritics) para unicidad; devuelve 409 Conflict si existe.
  - Valida avatar: el usuario debe tener fichado ese jugador o desbloqueado ese entrenador.
  - Actualiza perfil y devuelve nuevo estado.
- El mote se muestra en ranking (P32) y cabecera (P20) en lugar del email.

> Migración 004 y PUT /api/juego/identidad. Mote de 3 a 16 caracteres, único sin distinguir mayúsculas ni tildes (409 si está cogido). Avatar con la cara de un jugador fichado o de un entrenador.
> — `repo:saas/docs/gestion/README.md` (cita sin comprobar)

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
