---
tipo: "concepto"
titulo: "Manejo de errores tipados con formato común y feedback en UI (Hito 4 P17)"
temas: ["error-handling", "grada-colchonera", "hito-4", "procesos", "saas", "ux"]
claves: ["errorHandler.js", "ConflictError", "ForbiddenError", "ValidationError", "NotFoundError", "{ error: { code", "message } }", "capturas 02 y 03"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[error-handling]] · [[grada-colchonera]] · [[hito-4]] · [[procesos]] · [[saas]] · [[ux]]

- `src/services/` lanza clases de error propias: `ConflictError` (email repetido), `ForbiddenError` (sin permiso), `ValidationError` (datos inválidos), `NotFoundError` (recurso inexistente), etc.
- `src/api/errorHandler.js` (middleware Express final) captura cualquier error:
  - Si es error de negocio conocido → `res.status(código).json({ error: { code, message } })`.
  - Si es `Error` genérico → `500 { error: { code: 'INTERNAL', message: 'Error interno' } }` (loggea stack).
- Frontend `api.js` lanza excepción con `response.json()` parseado; `ui.js` muestra `error.message` en toast/alerta.
- Hito 4 (P17) añadió: estados de carga (spinners), timeouts en fetch, captura global `window.onerror`, mensajes user-friendly (no técnicos).

> Errores de negocio tipados que la API traduce a un formato común `{ error: { code, message } }`; la interfaz muestra cada mensaje. Su pulido (P17) está hecho en el Hito 4: avisos legibles, estados de carga y error, timeout y captura global de errores
> — `repo:saas/docs/revision-entrega.md`

Relacionado: [[frontend-spa-con-rutas-por-hash-y-vistas-cargadas-bajo-deman]] · [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[estrategia-de-pruebas-error-first-y-ci-como-requisito-de-mer]] · [[manejo-de-errores-de-principio-a-fin-de-errores-tipados-a-ui]] · [[cliente-api-con-timeout-de-15-s-y-manejo-de-apierror]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
