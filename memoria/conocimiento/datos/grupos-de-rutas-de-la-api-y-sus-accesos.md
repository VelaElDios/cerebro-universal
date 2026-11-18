---
tipo: "dato"
titulo: "Grupos de rutas de la API y sus accesos"
temas: ["api", "grada-colchonera", "rutas", "saas"]
claves: ["health", "auth", "users", "juego", "prueba", "acceso público", "admin", "sesión"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-17"
---

Temas: [[api]] · [[grada-colchonera]] · [[rutas]] · [[saas]]

Resumen de endpoints por grupo: Salud: `GET /api/health` (público). Autenticación: `POST /api/auth/register`, `POST /api/auth/login`, `POST /api/auth/logout`, `GET /api/auth/me` (sesión), `GET /api/auth/confirm`, `POST /api/auth/resend-confirmation`, `GET /api/auth/providers`, `GET /api/auth/google`, `GET /api/auth/google/callback` (públicos salvo `me`). Usuarios (admin): `GET /api/users`, `GET /api/users/:id/active`, `PATCH /api/users/:id/role`, `DELETE /api/users/:id` (baja propia o admin). Juego (sesión, `desbloquear` admin): `GET /api/juego/perfil`, `POST /api/juego/partidas`, `POST /api/juego/partidas/:id/fin`, `POST /api/juego/contratar`, `POST /api/juego/entrenar`, `PUT /api/juego/identidad`, `GET /api/juego/ranking`, `POST /api/juego/desbloquear`. Prueba técnica: `POST /api/prueba/dominio` (público).

> | Salud | `GET /api/health` | Público | | Autenticación | `POST register`, `POST login`, `POST logout`, `GET me`, `GET confirm`, `POST resend-confirmation`, `GET providers`, `GET google`, `GET google/callback` | Público (salvo `me`) | | Usuarios | `GET /users`, `GET /users/:id/active`, `PATCH /users/:id/role`, `DELETE /users/:id` | Admin (la baja, propio o admin) | | Juego | `GET perfil`, `POST partidas`, `POST partidas/:id/fin`, `POST contratar`, `POST entrenar`, `PUT identidad`, `GET ranking`, `POST desbloquear` | Sesión (`desbloquear`, admin) |
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[modulos-del-backend-y-sus-responsabilidades]] · [[flujo-de-confirmacion-de-cuenta-por-correo-get-api-auth-conf]] · [[login-local-con-cuenta-pendiente-y-reenvio-de-confirmacion-p]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
