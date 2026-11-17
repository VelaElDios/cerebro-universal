---
tipo: "concepto"
titulo: "Arquitectura en capas cliente-servidor verificada (API → lógica → datos)"
temas: ["arquitectura", "backend", "grada-colchonera", "procesos", "saas"]
claves: ["src/api", "src/services", "src/repositories", "express.static", "frontera capas"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md"]
confianza: "propuesto"
fecha: "2026-11-16"
actualizado: "2026-11-16"
---

Temas: [[arquitectura]] · [[backend]] · [[grada-colchonera]] · [[procesos]] · [[saas]]

La verificación confirma la separación estricta en tres capas backend:
- `src/api/` (rutas Express) llama solo a servicios (`userService.*`).
- `src/services/` (reglas de negocio) llama solo a repositorios (`userRepository.*`).
- `src/repositories/` (acceso a datos) es la única que conoce PostgreSQL.
- `src/app.js` es el único punto donde se instancian y conectan las tres capas.
- El frontend sirve desde `public/` con `express.static` (mismo origen).
- En el navegador: `ui.js` (presentación) → `api.js` (cliente HTTP) → `/api/*`.
Esto permite testear la lógica con repositorios en memoria y cambiar de BD sin tocar servicios.

> Backend: capas API, lógica y datos en módulos separados ✅ `src/api/` → `src/services/` → `src/repositories/`. La lógica recibe el repositorio por parámetro, así que no sabe si los datos están en memoria o en PostgreSQL
> — `repo:saas/docs/revision-entrega.md` (cita sin comprobar)

Relacionado: [[arquitectura-en-capas-cliente-servidor-node-js-express-postg]] · [[modulos-del-backend-y-sus-responsabilidades]] · [[estrategia-de-pruebas-niveles-y-enfoque-error-first]]

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
