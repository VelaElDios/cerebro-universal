---
tipo: "dato"
titulo: "Métricas de calidad: 80 tests automatizados con node:test, comando único npm test"
temas: ["calidad", "grada-colchonera", "node-test", "procesos", "saas", "testing"]
claves: ["npm test", "node:test", "80 pruebas", "tests/userService.test.js", "tests/api.auth.test.js"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[calidad]] · [[grada-colchonera]] · [[node-test]] · [[procesos]] · [[saas]] · [[testing]]

- Framework nativo `node:test` (sin dependencias extra).
- 80 tests totales cubriendo:
  - `userService.test.js`: ≥5 unitarios de lógica usuarios (email repetido, pending login, self-delete, last-admin, etc.).
  - `accountConfirmation.test.js`: flujo confirmación correo.
  - `googleOAuth.test.js`: flujo OAuth.
  - `api.auth.test.js`, `api.users.test.js`, `api.database.test.js`: integración API real contra BD.
  - `config.test.js`, `frontend.test.js`: configuración y servir estáticos.
- Comando documentado en README: `npm test` (script `"test": "node --test"` en package.json).
- CI ejecuta mismo comando en contenedor con PostgreSQL 17.

> `node:test`; se ejecutan con `npm test` (80 pruebas)
> — `repo:saas/docs/revision-entrega.md`

Relacionado: [[resumen-de-pruebas-por-fichero-322-totales]] · [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[pipeline-ci-cd-github-actions-con-postgresql-17-real-docker]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
