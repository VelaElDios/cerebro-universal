# Configuración del Hito 4: correo y Google OAuth

Este documento recoge la configuración concreta del Hito 4 (confirmación por correo y login con Google) tal como quedó en producción.

---

## Correo electrónico (SMTP)

- **Proveedor:** Gmail con contraseña de aplicación.
- **Puerto:** 465 (SMTP sobre SSL). Los puertos 25 y 587 sin cifrar suelen estar bloqueados en Cloud Run.
- **Secreto:** la contraseña de aplicación se guarda en Secret Manager de Google Cloud y se inyecta como variable de entorno `SMTP_URL`; nunca está en el repositorio.
- **Token de confirmación:** firmado con HMAC-SHA256, con propósito y caducidad de **24 horas**; no se guarda en la base de datos.
- **Reenvío:** `POST /api/auth/resend-confirmation` responde 202 en todos los casos para no revelar si la cuenta existe.

---

## Google OAuth 2.0

- **Aplicación registrada:** en Google Auth Platform, con estado de publicación «En producción» para usuarios externos.
- **Redirect URIs:** se registran las dos formas de URL de Cloud Run (la directa y la de `run.app`) para evitar `redirect_uri_mismatch`; la aplicación usa la variable `PUBLIC_URL` para construir la URI de retorno.
- **Flujo:** se guarda un `state` aleatorio en la sesión (un solo uso) antes de redirigir a Google; en el callback se compara y se borra antes de cambiar el código por el perfil.
- **Cuenta nueva:** si el email no existe, se crea la cuenta ya activa con `auth_provider = google`.
- **Baja con Google:** tras eliminar la cuenta, se cierra también la sesión local (PR #56).

---

## Pruebas asociadas

- `accountConfirmation.test.js`: 6 pruebas (correo con enlace, confirmación, enlace manipulado o caducado, cuenta eliminada, doble confirmación, reenvío).
- `googleOAuth.test.js`: 11 pruebas (redirección con state, cuenta nueva, existente, pendiente, state incorrecto o reutilizado, cancelación, email sin verificar, vuelta tras baja).
- `mailer.test.js`: 3 pruebas (SMTP o registro en local).
- `tokenSigner.test.js`: 3 pruebas (firma, manipulación y caducidad).
