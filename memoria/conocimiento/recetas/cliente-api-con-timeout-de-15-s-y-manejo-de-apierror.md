---
tipo: "receta"
titulo: "Cliente API con timeout de 15 s y manejo de ApiError"
temas: ["api-client", "frontend", "grada-colchonera", "saas"]
claves: ["api.js", "fetch", "AbortController", "timeout 15s", "ApiError", "401 sesión caducada"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[api-client]] · [[frontend]] · [[grada-colchonera]] · [[saas]]

Implementación en `public/js/api.js`: único punto que usa `fetch`. Cada petición crea `AbortController` con `setTimeout` de 15 s para abortar si no responde. Respuestas con status >= 400 se convierten en instancia `ApiError` con propiedades `status`, `code`, `message`. Si el status es 401 y hay sesión activa, dispara evento para que la UI sepa que la sesión caducó (p.ej. redirigir a login). Uso: `api.register(email, password)`, `api.login(...)`, `api.getPerfil()`, `api.postPartida(...)`, etc. Manejo de errores unificado en componentes de UI.

> Cliente (api.js): único sitio con fetch; timeout de 15 s con AbortController; convierte las respuestas de error en ApiError (estado, código y mensaje); si una petición devuelve 401 con sesión, avisa a la interfaz de que la sesión ha caducado.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[frontend-spa-con-rutas-por-hash-y-vistas-cargadas-bajo-deman]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
