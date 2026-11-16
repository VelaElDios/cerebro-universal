---
tipo: "tema"
titulo: "auth"
notas: 10
---
# auth

Nodo del mapa del Cerebro con todo lo que se sabe de «auth» (este archivo se genera solo).

## Recetas (cómo lo hacemos)

- 🧪 [[memoria/conocimiento/recetas/flujo-de-confirmacion-de-cuenta-por-correo-get-api-auth-conf|Flujo de confirmación de cuenta por correo (GET /api/auth/confirm)]]
- 🧪 [[memoria/conocimiento/recetas/inicio-de-sesion-google-oauth-2-0-con-state-anti-csrf-e-inte|Inicio de sesión Google OAuth 2.0 con state anti-CSRF e intercambio en servidor]]
- 🧪 [[memoria/conocimiento/recetas/login-con-google-oauth-2-0-codigo-de-autorizacion-state-en-s|Login con Google OAuth 2.0 (código de autorización, state en sesión)]]
- 🧪 [[memoria/conocimiento/recetas/login-local-con-cuenta-pendiente-y-reenvio-de-confirmacion-p|Login local con cuenta pendiente y reenvío de confirmación (POST /api/auth/login)]]
- 🧪 [[memoria/conocimiento/recetas/recuperacion-de-sesion-al-cargar-get-api-auth-me-y-logout-po|Recuperación de sesión al cargar (GET /api/auth/me) y logout (POST /api/auth/logout)]]
- 🧪 [[memoria/conocimiento/recetas/registro-de-usuario-con-confirmacion-por-correo-hmac-24-h-y|Registro de usuario con confirmación por correo (HMAC, 24 h) y estado pending]]

## Decisiones (y por qué)

- ⚖️ [[memoria/conocimiento/decisiones/proteccion-del-ultimo-administrador-al-cambiar-rol-patch-api|Protección del último administrador al cambiar rol (PATCH /api/users/:id/role) y al darse de baja (DELETE /api/users/:id)]]

## Conceptos

- 💡 [[memoria/conocimiento/conceptos/cadena-de-middlewares-para-peticion-protegida-y-autorizacion|Cadena de middlewares para petición protegida y autorización por roles (requireAuth, requireRole)]]
- 💡 [[memoria/conocimiento/conceptos/control-de-acceso-basado-en-roles-y-propiedad-requireauth-re|Control de acceso basado en roles y propiedad (requireAuth, requireRole, requireSelfOrRole)]]
- 💡 [[memoria/conocimiento/conceptos/gestion-de-sesiones-con-cookies-httponly-y-almacenamiento-en|Gestión de sesiones con cookies httpOnly y almacenamiento en PostgreSQL]]

## Temas relacionados

[[grada-colchonera]] · [[saas]] · [[procesos]] · [[rbac]] · [[secuencia]] · [[google]] · [[oauth]] · [[middleware]] · [[autorizacion]] · [[middlewares]] · [[seguridad]] · [[sesiones]]
