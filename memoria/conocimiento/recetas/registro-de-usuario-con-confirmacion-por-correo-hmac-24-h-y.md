---
tipo: "receta"
titulo: "Registro de usuario con confirmación por correo (HMAC, 24 h) y estado pending"
temas: ["auth", "email-confirmation", "grada-colchonera", "procesos", "saas"]
claves: ["POST /api/auth/register", "GET /api/auth/confirm", "accountConfirmationService", "mailer", "REQUIRE_EMAIL_CONFIRMATION"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[auth]] · [[email-confirmation]] · [[grada-colchonera]] · [[procesos]] · [[saas]]

Flujo completo implementado y verificado:
1. `POST /api/auth/register` valida email único y contraseña ≥ 8 chars. Crea usuario con `status: 'pending'`.
2. `accountConfirmationService` genera token HMAC (expira 24 h) y `mailer` envía enlace `GET /api/auth/confirm?token=...`.
3. `GET /api/auth/confirm` verifica HMAC, cambia `status` a `'active'`.
4. Mientras `status === 'pending'`, `POST /api/auth/login` devuelve `403 { code: 'ACCOUNT_PENDING' }`.
5. Endpoint para reenviar correo de confirmación (no documentado en la tabla pero implícito en "puede pedir otro correo").
6. Variable `REQUIRE_EMAIL_CONFIRMATION=true` por defecto; si se pone `false`, se salta el paso pending.

> Al registrarse la cuenta queda `pending` y se envía un correo con un enlace firmado (HMAC, 24 h). `GET /api/auth/confirm` la activa; una cuenta pendiente no puede entrar (`403 ACCOUNT_PENDING`) y puede pedir otro correo. `REQUIRE_EMAIL_CONFIRMATION` está activo por defecto
> — `repo:saas/docs/revision-entrega.md`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
