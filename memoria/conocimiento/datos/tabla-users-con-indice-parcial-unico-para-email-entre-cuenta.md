---
tipo: "dato"
titulo: "Tabla users con índice parcial único para email entre cuentas no eliminadas"
temas: ["grada-colchonera", "modelo-datos", "postgresql", "saas"]
claves: ["users", "email", "índice parcial", "migración 005", "baja lógica", "status deleted"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[modelo-datos]] · [[postgresql]] · [[saas]]

Tabla `users`: una fila por cuenta. `id` UUID PK. `email` normalizado (minúsculas, sin espacios) con índice único parcial que solo aplica a filas donde `status <> 'deleted'` (migración 005), permitiendo reutilizar el email tras una baja. `password_hash` (null en cuentas Google). `role` (`user` | `admin`). `status` (`pending` | `active` | `deleted`). `auth_provider` (`local` | `google`). `created_at`, `deleted_at`. `apodo` y `apodo_clave` (mote normalizado sin mayúsculas ni tildes, índice único). `avatar`.

> email normalizado (minúsculas, sin espacios) y único entre las cuentas no eliminadas (índice parcial de la migración 005), así que tras una baja se puede volver con el mismo email.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[correccion-de-unicidad-de-email-tras-baja-logica-indice-parc]] · [[maquina-de-estados-de-la-cuenta-de-usuario]] · [[gestion-de-sesiones-con-cookies-httponly-y-almacenamiento-en]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
