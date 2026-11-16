---
tipo: "receta"
titulo: "Manejo de errores de principio a fin: de errores tipados a UI con reintento"
temas: ["error-handling", "frontend", "grada-colchonera", "saas"]
claves: ["ValidationError", "ConflictError", "errorHandler", "ApiError", "TIMEOUT", "aviso legible"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[error-handling]] · [[frontend]] · [[grada-colchonera]] · [[saas]]

Flujo de errores: 1) Lógica lanza errores tipados (`ValidationError`, `ConflictError`, etc.). 2) `errorHandler` (middleware Express) convierte a código HTTP + cuerpo `{error: {code, message}}`. 3) Cliente `api.js` captura y lanza `ApiError` (estado, código, mensaje). 4) Vista muestra aviso, error en formulario o estado de error con botón "Reintentar". Errores inesperados → `errorHandler` devuelve 500 genérico + log `http.error` con traza. Timeout 15s → `ApiError TIMEOUT`. Redirecciones (confirmación, Google) → `?aviso=...` traducido a mensaje legible. UI: estados de carga, vacío, error con reintento; captura global de promesas rechazadas; formularios marcan campo erróneo con explicación; error de servidor muestra mensaje arriba sin borrar datos (excepto password). Usuario nunca ve JSON ni stack traces.

> El usuario nunca ve JSON ni trazas: cada error se traduce a un mensaje en español. La interfaz tiene estados de carga, vacío y error con reintento, y una captura global de promesas rechazadas. Los formularios marcan el campo con el error y lo explican debajo; al fallar el servidor, el formulario muestra el error arriba sin perder lo escrito (salvo la contraseña).
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Relacionado: [[cadena-de-middlewares-para-peticion-protegida-y-autorizacion]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
