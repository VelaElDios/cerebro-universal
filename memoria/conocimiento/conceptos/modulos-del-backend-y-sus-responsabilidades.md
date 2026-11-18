---
tipo: "concepto"
titulo: "Módulos del backend y sus responsabilidades"
temas: ["backend", "grada-colchonera", "modulos", "saas"]
claves: ["server.js", "bootstrap.js", "app.js", "config.js", "logger.js", "api/index.js", "api/auth.js", "api/users.js", "api/juego.js", "api/currentUser.js", "api/errorHandler.js", "services", "repositories", "integrations", "db/migrate.js"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[backend]] · [[grada-colchonera]] · [[modulos]] · [[saas]]

Módulos principales: `server.js` (entry point, carga config, llama `bootstrap`, escucha `PORT`, apagado ordenado con `SIGTERM`); `bootstrap.js` (elige PostgreSQL si hay `DATABASE_URL` o memoria, aplica migraciones, crea/promociona primer admin, configura correo SMTP o log); `app.js` (construye Express: JSON, sesión, `/api`, estáticos `public/`); `config.js`/`loadConfig.js` (leen y validan variables de entorno, exigen secretos en producción); `logger.js` (logs JSON por línea, niveles, ocultación datos sensibles); `api/index.js` (monta router: `requestLogger`, `currentUser`, `/health`, `/auth`, `/prueba`, `/users`, `/juego` con `requireAuth`, 404, manejador errores); `api/auth.js` (registro, confirmación, reenvío, login, Google, logout, `me`); `api/users.js` (admin users: `requireRole('admin')`, `requireSelfOrRole('admin')`); `api/juego.js` (perfil, partidas, contratos, entrenamiento, identidad, ranking, modo pruebas); `api/currentUser.js` (middlewares identidad, auth, autorización); `api/errorHandler.js` (traduce errores tipados a HTTP `{ error: { code, message } }`); `services/*` (reglas de negocio: `userService`, `accountConfirmationService`, `tokenSigner`, `passwordHasher`, `juegoService`, `domainPolicy`, `errors`); `repositories/*` (`memoryUserRepository`, `postgresUserRepository`, `memoryJuegoRepository`, `postgresJuegoRepository`); `integrations/mailer.js` (SMTP con `nodemailer` o log si no hay `SMTP_URL`); `integrations/googleOAuth.js` (URL autorización Google e intercambio código por perfil); `db/migrate.js` y `db/migrations/*.sql` (migraciones versionadas: 001 usuarios, 002 sesiones, 003 juego, 004 identidad, 005 email libre tras baja).

> server.js | Punto de entrada: carga la configuración, llama a bootstrap y escucha en PORT; para con orden al recibir SIGTERM
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]] · [[arquitectura-en-capas-cliente-servidor-verificada-api-logica]] · [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[grupos-de-rutas-de-la-api-y-sus-accesos]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
