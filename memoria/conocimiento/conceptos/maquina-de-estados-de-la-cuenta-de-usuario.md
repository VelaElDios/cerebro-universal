---
tipo: "concepto"
titulo: "Máquina de estados de la cuenta de usuario"
temas: ["autenticación", "grada-colchonera", "modelo-datos", "saas"]
claves: ["pending", "active", "deleted", "registro local", "Google", "primer administrador", "baja", "sesión deja de valer", "email libre"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[autenticación]] · [[grada-colchonera]] · [[modelo-datos]] · [[saas]]

Estados y transiciones: `[*]` -> `pending` (registro local); `[*]` -> `active` (primer acceso Google o primer admin `ADMIN_EMAIL`); `pending` -> `active` (enlace correo o login Google con mismo email); `active` -> `deleted` (baja propia o admin); `pending` -> `deleted` (admin elimina); `deleted` -> `[*]`. En `deleted`: fila conservada, no puede entrar, sesión invalida en siguiente petición, sale del ranking, suelta email y mote (permite nueva cuenta con mismo email, también vía Google).

> pending --> active: enlace del correo / pending --> active: entra con Google con el mismo email / active --> deleted: baja propia o de un administrador / deleted --> [*]
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Relacionado: [[tabla-users-con-indice-parcial-unico-para-email-entre-cuenta]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
