---
tipo: "concepto"
titulo: "Formato de logs JSON y eventos registrados"
temas: ["grada-colchonera", "logging", "observabilidad", "saas"]
claves: ["JSON", "X-Request-Id", "event", "level", "msg", "datos sensibles oculto"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[logging]] · [[observabilidad]] · [[saas]]

Logging estructurado: una línea JSON por evento en stdout (Cloud Logging en producción). Campos obligatorios: `time` (ISO), `level` (info/error/warn), `event` (nombre del evento), `msg` (mensaje legible), `data` (objeto con contexto). Cada request lleva header `X-Request-Id` que se propaga a todas las líneas de log de esa petición. Eventos definidos: ciclo de vida (`app.start`, `app.stop`, `app.storage`, `app.mail`, `admin.bootstrap`), HTTP (`http.request`, `http.error`), autenticación (`user.registered`, `auth.login`, `auth.logout`, `auth.login_failed`, `auth.forbidden`, `auth.oauth_denied`, `auth.oauth_failed`), correo (`mail.confirmation_sent`, `mail.failed`, `mail.not_sent`), confirmación (`user.confirmed`, `user.confirm_failed`), administración (`user.role_changed`, `user.deleted`), juego (`juego.identidad`). Datos sensibles (passwords, tokens, emails) se reemplazan por `[oculto]` antes de loguear.

> Una línea JSON por evento en la salida estándar (Cloud Logging en producción), con time, level, event, msg y datos, por ejemplo {"time":"2026-10-12T10:00:00.000Z","level":"info","event":"auth.login","msg":"Inicio de sesión","userId":"..."}. Cada petición lleva un identificador (X-Request-Id) que aparece en todas sus líneas. Eventos: app.start, app.stop, app.storage, app.mail, admin.bootstrap, http.request, http.error, user.registered, auth.login, auth.logout, auth.login_failed, auth.forbidden, mail.confirmation_sent, mail.failed, mail.not_sent, user.confirmed, user.confirm_failed, auth.oauth_denied, auth.oauth_failed, user.role_changed, user.deleted y juego.identidad. Los datos sensibles se sustituyen por [oculto].
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]] · [[gestion-de-sesiones-con-cookies-httponly-y-almacenamiento-en]] · [[modulos-del-backend-y-sus-responsabilidades]] · [[manejo-de-errores-de-principio-a-fin-de-errores-tipados-a-ui]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
