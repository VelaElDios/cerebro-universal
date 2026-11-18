---
tipo: "concepto"
titulo: "Gestión de sesiones con cookies httpOnly y almacenamiento en PostgreSQL"
temas: ["auth", "grada-colchonera", "procesos", "saas", "seguridad", "sesiones"]
claves: ["cookie httpOnly", "tabla session", "POST /api/auth/logout", "GET /api/auth/me", "iniciar()"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[auth]] · [[grada-colchonera]] · [[procesos]] · [[saas]] · [[seguridad]] · [[sesiones]]

- Login/registro exitoso → `Set-Cookie: sessionId=...; HttpOnly; Secure; SameSite=Lax` (valor = PK de tabla `session`).
- Tabla `session` en PostgreSQL: `id`, `user_id`, `created_at`, `expires_at`.
- `requireAuth` middleware lee cookie, busca en BD, adjunta `req.user` y `req.session`.
- `GET /api/auth/me` devuelve `{ user: { id, email, role, status } }` si hay sesión válida.
- `ui.js:iniciar()` llama a `GET /api/auth/me` al cargar; si 200, muestra vista autenticada.
- `POST /api/auth/logout` borra fila en `session` y envía `Set-Cookie: sessionId=; Max-Age=0`.
- Sesión sobrevive a reinicios del servidor (persistencia real en BD).

> Cookie `httpOnly` con la sesión guardada en PostgreSQL. Al cargar, la interfaz llama a `GET /api/auth/me`
> — `repo:saas/docs/revision-entrega.md`

Relacionado: [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]] · [[control-de-acceso-basado-en-roles-y-propiedad-requireauth-re]] · [[modulos-del-backend-y-sus-responsabilidades]] · [[recuperacion-de-sesion-al-cargar-get-api-auth-me-y-logout-po]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
