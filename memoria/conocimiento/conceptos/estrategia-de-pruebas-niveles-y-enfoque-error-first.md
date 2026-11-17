---
tipo: "concepto"
titulo: "Estrategia de pruebas: niveles y enfoque error-first"
temas: ["grada-colchonera", "saas", "testing"]
claves: ["node:test", "pg-mem", "unitarias", "contrato", "integración", "OAuth", "simulación", "reloj inyectable"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[grada-colchonera]] · [[saas]] · [[testing]]

La suite de pruebas se ejecuta con `npm test` (Node `node:test` + `node:assert/strict`). En local usa `pg-mem` para no requerir PostgreSQL; en CI corre contra PostgreSQL 17 real. Los tests cubren: lógica pura con dependencias inyectadas (userService, tokenSigner, domainPolicy, logger, mailer); contrato del repositorio (misma batería contra implementación en memoria y PostgreSQL); integración HTTP real contra la app en puerto aleatorio con cookies (tests/helpers.js) probando 401, 403, 409; OAuth y correo con fakes (Google y SMTP); base de datos real solo en CI (api.database.test.js); frontend estático (solo api.js usa fetch, sin inyección HTML, módulos importables); simulación del juego paso a paso con semilla (jefes, ultras, colisiones, mapa, equilibrio, logros). Prioridad a casos de error (rechazos por email repetido, cuenta pendiente, permisos, último admin, enlaces manipulados/caducados, state reutilizado, resultados imposibles, doble contrato). Reloj y aleatoriedad inyectables para probar expiraciones sin esperas.

> Niveles: Unitarias de la lógica (userService, tokenSigner, domainPolicy, logger, mailer) con dependencias falsas inyectadas. Contrato del repositorio: la misma batería contra la implementación en memoria y la de PostgreSQL. Integración de la API: peticiones HTTP reales a la app montada en un puerto aleatorio (tests/helpers.js), con cookies, cubriendo 401, 403, 409… Integración con OAuth y correo: Google y SMTP sustituidos por versiones falsas (no se llama a nadie). Base de datos real (api.database.test.js, solo en el CI): registro, inicio de sesión y sesión guardada en PostgreSQL. Frontend estático: que solo api.js use fetch, que no se meta texto de usuario como HTML y que todos los módulos se importen. Simulación del juego: mundos con semilla avanzados paso a paso (jefes, ultras, colisiones, alcance del mapa, equilibrio, logros). Casos de error primero: muchas pruebas comprueban rechazos (email repetido, cuenta pendiente, usuario normal que intenta eliminar a otro, último administrador, enlace manipulado o caducado, state reutilizado, resultado de partida imposible, dos contratos a la vez). Reloj y azar inyectables para probar la caducidad de los enlaces y la validación de las partidas sin esperar.
> — `repo:saas/docs/documentacion-tecnica.md` (cita sin comprobar)

Relacionado: [[desglose-del-alcance-del-sprint-1-por-hitos-y-fechas]] · [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]] · [[estrategia-de-pruebas-error-first-y-ci-como-requisito-de-mer]] · [[arquitectura-en-capas-cliente-servidor-verificada-api-logica]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
