---
tipo: "receta"
titulo: "Inicio de sesión Google OAuth 2.0 con state anti-CSRF e intercambio en servidor"
temas: ["auth", "google", "grada-colchonera", "oauth", "procesos", "saas"]
claves: ["googleOAuth.js", "authorization code", "state", "authProvider: google", "public/privacidad.html"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[auth]] · [[google]] · [[grada-colchonera]] · [[oauth]] · [[procesos]] · [[saas]]

Implementación completa server-side:
- Frontend redirige a Google con `state` aleatorio guardado en sesión.
- Callback `GET /api/auth/google/callback` recibe `code` y `state`, valida `state` contra sesión.
- Servidor intercambia `code` por tokens con Google (secretos solo en backend).
- Obtiene perfil (email, nombre), busca/crea usuario con `authProvider: 'google'` y `status: 'active'`.
- Crea sesión igual que login local (cookie httpOnly + BD).
- Requiere `GOOGLE_CLIENT_ID`, `GOOGLE_CLIENT_SECRET`, `GOOGLE_CALLBACK_URL` en variables de entorno.
- Política de privacidad en `public/privacidad.html` para cumplir requisitos de Google.

> Google OAuth 2.0 (código de autorización) con `state` anti-CSRF; el intercambio del código se hace en el servidor y la cuenta se crea con `authProvider: google`. La app de Google está publicada, con su política de privacidad
> — `repo:saas/docs/revision-entrega.md`

Relacionado: [[login-con-google-oauth-2-0-codigo-de-autorizacion-state-en-s]] · [[como-crear-cliente-oauth-de-google-para-la-grada-colchonera]] · [[comportamiento-de-cuentas-segun-metodo-de-registro-y-estado]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
