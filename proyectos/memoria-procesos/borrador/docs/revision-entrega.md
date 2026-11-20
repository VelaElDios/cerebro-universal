# Revisión de la entrega del Sprint 1 frente al enunciado

Fecha de la revisión: 12/10/2026 (primera entrega) y 27/10/2026 (cierre del sprint). Esta revisión recorre el enunciado del Sprint 1 requisito a requisito y apunta la evidencia concreta en el repositorio.

---

## Hito 1: repositorio, CI y despliegue

| Requisito del enunciado | Cumplimiento | Evidencia |
|---|---|---|
| Repositorio GitHub con flujo GitHub Flow | Sí | Rama `main` protegida, ramas `hito-1/integracion` y `hito-1/Tx-descripcion`; PR #1, #2; `CONTRIBUTING.md` |
| Integración continua con GitHub Actions | Sí | Workflow `ci.yml` con job *Pruebas* (`npm ci` + `npm test`) y job *Imagen Docker*; PR #3 |
| Despliegue continuo en URL pública | Sí | Render como primer despliegue (PR #4, #10); Cloud Run añadido después (P19, PR #27, #28) |
| Lógica de gestión de usuarios en memoria | Sí | `memoryUserRepository`, `userService`; PR #5, #6 |
| Pruebas unitarias automatizadas | Sí | Al menos 5 pruebas con `node:test`; PR #7 |
| Capa API de usuarios | Sí | `src/api/users.js`; PR #8 |

**Cierre del Hito 1:** PR #9 de `hito-1/integracion` a `main`; release `hito-1`.

---

## Hito 2: frontend separado y autenticación local

| Requisito del enunciado | Cumplimiento | Evidencia |
|---|---|---|
| Frontend separado del backend con cliente de comunicación propio | Sí | `public/js/api.js` (único `fetch`) y `public/js/ui.js`; PR #11, #12 |
| Registro e inicio de sesión locales con hash de contraseña | Sí | `userService.register` y `authenticate` con bcrypt; PR #13, #14 |
| Mantener la sesión al recargar y cerrarla en el servidor | Sí | `express-session` + tabla `session`; PR #15 |
| Rutas protegidas en el servidor (401 sin sesión) | Sí | Middleware `requireAuth`; PR #16 |

**Cierre del Hito 2:** PR #17 de `hito-2/integracion` a `main`; release `hito-2`.

---

## Hito 3: persistencia, secretos, roles y logs

| Requisito del enunciado | Cumplimiento | Evidencia |
|---|---|---|
| Persistencia en base de datos real (PostgreSQL) | Sí | `postgresUserRepository`, migraciones en `src/db/migrations/`; PR #18, #19 |
| Secretos fuera del código (variables de entorno) | Sí | `loadConfig.js`, `.env.example`; PR #20 |
| Roles usuario/administrador con primer administrador | Sí | `requireRole`, `requireSelfOrRole`, `userService.ensureAdmin`; PR #21, #22 |
| Listar usuarios, ver si están activos, cambiar roles (solo admin) | Sí | `GET /api/users`, `GET /api/users/:id/active`, `PATCH /api/users/:id/role`; PR #21, #22 |
| Baja lógica (nunca el último admin; email libre tras la baja) | Sí | `DELETE /api/users/:id` con `status = deleted`; PR #22 |
| Registro de la actividad relevante (logs) | Sí | `src/logger.js` y `requestLogger`; PR #23 |

**Cierre del Hito 3:** PR #24 de `hito-3/integracion` a `main`; release `hito-3`.

---

## Hito 4: correo, Google y errores

| Requisito del enunciado | Cumplimiento | Evidencia |
|---|---|---|
| Inicio de sesión con proveedor externo (Google OAuth 2.0) | Sí | `googleOAuth.js`, `GET /api/auth/google` y `/callback`; PR #40 |
| Confirmación de la cuenta por correo con reenvío | Sí | `accountConfirmationService`, token HMAC de 24 h, `GET /api/auth/confirm`, `POST /api/auth/resend-confirmation`; PR #38, #39 |
| Manejo de errores con información clara al usuario | Sí | `errorHandler.js` y avisos en el frontend; PR #37–#41 |
| README completo y revisión de la entrega | Sí | `README.md` y este documento; PR #25, #26, #30, #31 |
| Despliegue continuo en Google Cloud Run (P19, añadido por créditos de educación) | Sí | `Dockerfile`, workflow `deploy-cloud-run.yml`; PR #27, #28 |

**Cierre del sprint:** PR #29 (cierre del sprint) y #32 (revisión final y memoria). Release `sprint-1`.

---

## Alcance de la primera entrega (12/10/2026)

La primera entrega cubrió los Hitos 1–3 más P18 y P19: **16 PBIs** en total (P1–P14, P18 y P19), con sus tareas correspondientes de las 32 totales (T1–T32). El Hito 4 (P15–P17) se completó y comprobó en producción el 23/10/2026.

---

## Corrección detectada en la revisión

Durante la revisión frase a frase se detectó que el permiso de «comprobar si un usuario está activo» (`GET /api/users/:id/active`) no estaba correctamente restringido a administradores en una primera versión; la corrección se integró en el PR #30.
