---
tipo: "dato"
titulo: "Requisitos funcionales del Sprint 1 (13 RF) con trazabilidad"
temas: ["grada-colchonera", "requisitos", "saas", "sprint", "trazabilidad"]
claves: ["RF-01 a RF-13", "PBI", "userService", "api.auth", "postgres", "roles", "googleOAuth", "domainPolicy"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[requisitos]] · [[saas]] · [[sprint]] · [[trazabilidad]]

Tabla completa de 13 requisitos funcionales del Sprint 1 (base SaaS) con trazabilidad total: ID, descripción, hito, PBI asociado, ubicación exacta en código (servicios, endpoints, vistas, middlewares) y suites de pruebas que los cubren. Cubre: registro/login local (RF-01, RF-02), sesión y logout (RF-03), protección de rutas (RF-04), PostgreSQL real con migraciones (RF-05), roles y primer admin (RF-06), gestión de usuarios por admin (RF-07), baja lógica y re-registro (RF-08), logging (RF-09), confirmación email con reenvío (RF-10), OAuth Google (RF-11), manejo global de errores (RF-12), y prueba técnica de dominios permitidos (RF-13). Útil para generar matriz de trazabilidad en anexo B y para saber qué testear en cada módulo.

> | Id | Requisito | Hito | PBI | Dónde se cumple | Pruebas |
|---|---|---|---|---|---|---|
| RF-01 | Registro con email y contraseña (validación, email único, contraseña de 8 o más caracteres) | 2 | P8 | `userService.register`, `POST /api/auth/register`, vista `registro.js` | `userService`, `api.auth` |
| RF-02 | Inicio de sesión local, con el mismo mensaje si el email no existe o la contraseña es incorrecta | 2 | P8 | `userService.authenticate`, `POST /api/auth/login` | `api.auth` |
| RF-03 | Mantener la sesión al recargar y cerrarla en el servidor | 2 | P9 | `express-session` + tabla `session`, `GET /api/auth/me`, `POST /api/auth/logout` | `api.auth`, `api.database` (CI) |
| RF-04 | Rutas protegidas en el servidor (`401` sin sesión) | 2 | P10 | `requireAuth` | `api.users`, `api.auth` |
| RF-05 | Persistencia en una base de datos real | 3 | P11 | PostgreSQL (Neon), `postgresUserRepository`, migraciones | `userRepository`, `migrate`, `api.database` |
| RF-06 | Roles usuario y administrador, con un primer administrador | 3 | P13 | `requireRole`, `requireSelfOrRole`, `userService.ensureAdmin` | `userService`, `api.users`, `bootstrap` |
| RF-07 | Listar usuarios, ver si un usuario está activo y cambiar roles (solo administrador) | 3 | P13 | `GET /api/users`, `GET /api/users/:id/active`, `PATCH /api/users/:id/role`, vista `admin.js` | `api.users` |
| RF-08 | Darse de baja (y que el administrador pueda eliminar cuentas); nunca eliminar al último administrador; tras la baja se puede volver con el mismo email | 3 | P13 | `DELETE /api/users/:id` (baja lógica), vistas `perfil.js` y `admin.js` | `userService`, `api.users` |
| RF-09 | Registro de la actividad relevante | 3 | P14 | `src/logger.js`, `requestLogger` | `logger` |
| RF-10 | Confirmación de la cuenta por correo, con reenvío | 4 | P16 | `accountConfirmationService`, `tokenSigner`, `mailer`, `GET /api/auth/confirm`, `POST /api/auth/resend-confirmation` | `accountConfirmation`, `tokenSigner`, `mailer`, `api.auth` |
| RF-11 | Inicio de sesión con un proveedor externo (Google, OAuth 2.0) | 4 | P15 | `googleOAuth.js`, `GET /api/auth/google`, `GET /api/auth/google/callback`, `userService.loginWithOAuth` | `googleOAuth`, `userService` |
| RF-12 | Manejo de errores con información clara al usuario | 4 | P17 | `errorHandler.js`, `componentes.js`, `avisos.js`, `api.js` (timeout) | `api.*`, `frontend` |
| RF-13 | Prueba técnica: solo dominios de correo permitidos | Prueba | — | `domainPolicy.js`, `POST /api/prueba/dominio` | `domainPolicy` (13) |
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Relacionado: [[cada-entrega-solo-lleva-lo-de-su-sprint-alcance-coherente]] · Diagramas de secuencia con pgf-umlsd · [[desglose-del-alcance-del-sprint-1-por-hitos-y-fechas]] · [[tabla-de-trazabilidad-sprint-1-pbi-hito-titulo-tareas-prs-re]] · [[fechas-y-estructura-del-sprint-1-4-hitos-19-pbis-32-tareas]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
