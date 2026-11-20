---
tipo: "concepto"
titulo: "Arquitectura en capas cliente-servidor (Node.js/Express + PostgreSQL + integraciones)"
temas: ["arquitectura", "grada-colchonera", "nodejs", "postgresql", "saas", "capas"]
claves: ["cliente-servidor", "capas", "Node.js", "Express", "frontend estático", "mismo origen", "ui.js", "api.js", "game/", "canvas", "Web Audio", "src/api", "src/services", "src/repositories", "memoria", "PostgreSQL", "Neon", "club.js", "config.js", "logros.js", "SMTP Gmail", "Google OAuth 2.0"]
proyectos: ["memoria-procesos"]
fuentes: ["repo:saas/docs/documentacion-tecnica.md", "repo:saas/docs/arquitectura.md"]
confianza: "verificado"
fecha: "2026-11-16"
actualizado: "2026-11-20"
---

Temas: [[arquitectura]] · [[grada-colchonera]] · [[nodejs]] · [[postgresql]] · [[saas]]

Arquitectura cliente-servidor en capas (sección 5.1, diagrama Mermaid):

**Navegador (cliente):**
- UI: `ui.js` + `ui/` + `vistas/` → Cliente API: `api.js` (único fetch)
- GAME: `game/` (canvas, Web Audio) → Cliente API: `api.js`
- Comunicación: HTTP + JSON + cookie de sesión

**Servidor Node.js + Express:**
- Capa API (`src/api`): rutas, sesión, roles, logs, errores
- Lógica (`src/services`): usuarios, confirmación, tokens, juego
- Datos (`src/repositories`): memoria | PostgreSQL (Neon)
- Integraciones: correo (SMTP Gmail) | Google (OAuth 2.0)
- Reglas compartidas (punteado): `club.js`, `config.js`, `logros.js` (del juego)

**Base de datos:** PostgreSQL en Neon
**Integraciones externas:** SMTP Gmail, Google OAuth 2.0

Característica clave: el servidor sirve también el frontend estático → todo en el mismo origen (simplifica CORS, cookies, despliegue).

> Arquitectura **cliente-servidor en capas**. El servidor (Node.js + Express) sirve también el frontend estático, así que todo vive en el mismo origen.
> — `repo:saas/docs/documentacion-tecnica.md`

Relacionado: [[requisitos-no-funcionales-rnf-01-a-rnf-12-del-proyecto]] · [[como-exportar-diagramas-mermaid-para-la-memoria-latex]] · [[arquitectura-en-capas-cliente-servidor-verificada-api-logica]] · [[modulos-del-backend-y-sus-responsabilidades]] · [[estrategia-de-pruebas-niveles-y-enfoque-error-first]] · [[decisiones-de-diseno-del-backend-con-alternativas-y-justific]]

## Ampliación (2026-11-16, memoria-procesos)
El sistema se organiza en siete capas con responsabilidades claras y prohibiciones explícitas: 1) Presentación (`public/`): pinta vistas, valida formularios, muestra avisos y gestiona el juego; no accede a BD ni decide permisos. 2) Cliente de la API (`public/js/api.js`): único punto con `fetch`, timeout 15 s, traduce errores a `ApiError`, avisa si caduca la sesión; no pinta nada. 3) API (`src/api/`): rutas HTTP, sesión, autenticación/autorización, registro de peticiones, formato común de errores; no contiene reglas de negocio. 4) Lógica (`src/services/`): reglas de negocio puras; no conoce HTTP ni SQL. 5) Datos (`src/repositories/`): guardar/leer en memoria o PostgreSQL con el mismo contrato; no valida reglas. 6) Integraciones (`src/integrations/`): correo y Google; no decide nada. 7) Composición (`src/app.js`, `src/bootstrap.js`): conecta capas, elige BD, migra, crea primer administrador.

## Ampliación (2026-11-20, memoria-procesos)
Capas: Presentación (pinta vistas, valida formularios, muestra avisos, juega) → Cliente API (public/js/api.js: único fetch, timeout 15s, traduce errores) → API (src/api/: rutas, sesión, auth, logs, errores) → Lógica (src/services/: reglas de negocio) → Datos (src/repositories/: memoria|PostgreSQL mismo contrato) → Integraciones (correo, Google). Composición en src/app.js y src/bootstrap.js. Inyección de dependencias por parámetro. Sesiones en servidor (express-session + PostgreSQL). Bajas lógicas con email libre (índice único parcial). Token confirmación HMAC sin BD. OAuth 2.0 con fetch. Migraciones SQL propias. Cloud Run principal, Render alternativo. Reglas juego compartidas cliente/servidor. Concurrencia optimista (version). Simulación juego pura y determinista (paso fijo 1/60s, semilla). Gráficos y sonido generados por código.

Origen: [[proyectos/memoria-procesos/estado|memoria-procesos]]
