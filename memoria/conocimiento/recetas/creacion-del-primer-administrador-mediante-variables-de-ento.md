---
tipo: "receta"
titulo: "Creación del primer administrador mediante variables de entorno al arranque (ensureAdmin)"
temas: ["admin", "bootstrap", "grada-colchonera", "procesos", "saas", "variables-entorno"]
claves: ["ADMIN_EMAIL", "ADMIN_PASSWORD", "ensureAdmin", "bootstrap.js", "sin contraseñas en código"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[admin]] · [[bootstrap]] · [[grada-colchonera]] · [[procesos]] · [[saas]] · [[variables-entorno]]

En `src/bootstrap.js` (ejecutado al iniciar `src/app.js`):
- Si existen `ADMIN_EMAIL` y `ADMIN_PASSWORD` en `process.env`:
  - Busca usuario con ese email.
  - Si no existe: crea usuario con `role: 'admin'`, `status: 'active'`, hash de `ADMIN_PASSWORD`.
  - Si existe y no es admin: lo promueve a admin.
  - Si ya es admin: no hace nada.
- Permite desplegar sin intervención manual en BD y sin secretos en código.
- En producción (Cloud Run) las variables vienen de Secret Manager.
- En local: definirlas en `.env` (ignorado por git).

> Con las variables `ADMIN_EMAIL` y `ADMIN_PASSWORD` al arrancar (`ensureAdmin`): no hay contraseñas en el código y no hace falta tocar la base de datos a mano
> — `repo:saas/docs/revision-entrega.md`

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
