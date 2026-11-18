---
tipo: "receta"
titulo: "Arranque de la aplicación: configuración, migraciones y primer administrador (bootstrap)"
temas: ["arranque", "despliegue", "grada-colchonera", "migraciones", "saas"]
claves: ["server.js", "loadConfig", "bootstrap", "DATABASE_URL", "migrate", "ensureAdmin", "ADMIN_EMAIL", "ADMIN_PASSWORD", "Cloud Run"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[arranque]] · [[despliegue]] · [[grada-colchonera]] · [[migraciones]] · [[saas]]

1. `server.js` llama a `loadConfig`: lee y valida variables de entorno. En producción, si falta un secreto obligatorio → error y la app no arranca (Cloud Run mantiene la revisión anterior).
2. `bootstrap(config)`: si hay `DATABASE_URL` → ejecuta `migrate()` para aplicar migraciones pendientes; si no → usa repositorios en memoria (log `app.storage warn`).
3. `ensureAdmin(ADMIN_EMAIL, ADMIN_PASSWORD)`:
   - Si no existe → crea usuario `admin`, `active`, con hash bcrypt.
   - Si existe pero no es admin → actualiza rol a `admin` (no toca su contraseña).
   - Si ya es admin → sin cambios.
4. Log `admin.bootstrap` y `app.start`; la app queda lista.

> SV->>CF: Lee y valida las variables alt Producción sin un secreto obligatorio CF-->>SV: Error → la app no arranca (Cloud Run sigue con la versión anterior) end SV->>B: bootstrap(config) alt Hay DATABASE_URL B->>DB: migrate(): aplica las migraciones pendientes else B->>B: Repositorios en memoria (log app.storage warn) end B->>S: ensureAdmin(ADMIN_EMAIL, ADMIN_PASSWORD) alt No existe S->>DB: create(admin, active, hash) else Existe y no es admin S->>DB: update(role admin) else Ya es admin S-->>B: sin cambios (no se toca su contraseña) end B-->>SV: app lista (log admin.bootstrap, app.start)
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]] · [[creacion-del-primer-administrador-mediante-variables-de-ento]] · [[modulos-del-backend-y-sus-responsabilidades]] · [[seguridad-bcrypt-coste-10-sin-secretos-en-repo-secret-manage]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
