---
tipo: "receta"
titulo: "Login local con cuenta pendiente y reenvío de confirmación (POST /api/auth/login)"
temas: ["auth", "grada-colchonera", "saas", "secuencia"]
claves: ["authenticate", "UnauthorizedError", "ForbiddenError", "AccountPendingError", "resendConfirmation", "401", "403", "202", "grada.sid"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[auth]] · [[grada-colchonera]] · [[saas]] · [[secuencia]]

El usuario envía email y contraseña desde la vista `entrar.js`. `api.js` llama a `POST /api/auth/login`. El backend `userService.authenticate()` devuelve:
- `UnauthorizedError` (email desconocido o contraseña mala) → 401 con mensaje genérico «Email o contraseña incorrectos» (log `auth.login_failed`).
- `ForbiddenError` (cuenta eliminada) → 403 FORBIDDEN.
- `AccountPendingError` (cuenta pendiente) → 403 ACCOUNT_PENDING; la vista muestra botón «Reenviar el correo de confirmación». Al pulsar, `api.js` llama a `POST /resend-confirmation` que siempre responde 202 con el mismo mensaje (exista o no la cuenta) para no revelar existencia.
- Si correcto: el servidor regenera la sesión, guarda `userId` y devuelve 200 con usuario y cookie `grada.sid` (httpOnly). El frontend llama a `ponerUsuario()` y redirige a `#/jugar`.

> U->>V: Email y contraseña V->>C: login(email, password) C->>A: POST /login A->>S: authenticate() alt Email desconocido o contraseña mala S-->>A: UnauthorizedError A-->>C: 401 «Email o contraseña incorrectos» (log auth.login_failed) else Cuenta eliminada S-->>A: ForbiddenError A-->>C: 403 FORBIDDEN else Cuenta pendiente S-->>A: AccountPendingError A-->>C: 403 ACCOUNT_PENDING C-->>V: Muestra «Reenviar el correo de confirmación» U->>V: Pulsa Reenviar V->>C: resendConfirmation(email) C->>A: POST /resend-confirmation A-->>C: 202 (mismo mensaje exista o no la cuenta) else Correcto A->>A: Regenera la sesión y guarda userId A-->>C: 200 usuario + cookie grada.sid (httpOnly) C-->>V: ponerUsuario() → #/jugar
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[maquina-de-estados-de-la-cuenta-de-usuario]] · [[flujo-de-registro-con-email-y-contrasena]] · [[flujo-de-confirmacion-de-cuenta-por-correo-get-api-auth-conf]] · [[recuperacion-de-sesion-al-cargar-get-api-auth-me-y-logout-po]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
