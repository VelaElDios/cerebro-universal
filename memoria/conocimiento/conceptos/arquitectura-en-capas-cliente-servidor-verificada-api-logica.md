---
tipo: "concepto"
titulo: "Arquitectura en capas cliente-servidor verificada (API → lógica → datos)"
temas: ["arquitectura", "backend", "grada-colchonera", "procesos", "saas", "capas", "inyección-dependencias"]
claves: ["src/api", "src/services", "src/repositories", "express.static", "frontera capas"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/revision-entrega.md", "repo:saas/docs/arquitectura.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-22"
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

## Ampliación (2026-11-22, memoria-procesos)
Backend: API (rutas, sesión, roles, logs, errores) → Lógica (reglas de negocio) → Datos (memoria o PostgreSQL con mismo contrato) → Integraciones (correo, Google). Frontend: presentación (ui.js) y cliente API (api.js). La frontera interfaz/cliente queda en dos ficheros. Inyección de dependencias por parámetro permite probar la lógica con repositorios falsos.
relacionado: Decisiones técnicas y de proceso (D-01 a D-23), Modelo de datos entidad-relación

## Ampliación (2026-11-22, memoria-procesos)
|
  - **Presentación** (`public/`): pinta vistas, valida formularios, muestra avisos, juega. No habla con BD ni decide permisos.
  - **Cliente API** (`public/js/api.js`): único sitio con `fetch`; timeout 15 s; traduce errores a `ApiError`; avisa si caduca sesión.
  - **API** (`src/api/`): rutas HTTP, sesión, auth/autorización, logs, formato común errores. No contiene reglas de negocio.
  - **Lógica** (`src/services/`): reglas de negocio. No conoce HTTP ni SQL. Recibe dependencias por parámetro (inyección).
  - **Datos** (`src/repositories/`): guarda/lee (memoria o PostgreSQL) con mismo contrato. No valida reglas.
  - **Integraciones** (`src/integrations/`): correo y Google. No decide nada.
  - **Composición** (`src/app.js`, `src/bootstrap.js`): conecta capas, elige BD, migra, crea primer admin.
  
  Esta arquitectura permitió cambiar de memoria a PostgreSQL, añadir correo y Google, y montar el juego entero sin tocar la lógica existente.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
